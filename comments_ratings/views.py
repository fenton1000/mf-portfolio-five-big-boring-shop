from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import datetime
from .models import CommentRating

from products.models import Product


@login_required
@require_POST
def comment_rate_product(request, product_id):
    """
    Add comment and rating to CommentRating database for the
    specified product and user and re-calculate the rating and
    number of raters for the product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    comment = request.POST.get('comment')
    redirect_url = request.POST.get('redirect_url')
    user_rating = int(request.POST.get('user_rating'))

    if user_rating == 0:
        user_rating = None

    CommentRating.objects.create(
        user=user,
        product=product,
        user_rating=user_rating,
        comment=comment,
    )

    if user_rating:
        current_num_of_raters = product.num_of_raters

        if current_num_of_raters == 0:
            product.rating = user_rating
            product.num_of_raters = 1
        else:
            sum_of_all_ratings = (
                product.rating * current_num_of_raters + user_rating
            )
            product.num_of_raters += 1
            product.rating = sum_of_all_ratings/product.num_of_raters

        product.save()
    messages.success(
        request,
        f'Your comment/rating for {product.name} has been added'
        )
    return redirect(redirect_url)


@login_required
def edit_product_comment_rating(request, product_id):
    """
    Update a rating or comment in the CommentRating database
    for the specified product and user and re-calculate the
    rating for the product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    comment_rating_entry = get_object_or_404(
        CommentRating,
        user=user,
        product=product
        )
    if request.method == 'POST':
        new_comment = request.POST.get('comment')
        comment_rating_entry.comment = new_comment
        comment_rating_entry.date_updated = datetime.datetime.now()
        redirect_url = request.POST.get('redirect_url')

        if 'user_rating' in request.POST:
            new_user_rating = int(request.POST.get('user_rating'))
            if comment_rating_entry.user_rating:
                current_rating = comment_rating_entry.user_rating
                sum_of_all_ratings = (
                    (product.rating * product.num_of_raters - current_rating)
                    + new_user_rating
                )
                product.rating = sum_of_all_ratings/product.num_of_raters
            else:
                if product.num_of_raters == 0:
                    product.rating = new_user_rating
                    product.num_of_raters = 1
                else:
                    sum_of_all_ratings = (
                        product.rating
                        * product.num_of_raters
                        + new_user_rating
                    )
                    product.num_of_raters += 1
                    product.rating = sum_of_all_ratings/product.num_of_raters

            product.save()
            comment_rating_entry.user_rating = new_user_rating

        comment_rating_entry.save()
        messages.success(
            request, f'Your comment/rating for {product.name} has been updated'
        )
        return redirect(redirect_url)
    else:
        redirect_url = request.GET['redirect_url']
        template = 'comments_ratings/edit_comment_form.html'
        context = {
            'comment_rating_entry': comment_rating_entry,
            'redirect_url': redirect_url,
        }
        return render(request, template, context)


@login_required
def delete_product_comment_rating(request, product_id):
    """
    Delete a comment/rating entry in the CommentRating database for
    the specified product and user
    and re-calculate the rating for the
    product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.GET['redirect_url']
    comment_rating_entry = get_object_or_404(
        CommentRating,
        user=user,
        product=product
    )

    if comment_rating_entry.user_rating:
        current_rating = comment_rating_entry.user_rating
        new_num_of_raters = product.num_of_raters - 1

        if new_num_of_raters == 0:
            product.rating = None
            product.num_of_raters = 0
        else:
            sum_of_all_ratings = (
                product.rating * product.num_of_raters - current_rating
            )
            product.rating = sum_of_all_ratings/new_num_of_raters
            product.num_of_raters = new_num_of_raters

        product.save()
    comment_rating_entry.delete()
    messages.success(
        request, f'Your comment/rating for {product.name} has been deleted'
    )
    return redirect(redirect_url)
