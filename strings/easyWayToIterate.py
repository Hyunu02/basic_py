# TO INCLUDE CHARACTERS THAT ALREADY
# HAVE A SPECIAL MEANING IN PYTHON
# THERE IS BACKSLASH '\'

# EASY CHECKING USING 'in'
# 'in' CHECKS IF ONE STRING IS PART OF ANOTHER

print("e" in "blueberry") # => True
print("blue" in "blueberry") # => True
print("blue" in "strawberry") # => False

def common_letters(string_one, string_two):
  newLst = []
  for letter in string_one:
    if (letter in string_two) and not (letter in newLst):
      newLst.append(letter)
  return newLst

print(common_letters("hello", "world")) # => ['l', 'o']