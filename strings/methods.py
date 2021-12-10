# STRING METHODS CAN ONLY * CREATE * NEW STRINGS
# DO NOT CHANGE ORIGINAL STRINGS

# .lower() --> returns string with all lowercase characters
# .upper() --> returns string with all uppercase characters
# .title() --> returns string with first letter of each word upper
hello = 'woRLd'
hello_fixed = hello.upper()
print(hello_fixed) # => WORLD

# .split() --> returns list with each word separated by spaces
line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words) # => ['The', 'sky', 'has', 'given', 'over']

# .split(x) --> .split separated by x
# WHEN SPLIT WITH CHARACTER THAT ALSO ENDS, END UP WITH EMPTY STRING IN THE END
# can also .split('\n') or .split('\t')
# USES \ to split a line
hey = \
"""Hello
Hi
Hey"""
print(hey.split('\n'))

# .join() --> essentially the opposite of .split()
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one) # => Black reapers with the sound of steel on stones

winter_trees_lines = ['All the complicated details', 'of the attiring and', 
'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.',
'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

# .strip() --> removes all whitespace characters from beginning till end
# whitespace in the middle is preserved
# can also .strip(x) that will strip that character
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

# string_name.replace(character_being_replaced, new_character)
phrase = "I like strawberry because strawberry is strawberry"
print(phrase.replace("strawberry", "blueberry"))

# .find() --> returns first index value where located
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)
print(god_wills_it_line_one.find('banana')) # returns -1 if not found

# .format() --> include in string
def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)

print(poem_title_card("500", "Deborah"))

fish = "salmon"
food = "takoyaki"
print("Do you prefer {food} or {fish}?".format(fish = fish, food = food))