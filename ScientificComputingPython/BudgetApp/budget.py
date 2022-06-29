# Solution by Patricia Ternes <patricia.terdal@gmail.com>
# https://github.com/patricia-ternes/freeCodeCamp-projects/blob/main/ScientificComputingPython/BudgetApp/budget.py

from itertools import zip_longest


class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []

    def __repr__(self):
        msg = [
            "{:<23.23s}{:>7.2f}".format(p["description"], p["amount"])
            for p in self.ledger
        ]
        msg = "\n".join(["{:*^30}".format(self.name), "\n".join(msg)])
        msg = "\n".join([msg, "Total: {:.2f}".format(self.get_balance())])
        return msg

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -amount, "description": description})
        return funds

    def transfer(self, amount, category):
        transaction = self.withdraw(amount, " ".join(["Transfer to", category.name]))
        if transaction:
            category.deposit(amount, " ".join(["Transfer from", self.name]))
        return transaction

    def get_balance(self):
        return sum([p["amount"] for p in self.ledger])

    def check_funds(self, amount):
        return self.get_balance() >= amount


def create_spend_chart(categories):

    # Get total withdraw
    total = [
        -sum([p["amount"] for p in category.ledger if p["amount"] < 0])
        for category in categories
    ]
    # Normalize
    total = [item / sum(total) * 100 for item in total]

    # Create percentage labels
    bar = range(100, -1, -10)
    chart = ["{:>3d}|".format(i) for i in bar]

    # Fill bars with 'o'
    for value in total:
        chart = [
            chart[i] + "   " if item > value else chart[i] + " o "
            for i, item in enumerate(bar)
        ]

    # # Add title and break lines.
    chart = "\n".join(["Percentage spent by category", " \n".join(chart)])

    # # Add horizontal line
    chart = "".join([chart, " \n    ", len(total) * "---", "-"])

    # Add vertical categories.
    text = "  ".join([category.name for category in categories])
    for x in zip_longest(*text.split(), fillvalue=" "):
        chart = "".join([chart, "\n     ", "  ".join(x), "  "])

    return chart
