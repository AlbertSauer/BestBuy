import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def start(store_obj: store.Store):
    while True:
        print("\nWelcome to the Store! Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            active_products = store_obj.get_all_products()
            if not active_products:
                print("No active products available.")
            else:
                print("\nProducts in the store:")
                for idx, product in enumerate(active_products, start=1):
                    print(f"{idx}. ", end="")
                    product.show()

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal quantity of items in the store: {total_quantity}")

        elif choice == "3":
            active_products = store_obj.get_all_products()
            if not active_products:
                print("No active products available to order.")
                continue

            print("\nAvailable products:")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")

            shopping_list = []
            while True:
                prod_choice = input("Enter the product number to buy (or 'done' to finish): ").strip()
                if prod_choice.lower() == "done":
                    break
                if not prod_choice.isdigit() or int(prod_choice) < 1 or int(prod_choice) > len(active_products):
                    print("Invalid choice, try again.")
                    continue

                prod_idx = int(prod_choice) - 1
                quantity = input(f"Enter quantity for {active_products[prod_idx].name}: ").strip()
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity, try again.")
                    continue

                shopping_list.append((active_products[prod_idx], int(quantity)))

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\nOrder successful! Total price: {total_price} dollars.")
                except ValueError as e:
                    print(f"\nError processing order: {e}")

        elif choice == "4":
            print("Thank you for visiting! Goodbye.")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 4.")


# Start the prgram
if __name__ == "__main__":
    start(best_buy)
