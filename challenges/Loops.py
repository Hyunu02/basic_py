# Divisible By Ten
# CHECKS HOW MANY NUMBERS ARE DIVISIBLE BY TEN
def divisible_by_ten(nums):
    counter = 0
    for number in nums:
        if i % 10 == 0:
            counter += 1
    return counter

# Greetings
# Prepend 'Hello, ' string before name
def add_greetings(names):
    greeting = []
    for name in names:
        greeting.append('Hello, ' + name)
    return greeting

# Delete Starting Even Numbers
# REMOVES FIRST ELEMENT OF A LIST UNTIL IT FINDS AN 
# ODD NUMBER OR RUNS OUT OF ELEMENTS
def delete_starting_evens(lst):
    for i in range(len(lst)):
        if lst[0] % 2 == 0:
            lst.pop(0)
        else:
            break
    print("\n")
    return lst

    # while (len(lst) > 0 and lst[0] % 2 == 0):
    #   lst = lst[1:]
    # return lst

# Odd Indices
# GIVES VALUES AT EVERY ODD INDEX
def odd_indices(lst):
    newLst = []
    for i in range(len(lst)):
        if i % 2 != 0:
            newLst.append(lst[i])
    return newLst

# Exponents
# EVERY NUMBER IN THE FIRST LIST IS RAISED
# TO POWER OF EVERY NUMBER IN SECOND LIST
def exponents(bases, powers):
    res = []
    for base in bases:
        for power in powers:
            res.append(base ** power)
    return res
