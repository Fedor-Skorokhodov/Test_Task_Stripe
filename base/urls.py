from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:key>', views.item_view, name='item-page'),
    path('buy/<int:key>', views.buy_view, name='buy-page'),

]