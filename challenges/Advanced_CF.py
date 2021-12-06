# In Range
# checks if a number falls within a certain range
def in_range(num, lower, upper):
    return (lower <= num <= upper)

# Same Name
# checks if names are equal
def same_name(your_name, my_name):
    if (your_name == my_name):
        return True
    return False

# Always False
# always return False (contradiction)
def always_false(num):
    if (num < 0 and num > 0):
        return True
    return False

# Movie Review
# reviews a movie based on rating
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    if rating < 9:
        return "This one was fun."
    return "Outstanding!"

# Max Number
# selects number that is greatest from three input
def max_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    if (num2 > num1 and num2 > num3):
        return num2
    if (num3 > num1 and num3 > num2):
        return num3
    return "It's a tie!"