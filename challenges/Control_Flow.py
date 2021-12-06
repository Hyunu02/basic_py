# Large Power
# RETURN TRUE WHEN BASE RAISED TO THE EXPONENT IS
# GREATER THAN 5000, OTHERWISE RETURN FALSE
def large_power(base, exponent):
    res = base ** exponent
    if(res > 5000): return True
    return False

# Over Budget
# RETURN TRUE IF ALL SUM OF SPENDING IS GONE
# OVER BUDGET, OTHERWISE RETURN FALSE
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    sum = food_bill + electricity_bill + internet_bill + rent
    if budget < sum: return True
    return False