# for <temporary variable> in <collection>:
#   <action>

# <temporary variable> --> represent the value of the element in the
# collection the loop is currently on. Does not need to be defined beforehand
# best practice: make it as descriptive as possible

# <collection> --> to loop over

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
  print(game)
print("\n")

# using range() built-in function

for i in range(5): print(board_games[i])

phrase = "Iteration number: "

for temp in range(5):
  print(phrase + str(temp + 1))
