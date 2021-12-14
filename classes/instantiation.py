# PEP 8 Style Guide for Python Code recommends
# capitalizing the names of classes (easy to identify)

# Class doesn't accomplish antthing simpley be begind defined. 
# A class must be instantiated.
# Must create an instance of the class, in order to breathe life

class Facade:
    pass

# Object created by adding parentheses to
# the name of the class
# class instance is also called an object
# Instantiating a class looks like calling a function
# it takes a class and turns it into an object
facade_1 = Facade()

# __main__ means "this current file that we're running"

print(type(facade_1)) # <class '__main__.Facade'>