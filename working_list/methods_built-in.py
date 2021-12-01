# syntax for methods
# list.method(input)

#syntax for built-in function
# builtinfunction(input)

# .count() count and return number of occurrences of element 
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes)

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
# range (x, y) generate numbers starting at 2
# range (x, y, z) set interval of z in each number
range_five_three = range(5, 15, 3) 
print(list(range_five_three)) # OUTPUT: [5, 8, 11, 14]

# len(my_list) get length of a list
range_list = range(2, 3000, 100)
range_list_length = len(range_list) # len dont need to convert range object
print(range_list_length)

# .sort() / sorted() sort a list (numerical and alphabetical)
# .sort(reverse = True) to descending order
# it modifies the list directly
# cant use when list contain more than one type (e.g. num and str)
elements = ["a", "b", "z", "d", "m"]
elements.sort()
print(elements) # ['a', 'b', 'd', 'm', 'z']
elements.sort(reverse=True)
print(elements) # ['z', 'm', 'd', 'b', 'a']

# sorted() --> comes before a list, generates a new list
# instead modifying it
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games) # ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print(games_sorted) # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']