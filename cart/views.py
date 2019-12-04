from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from blog.models import Product, Variation


def cart_home(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart, "empty": False}
        new_total = 0.00
        for item in cart.cart_items.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cart_items.count()
        cart.total = new_total
        cart.save()

    else:
        empty_message = "Your cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}

    template = 'cart/cart_home.html'
    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    # cartitem.cart = None
    # cartitem.save()
    #send success message
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, slug):
    request.session.set_expiry(12000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    product_var = [] # product variations
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)

        if len(product_var) > 0:
            cart_item.variations.add(*product_var)

        cart_item.quantity = qty
        cart_item.line_total = float(cart_item.product.price) * float(qty)
        cart_item.save()
    else:
        return HttpResponseRedirect(reverse("cart"))

    return HttpResponseRedirect(reverse("cart"))
