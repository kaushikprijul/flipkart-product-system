from django.urls import path
from . import views


urlpatterns = [

    # Product list
    path(
        '',
        views.product_list,
        name='product_list'
    ),

    # Add product
    path(
        'add/',
        views.product_create,
        name='product_create'
    ),

    # Edit product
    path(
        'edit/<int:id>/',
        views.product_update,
        name='product_update'
    ),

    # Delete product
    path(
        'delete/<int:id>/',
        views.product_delete,
        name='product_delete'
    ),

    # Add product to cart
    path(
        'cart/add/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    # Cart page
    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),
]