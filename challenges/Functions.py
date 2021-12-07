# Tenth Power
# TAKES TENTH POWER OF A NUMBER
def tenth_power(num):
    return num ** 10

# Square Root
# TAKES SQUARE ROOT OF A NUMBER
def square_root(num):
    for i in range(num):
        if i ** 2 == num:
            return i
    return False
    # return num ** 0.5

# Win Percentage
# CALCULATES THE PERCENTAGE OF GAMES WON
def win_percentage(wins, losses):
    total = wins + losses
    return round(wins / total * 100)

# Average
# TAKES THE AVERAGE OF TWO NUMBERS
def average(num1, num2):
    sum = num1 + num2
    return sum / 2

# Remainder
# TAKES THE REMAINDER OF TWO NUMBER
def remainder(num1, num2):
    num1 = num1 * 2
    num2 = num2 / 2
    return num1 % num2