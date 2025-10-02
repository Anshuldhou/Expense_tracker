from expense import Expense
import calendar
import datetime

# Main function to drive the program
def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expense.csv"  # CSV file to store expenses
    budget = 20000  # Set a fixed budget

    # Get expense details from user
    expense = get_user_expense()

    # Save the expense to file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize all expenses
    summarize_expense(expense_file_path, budget)


# Function to collect expense details from the user
def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    # Predefined categories
    expense_categories = [
        "🍔Food",
        "🏡Home",
        "💼Work",
        "🎉Fun",
        "✨Misc"
    ]

    # Show category options
    while True:
        print("Select a category: ")
        for i, categories_name in enumerate(expense_categories):
            print(f"  {i + 1}. {categories_name}")

        # Get valid index
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        # Return Expense object if valid
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category.. Please try again!!")


# Save expense data to CSV file
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Save User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


# Function to summarize expenses from the file
def summarize_expense(expense_file_path, budget):
    print(f"Summarize User Expense")
    expenses: list[Expense] = []

    # Read all expenses
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)

    # Group by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount

    print("Expenses By Category 📉")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    # Total spent
    total_spent = sum([x.amount for x in expenses])
    print(f"💸Total Spent: ₹{total_spent:.2f}")

    # Remaining budget (no negative)
    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print(green(f"⚠️ Budget Exceeded by ₹{abs(remaining_budget):.2f}!"))
    else:
        print(f"✅Budget Remaining: ₹{remaining_budget:.2f}")

    # Remaining days calculation
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days <= 0:
        print("📅 No days left in this month!")
    else:
        daily_budget = remaining_budget / remaining_days
        print(green(f"👉Budget Per Day: ₹{daily_budget:.2f}"))


# Function to print green-colored text in terminal
def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
