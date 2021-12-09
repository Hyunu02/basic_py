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
