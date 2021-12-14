# there are "magic" methods that have special behavior
# 'dunder methods', they have two underscores on either side

# __init__() method --> initialize a newly created object
# called every time the class in instantiated

# Methods that are used to prepare an object being
# instantiated are called constructors

# in the instantiation we can pass parameters, it will
# be received by the __init__() method

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("New circle with diameter:", diameter)

teaching_table = Circle(36)