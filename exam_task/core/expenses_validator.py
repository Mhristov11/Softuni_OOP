class ExpensesValidator:
    @staticmethod
    def validate(expenses):
        if expenses < 0.00:
            raise ValueError("Expenses cannot be a negative number!")
        return expenses
