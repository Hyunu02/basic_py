# METHODS are functions that are defined as part of a class

# first argument --> always the object that is calling the method
# convention --> self
# define methods similarly to functions
# self refers to object calling the function

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area

circle = Circle()
pizza_area = circle.area(12/2)      # JUST PASS 1 ONE ARGUMENT BECAUSE SELF IS IMPLICIT
teaching_table_area = circle.area(36/2) 
round_room_area = circle.area(11460/2)

print(pizza_area)