# Larger Sum
# Calculate which list has the larger fum
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number1 in lst1:
        sum1 += number1
    for number2 in lst2:
        sum2 += number2
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

# Over 9000
# Sum until it reaches 9000
def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if (sum > 9000):
            break
    return sum

# Max Num
# RETURNS THE MAX VALUE OF A LIST
def max_num(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return  max

# Same Values
# records index tf numbers are equal
def same_values(lst1, lst2):
    index = []
    for ind in range(len(lst1)):
        if lst1[ind] == lst2[ind]:
            index.append(ind)
    return index

# Reversed List
# CHECK IF SECOND LIST IS REVERSE OF FIRST
def reversed_list(lst1, lst2):
    reverse_index = -1
    for i in range(len(lst1)):
        if lst1[i] != lst2[reverse_index]:
            return False
        reverse_index -= 1
    return True

    # reverse_index = lst2[len(lst2) - 1 - index]