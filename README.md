🧾 Personal Expense Tracker (Python CLI)

A simple and interactive command-line expense tracker built using Python. It allows you to record daily expenses, store them in a CSV file, and track spending by category with budget insights.

## 🚀 Features

- Add expenses with name, category, and amount  
- Stores data in `expense.csv`  
- Category-wise expense summary  
- Total spending calculation  
- Monthly budget tracking  
- Daily spending recommendation  
- Emoji-based categories with UTF-8 support

## 🗂 Project Structure

expense-tracker/  
│  
├── expense_tracker.py      # Main application logic  
├── expense.py              # Expense model/class  
├── expense.csv             # Expense records  
└── README.md               # Project documentation

## ⚙️ How to Run

1. Run the script  
```bash
python expense_tracker.py
or (Windows)

bash
Copy code
py expense_tracker.py
Follow the instructions in the terminal to add expenses and view summaries.

🧠 How It Works
User Input

Expense Name

Amount

Category Selection (🍔Food, 🏡Home, 💼Work, 🎉Fun, ✨Misc)

Saving Data

Expense entries are appended to expense.csv using UTF-8 encoding.

Summary & Budget
Displays:

📉 Category-wise totals

💸 Total spent

✅ Remaining budget

👉 Suggested daily spend limit (based on remaining days)

✅ Example Output
sql
Copy code
Running Expense Tracker!
Getting User Expense
Enter expense name: Lunch
Enter expense amount: 120
Select a category:
  1. 🍔Food
  2. 🏡Home
  3. 💼Work
  4. 🎉Fun
  5. ✨Misc
Enter a category number [1 - 5]: 1
Save User Expense: <Expense: Lunch, 🍔Food, ₹120.00> to expense.csv

Summarize User Expense
Expenses By Category 📉
  🍔Food: ₹450.00
💸Total Spent: ₹450.00
✅Budget Remaining: ₹19550.00
👉Budget Per Day: ₹650.00
🌱 Future Improvements
Edit/delete past expenses

Export to Excel

Web or GUI version

User profiles

Weekly or custom budgets

📬 Contact
Author: Anshul
GitHub: https://github.com/Anshuldhou