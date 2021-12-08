my_name = "Andre"
first_initial = my_name[0]
print(first_initial) # OUTPUT: A

# SLICING A STRING
fruit = 'Mango'
print(fruit[:4]) # OUTPUT: MANG

# STRINGS ARE IMMUTABLE
first_name = "Bob"
# first_name[0] = "R" DOESNT WORK!
# cant change an individual character
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name) # OUTPUT: Rob