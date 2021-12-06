# Append Size
# CALCULATE LENGTH AND APPEND TO THE END
def append_size(lst):
    lst.append(len(lst))
    return lst

# Append Sum
# calculates sum of the last two elements of a list
# and appends it to the end
def append_sum(lst):
    for i in range(3):
        lst.append(lst[-1] + lst[-2])
    return lst

# Larger List
# return last item of the belt which contains more item
def larger_list(lst1, lst2):
    if (len(lst1) >= len(lst2)):
        return lst1[-1]
    return lst2[-1]

# Mora Than N
# CHECKS NUMBER OF INSTANCES OF A CERTAIN TYPE
def more_than_n(lst, item, n):
    count = 0
    for i in lst:
        if i == item:
            count += 1
    if count > n: return True
    # could also use lst.count(item)
    return False

# Combine Sort
# COMBINES TWO LISTS AND THEN SORTS THEM
def combine_sort(lst1, lst2):
    newLst = lst1 + lst2
    newLst.sort()
    # sortedList = sorted(newLst) to not change directly the list
    return newLst