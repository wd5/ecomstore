from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
import cart

def show_cart(request, template_name="cart/cart.html"):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    c = locals()
    c.update(csrf(request))
    return render_to_response(template_name, c, context_instance=RequestContext(request))