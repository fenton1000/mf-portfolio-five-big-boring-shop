from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm
from comments_ratings.models import CommentRating
from favourites.models import Favourites


def products(request):
    """ A view to return the products page including sorting and searching """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            search_category = request.GET['category']
            products = products.filter(category__name=search_category)
            category = get_object_or_404(Category, name=search_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__friendly_name__icontains=query)
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    all_comments_ratings = CommentRating.objects.filter(product=product)
    current_user_comment_rating = None
    on_favourites = False
    from_profile = None
    if user.is_authenticated:
        current_user_comment_rating = CommentRating.objects.filter(
            user=user,
            product=product
        )
        if Favourites.objects.filter(product=product, user=user).exists():
            on_favourites = True

    if request.GET:
        if 'from_profile' in request.GET:
            from_profile = True

    context = {
        'product': product,
        'current_user_comment_rating': current_user_comment_rating,
        'all_comments_ratings': all_comments_ratings,
        'on_favourites': on_favourites,
        'from_profile': from_profile
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
