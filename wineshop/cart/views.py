from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Wine
from django.http import JsonResponse
from django.contrib import messages


def cart_summery(request):
    cart = Cart(request)
    cart_products = cart.get_products

    quantities = cart.get_quants
    totals = cart.total()

    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'totals': totals

    }
    return render(request, 'Cart/cart_summery.html', context)


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        wine_id = int(request.POST.get('wine_id'))
        wine_qty = int(request.POST.get('wine_qty'))
        wine = get_object_or_404(Wine, id=wine_id)
        cart.add(wine=wine, quantity=wine_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, 'Product added successfully!')
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        wine_id = int(request.POST.get('wine_id'))
        cart.delete(wine=wine_id)
        response = JsonResponse({'wine': wine_id})
        messages.success(request, 'Item deleted successfully!')
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        wine_id = int(request.POST.get('wine_id'))
        wine_qty = int(request.POST.get('wine_qty'))

        cart.update(wine=wine_id, quantity=wine_qty)
        response = JsonResponse({'qty': wine_qty})
        messages.success(request, f'Product updated successfully!')
        return response

