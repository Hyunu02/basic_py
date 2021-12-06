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

# Twice As Large
# CHECKS IF NUM1 IS TWICE AS LARGE THAN NUM2
def twice_as_large(num1, num2):
    if num1 > num2 * 2: return True
    return False

# Divisible By Ten
# VERIFIES IF NUM IS DIVISIBLE BY TEN
def divisible_by_ten(num):
    if num % 10 == 0: return True
    return False

# Not Sum To Ten
# CHECK IF SUMMATION OF TWO INPUTS DOESN'T EQUAL TEN
def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10): return True
    return False