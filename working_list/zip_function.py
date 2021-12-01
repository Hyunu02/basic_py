# zip() allow us to quickly combine associated data-sets
# without multi-dimensional lists

# takes two or more lists as inputs and returns an
# object that contains a list of pairs from each input

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]

name_and_heights = zip(names, heights)
print(name_and_heights) 
# this zip object contais the location of variable in computer's memory

converted_list = list(name_and_heights)
print(converted_list) # inner lists converted into tuples