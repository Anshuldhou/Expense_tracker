class Expense:
    def __init__(self, name, category, amount) -> None:
        # Store expense data
        self.name = name  # What the user spent on
        self.category = category  # Expense category
        self.amount = amount  # Expense amount

    def __repr__(self):
        # How the expense will appear when printed
        return f"<Expense: {self.name}, {self.category}, ₹{self.amount:.2f}>"
