# 45
def task45_salary_after_tax(salary, tax_rate=0.15):
    """
    Task 45:
    Write a function that calculates net salary after deducting tax.
    Example: salary_after_tax(100000) → 85000
    """
    rate = salary * tax_rate
    net_salary = salary - rate
    return f"Salary: {salary}, Tax Rate: {tax_rate} → Net Salary: {net_salary}"

print(task45_salary_after_tax(100000))