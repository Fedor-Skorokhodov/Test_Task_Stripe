from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Item, Discount
from .factories import create_stripe_checkout_session, get_or_create_order


@require_http_methods(['GET'])
def item_view(request, key):
    try: item = Item.objects.get(id=key)
    except: return HttpResponseNotFound()

    order = get_or_create_order(request)
    if order.items.all().filter(id=key).exists():
        added_to_cart = True
    else:
        added_to_cart = False

    context = {'item': item, 'session_key': request.session.session_key, 'added_to_cart': added_to_cart}
    return render(request, 'base/item.html', context=context)


@require_http_methods(['GET'])
def buy_view(request, key):
    add_to_order_view(request, key)
    return buy_order_view(request)


@require_http_methods(['GET'])
def buy_order_view(request):
    order = get_or_create_order(request)
    session_id = create_stripe_checkout_session(order)

    return JsonResponse({'session_id': session_id})


@require_http_methods(['GET'])
def add_to_order_view(request, key):
    try: item = Item.objects.get(id=key)
    except: return HttpResponse('Failure')

    order = get_or_create_order(request)
    order.items.add(item)
    order.save()
    return HttpResponse('Success')


@require_http_methods(['GET'])
def remove_from_order_view(request, key):
    try: item = Item.objects.get(id=key)
    except: return HttpResponse('Failure')

    order = get_or_create_order(request)
    if order.items.all().filter(id=key).exists():
        order.items.remove(item)
    return HttpResponse('Success')


@require_http_methods(['GET'])
def activate_coupon_view(request):
    order = get_or_create_order(request)
    discount = Discount.objects.get(rate=5)
    order.discount = discount
    order.save()
    return 'Success'


@require_http_methods(['GET'])
def order_view(request):
    order = get_or_create_order(request)
    context = {'session_key': request.session.session_key, 'order': order}
    return render(request, 'base/order.html', context=context)


def home_view(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'base/home.html', context=context)
