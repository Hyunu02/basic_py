# tuples are similar to lists, but they are immutable
# usually used to datas which arent similar (e.g. name, age, etc)
# order MATTERS!

dog_info = ('Hyba', 7, 'French Doggo')
print(dog_info) # Output: ('Hyba', 7, 'French Doggo')
print(dog_info[0]) # Output: Hyba

# dog_info[0] = 'Eva'  --> it doesnt work

# unpacking a tuple
name, age, specie = dog_info
print(specie, age) # Output: French Doggo 7

one_element_tuple = (12) # it doesnt create tuple! (one element)
print(one_element_tuple) # Output: 12
one_element_tuple = (4,) 
print(one_element_tuple) # Output: (12,)