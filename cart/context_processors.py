from .cart import Cart

def default(request):
    cart = Cart(request)
    return {'cart':cart}

