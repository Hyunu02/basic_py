# 1) Positional arguments: depend on their positions in function call
# 2) Keyword arguments: refer explicitly to what each argument is assigned when call function
#  calculate_taxi_price(rate=0.5, discount = 10, miles_to_travel = 100)
# 3) Default arguments: can set default argument
#  def calculate_taxi_price(miles_to_travel, rate, discount = 10)

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

# Keyword argument
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
# third argument as default in function
trip_planner("Brooklyn", "Queens")

# scope --> name where variable can be accessed

# multiple returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)