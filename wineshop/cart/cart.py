from shop.models import Wine


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get current session key
        cart = self.session.get('session_key')

        # If the user is new, no session key. Create one !

        if "session_key" not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart works on all pages

        self.cart = cart

    def add(self, wine, quantity):
        wine_id = str(wine.id)
        wine_qty = str(quantity)
        if wine_id in self.cart:
            pass
        else:
            self.cart[wine_id] = int(wine_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        wine_ids = self.cart.keys()
        products = Wine.objects.filter(id__in=wine_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, wine, quantity):
        wine_id = str(wine)
        wine_qty = int(quantity)
        our_cart = self.cart
        our_cart[wine_id] = wine_qty
        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, wine):
        wine_id = str(wine)
        if wine_id in self.cart:
            del self.cart[wine_id]
        self.session.modified = True

    def total(self):
        wine_id = self.cart.keys()
        wines = Wine.objects.filter(id__in=wine_id)
        quantity = self.cart
        total_price = 0
        for key, value in quantity.items():
            key = int(key)
            for wine in wines:
                if wine.id == key:
                    if wine.is_sale:
                        total_price += wine.sale_price * value
                    else:
                        total_price += wine.price * value
        return total_price
