from typing import List, Tuple
import products  # Importing the Product class from products.py


class Store:
    def __init__(self, product_list: List[products.Product]):
        self.products = product_list  # List of Product instances

    # Add a product to the store
    def add_product(self, product: products.Product):
        self.products.append(product)

    # Remove a product from the store
    def remove_product(self, product: products.Product):
        if product in self.products:
            self.products.remove(product)

    # Get total quantity of all products in the store
    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    # Get all active products
    def get_all_products(self) -> List[products.Product]:
        return [product for product in self.products if product.is_active()]

    # Place an order of multiple products
    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0.0
        # First, check if all purchases are valid before modifying quantities
        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError("Quantity must be positive for all items in the order.")
            if quantity > product.get_quantity():
                raise ValueError(
                    f"Cannot buy {quantity} of {product.name}. Only {product.get_quantity()} available."
                )
        # If all checks passed, buy the products
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price



if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())  # Should print 850 (100+500+250)

    order_price = best_buy.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Order cost: {order_price} dollars.")  # Should print the total price of the order
