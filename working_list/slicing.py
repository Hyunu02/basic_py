# my_list[start:end]
# start --> first element to include
# end --> one more than the last index to include

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
middle = suitcase[2:4]
print(beginning) # ['shirt', 'shirt']
print(middle) # ['pants', 'pants']

# my_list[:x] --> select first x elements
# my_list[y:] --> select y until last element

last_two_elements = suitcase[-2:]
slice_off_last_three = suitcase[:-3]
print(last_two_elements) # ['pajamas', 'books']
print(slice_off_last_three) # ['shirt', 'shirt', 'pants']
