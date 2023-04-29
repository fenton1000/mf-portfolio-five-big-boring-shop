from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import UserProfile, Favourites, Rating
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
