from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, CartItem


def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )

def product_create(request):

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        if not product_name or not category or not price or not quantity:
            messages.error(request, 'Please fill in all fields.')
            return redirect('product_create')
        Product.objects.create(
            product_name=product_name,
            category=category,
            price=price,
            quantity=quantity
        )
        messages.success(
            request,
            'Product added successfully!'
        )

        return redirect('product_list')

    return render(
        request,
        'products/product_form.html'
    )

def product_update(request, id):

    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        messages.success(
            request,
            'Product updated successfully!'
        )

        return redirect('product_list')

    return render(
        request,
        'products/product_form.html',
        {'product': product}
    )

def product_delete(request, id):

    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(
            request,
            'Product deleted successfully!'
        )
        return redirect('product_list')

    return render(
        request,
        'products/product_confirm_delete.html',
        {'product': product}
    )

def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )
    if not created:
        if cart_item.quantity < product.quantity:
            cart_item.quantity += 1
            cart_item.save()
    messages.success(
        request,
        f"{product.product_name} added to your cart!"
    )

    return redirect('product_list')

def cart_view(request):

    cart_items = CartItem.objects.select_related(
        'product'
    ).all()
    total = sum(
        item.total_price()
        for item in cart_items
    )
    cart_count = sum(
        item.quantity
        for item in cart_items
    )

    return render(
        request,
        'products/cart.html',
        {
            'cart_items': cart_items,
            'total': total,
            'cart_count': cart_count,
        }
    )