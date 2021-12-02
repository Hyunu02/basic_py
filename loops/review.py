single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for i in single_digits:
  print(i)
  squares.append(i ** 2)
print(squares)

# list comprehension
cubes = [number ** 3 for number in single_digits]
print(cubes)