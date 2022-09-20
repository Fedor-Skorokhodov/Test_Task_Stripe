from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('item/<int:key>', views.item_view, name='item-page'),
    path('buy/<int:key>', views.buy_view, name='buy-page'),
    path('buy_order', views.buy_order_view, name='buy-order-page'),
    path('add_to_order/<int:key>', views.add_to_order_view, name='add-to-order-page'),
    path('remove_from_order/<int:key>', views.remove_from_order_view, name='remove-from-order-page'),
    path('cart', views.order_view, name='cart-page'),
    path('activate_coupon', views.activate_coupon_view, name='coupon-page'),

]