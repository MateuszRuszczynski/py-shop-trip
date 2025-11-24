import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, product_cart: dict) -> float:
        total_price = 0
        for product, quantity in product_cart.items():
            total_price += quantity * self.products[product]
        return total_price

    def print_receipt(self, customer: "Customer", cart_item: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart_item.items():
            price = self.products[product]
            cost = price * quantity
            if cost.is_integer():
                cost_str = str(int(cost))
            else:
                cost_str = str(cost)
            print(f"{quantity} {product}s for {cost_str} dollars")

        total = self.calculate_cart_cost(cart_item)
        if total.is_integer():
            total_str = str(int(total))
        else:
            total_str = str(total)

        print(f"Total cost is {total_str} dollars")
        print("See you again!")
        print()
