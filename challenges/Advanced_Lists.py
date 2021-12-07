# Every Three Numbers
# CREATES A LIST OF NUMBERS UP TO 100 IN
# INCREMENT OF 3 STARTING FROM INPUT PASSED
def every_three_nums(start):
    lst = list((range(start, 101, 3)))
    return lst

# Remove Middle
# REMOVE ALL ELEMENTS WITHIN A RANGE
def remove_middle(lst, start, end):
    count = start
    while count != end + 1:
        lst.pop(start)
        count += 1
    return lst
    # return lst[:start] + lst[end+1:]

# More Frequent Item
# COUNT 2 ITEMS AND RETURN THE ONE
# THAT SHOWS UP MORE
def more_frequent_item(lst, item1, item2):
    c1 = lst.count(item1)
    c2 = lst.count(item2)
    if c1 >= c2: return item1
    return item2

# Double Index
# double a value at a given position
def double_index(lst, index):
    if index >= len(lst):
        return lst  # return original lst if invalid index
    newLst = lst[:index]
    newLst.append(lst[index] * 2)
    newLst += lst[index + 1:]
    return newLst

# Middle Item
# FINDS THE MIDDLE ITEM FROM A LIST OF VALUES
def middle_element(lst):
    n = len(lst)
    if n % 2 != 0:
        return lst[n//2]
    else:
        ave = (lst[n//2] + lst[n//2-1])/2
        return ave