# syntax for methods
# list.method(input)

#syntax for built-in function
# builtinfunction(input)

# .count() count number of occurrences of element 
# .insert(index, value input) insert element in specific index
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0, "Pineapple")
print(front_display_list) # OUTPUT: ['Pineapple', 'Mango', 'Filet Mignon', 'Chocolate Milk']

# .pop() remove and return element from specific index or from the end
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
removed = data_science_topics.pop() + " / "
removed += data_science_topics.pop(-2)
print(data_science_topics)
print(removed) # OUTPUT: Python 3 / Algorithms

# range() built-in to create consecutive sequence of int, which is range object
number_list = range(9)
print(number_list) # OUTPUT: range(0, 9)
print(list(number_list)) # list() takes single input for object

# len() get length of a list
# .sort() / sorted() sort a list