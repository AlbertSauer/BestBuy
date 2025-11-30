class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Products start as active by default

    # Getter for quantity
    def get_quantity(self) -> int:
        return self.quantity

    # Setter for quantity
    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    # Check if product is active
    def is_active(self) -> bool:
        return self.active

    # Activate product
    def activate(self):
        self.active = True

    # Deactivate product
    def deactivate(self):
        self.active = False

    # Show product information
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    # Buy a quantity of the product
    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError(f"Cannot buy {quantity} items. Only {self.quantity} available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Should print 12500
    print(mac.buy(100))  # Should print 145000
    print(mac.is_active())  # Should print False, because quantity reached 0

    bose.show()  # Should print Bose product info
    mac.show()  # Should print MacBook info

    bose.set_quantity(1000)
    bose.show()  # Should show updated quantity
