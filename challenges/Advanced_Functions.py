# First Three Multiplies
# PRINT 1, 2, 3 TIMES AND RETURN 3 TIMES NUMBER
def first_three_multiples(num):
    for i in range(1, 4):
        print(num * i)
    return num * i

# Tip
# RETURNS VALUE OF TIP
def tip(total, percentage):
    return total * percentage / 100

# Bond, James Bond
# CONCATENATE STRINGS TO REPLACE NAME
def introduction(first_name, last_name):
    return ("{l}, {f} {l}".format(f = first_name, l = last_name))
    # return last_name + ", " + first_name + " " + last_name

# Dog Years
# CALCULATES A DOG'S AGE IN DOG YEARS
def dog_years(name, age):
    return ("{name}, you are {age} years old in dog years".format(name = name, age = age * 7))
    # return name+", you are "+str(age * 7)+" years old in dog years"

# All Operations
# PERFORMS MULTIPLE MATHEMATICAL OPERATIONS ON MULTI INPUTS
def lots_of_math(a, b, c, d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return ((a + b) * (c - d)) % a