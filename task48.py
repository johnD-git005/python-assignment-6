# 48
def task48_banking_withdraw(balance, withdraw_amount):
    """
    Task 48:
    Write a function to simulate ATM withdrawal.
    - If withdraw_amount <= balance, return new balance
    - Otherwise return "Insufficient funds"
    """
    if withdraw_amount > balance:
        return "Insuficient Funds!"

    elif withdraw_amount < 0:
        return "Invalid Input for Withdrawal Amount"

    else:
        balance -= withdraw_amount
        return f"Withdrawal: {withdraw_amount}, Balance: {balance}"

print(task48_banking_withdraw(1000, 100))