# there is different ways to print thing you want to show

# 1 method

print("Hey my name is %s." % "Andre")
print("I have %d pencils and %d papers!" %(2, 3))

# 2 method

print("I like {} color and {} color.".format("blue", "red"))
print("I like {1} and {0}.".format("mango", "watermelon"))

# 3 method

print("I have a doggo called {name} and she is {age}".format(name = "Hyba", age = 7))

# 4 method, v3.6 or higher

present = "a camera"
print(f"What did you really give me {present}?")

# when printing a number, you can print directly if use ',' but
# cannot when used '+'

print("I wish I had", 4, "pencils")
print("And I wish I had " + str(4) + " pens")