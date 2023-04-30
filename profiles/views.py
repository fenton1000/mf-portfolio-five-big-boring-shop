from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import UserProfile, Favourites, Rating, Comment
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    favourites = Favourites.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favourites': favourites,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def delete_favourite(request, product_id):
    """ Delete a product from user favourite list """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    favourite = get_object_or_404(Favourites, user=user, product=product)
    favourite.delete()
    messages.success(request, 'Product deleted from favourites!')
    return redirect('profile')


@login_required
@require_POST
def rate_product(request, product_id):
    """
    Add a rating to the Rating database for the specified product and user
    and re-calculate the rating and number of raters for the
    product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    user_rating = int(request.POST.get('user_rating'))
    redirect_url = request.POST.get('redirect_url')

    if Rating.objects.filter(
        user=user,
        product=product,
    ).exists():
        messages.warning(request, 'You have already rated this product!')
        return redirect(redirect_url)

    Rating.objects.create(
        user=user,
        product=product,
        user_rating=user_rating,
    )

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
    messages.success(request, f'Your rating for {product.name} has been added')
    return redirect(redirect_url)


@login_required
@require_POST
def edit_product_rating(request, product_id):
    """
    Update a rating in the Rating database for the specified product and user
    and re-calculate the rating for the product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    new_user_rating = int(request.POST.get('user_rating'))
    redirect_url = request.POST.get('redirect_url')
    rating_entry = get_object_or_404(Rating, user=user, product=product)
    current_rating = rating_entry.user_rating

    rating_entry.user_rating = new_user_rating
    rating_entry.save()

    sum_of_all_ratings = (
        (product.rating * product.num_of_raters - current_rating)
        + new_user_rating
    )
    product.rating = sum_of_all_ratings/product.num_of_raters

    product.save()
    messages.success(
        request, f'Your rating for {product.name} has been updated'
    )
    return redirect(redirect_url)


@login_required
def delete_product_rating(request, product_id):
    """
    Delete a rating entry in the Rating database for
    the specified product and user
    and re-calculate the rating for the
    product in the Product db.
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.GET['redirect_url']
    rating_entry = get_object_or_404(Rating, user=user, product=product)
    current_rating = rating_entry.user_rating

    rating_entry.delete()

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
    messages.success(
        request, f'Your rating for {product.name} has been deleted'
    )
    return redirect(redirect_url)


@login_required
@require_POST
def add_comment(request, product_id):
    """
    Add a comment to the Comment database for the specified product and user
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    comment = request.POST.get('comment')
    redirect_url = request.POST.get('redirect_url')

    Comment.objects.create(
        user=user,
        product=product,
        comment=comment,
    )

    messages.success(request, f'Your comment on {product.name} has been added')
    return redirect(redirect_url)


@login_required
def edit_comment(request, comment_id):
    """
    Update a comment in the Comment database for the specified product and user
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        redirect_url = request.POST.get('redirect_url')
        edited_comment = request.POST.get('edited_comment')
        comment.comment = edited_comment
        comment.save()
        messages.success(
            request, f'Your comment on {comment.product.name} has been edited'
        )
        return redirect(redirect_url)
    else:
        redirect_url = request.GET['redirect_url']
        template = 'profiles/edit_comment_form.html'
        context = {
            'comment': comment,
            'redirect_url': redirect_url,
        }
        return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment in the Comment database
    for the loggin in user
    """

    comment = get_object_or_404(Comment, pk=comment_id)
    product_name = comment.product.name
    redirect_url = request.GET['redirect_url']
    comment.delete()

    messages.success(
        request, f'Your comment on {product_name} has been deleted'
    )
    return redirect(redirect_url)
