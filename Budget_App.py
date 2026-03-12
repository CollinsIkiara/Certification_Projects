# Budget App

# This code defines a `Category` class to manage budget categories. The `Category` class allows for deposits, withdrawals, transfers, and balance checks.
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""

        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# The `create_spend_chart` function generates a bar chart representing the percentage of total withdrawals for each category.
def create_spend_chart(categories):

    withdrawals = [
        sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        for cat in categories
    ]

    total = sum(withdrawals)

    percentages = [int((w / total) * 100) // 10 * 10 for w in withdrawals]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")


# ----------------------
# Example Usage
# ----------------------

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing.deposit(500, "initial deposit")
clothing.withdraw(25.55, "shirt")
clothing.withdraw(100, "jacket")

auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")
auto.withdraw(200, "repairs")

food.transfer(50, clothing)

print(food)
print() # Blank line for better readability
print(clothing)
print() # Blank line for better readability
print(auto)
print() # Blank line for better readability

print(create_spend_chart([food, clothing, auto]))

# Complete!