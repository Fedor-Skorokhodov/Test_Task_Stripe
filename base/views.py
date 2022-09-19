from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Item
import stripe

# test key
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

DOMAIN = 'http://127.0.0.1:8000'


@require_http_methods(['GET'])
def item_view(request, key):
    try: item = Item.objects.get(id=key)
    except: return HttpResponseNotFound()

    return render(request, 'base/item.html', context={'item': item})


@require_http_methods(['GET'])
def buy_view(request, key):
    try: item = Item.objects.get(id=key)
    except: return HttpResponseNotFound()

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': item.price*100,
                    'product_data': {
                        'name': item.name
                    }

                },
                'quantity': 1
            }
        ],
        mode='payment',
        success_url=DOMAIN + '/item/' + str(item.id),
        cancel_url=DOMAIN + '/item/' + str(item.id),
    )

    session_id = checkout_session.id
    return JsonResponse({'session_id': session_id})

