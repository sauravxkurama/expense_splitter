from expense_manager import ExpenseManager
from optimizer import minimize_transactions
from utils import save_data, load_data


manager = ExpenseManager()

while True:
    print("\n📌 Choose an option:")
    print("1. Add Expense")
    print("2. Show Balances")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        paid_by = input("Paid by: ")
        amount = float(input("Amount: "))
        participants = input("Participants (comma-separated): ").split(',')
        participants = [p.strip() for p in participants]
        manager.add_expense(paid_by, amount, participants)
        print("✅ Expense added.")
    
    elif choice == '2':
        print("\n🔍 Current Balances:")
        manager.show_balances()

    elif choice == '3':
        print("👋 Exiting. See you!")
        break

    else:
        print("❌ Invalid choice. Try again.")
