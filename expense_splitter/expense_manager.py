class ExpenseManager:
    def __init__(self):
        self.balances = {}

    def add_expense(self, paid_by, amount, participants):
        split_amount = amount / len(participants)

        for person in participants:
            if person not in self.balances:
                self.balances[person] = 0.0
            self.balances[person] -= split_amount

        self.balances[paid_by] += amount

    def show_balances(self):
        for person, balance in self.balances.items():
            if abs(balance) > 0.01:
                status = "owes" if balance < 0 else "is owed"
                print(f"{person} {status} ₹{abs(balance):.2f}")
            else:
                print(f"{person} is settled up")
 