class Cart(object):
    def __init__(self):
        self.item_list = []
        self.number_of_items = 0

    def add_item_to_cart(self, item=''):
        self.item_list.append(item.lower())
        self.__number_of_item_in_cart()
        print("{} added to cart".format(item))

    def add_list_to_cart(self, item):
        """Add a list to a cart."""
        for element in item:
            self.item_list.append(element.lower())

        print("Added {} to cart".format(item))
        for element in item:
            self.__number_of_item_in_cart()

    def remove_from_cart(self, item=''):
        """Remove item from a cart"""
        item = item.lower()
        if item in self.item_list:
            self.item_list.remove(item)
            self.__decrease_item()
        else:
            print("{} not in cart".format(item))

    def __number_of_item_in_cart(self):
        self.number_of_items += 1

    def __decrease_item(self):
        self.number_of_items -= 1

    def __str__(self):
        return "Items in your cart {}".format(self.item_list)


def main():
    cart = Cart()
    cart.add_item_to_cart("Coffee Maker")
    my_list = ["Blender", "Oven", "Iron", "Electric Kettle"]
    cart.add_list_to_cart(my_list)
    print(cart)
    print("Number of items in cart: {}".format(cart.number_of_items))

    print('\n')
    cart.remove_from_cart("Oven")
    print(cart)
    print("Number of items in cart: {}".format(cart.number_of_items))


main()
