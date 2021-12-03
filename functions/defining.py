# 'def' keyword indicates the beginning of a function
# AKA function header

# def function_name():
#   functions tasks go here        (INDENTED!)

print("Checking the weather for you!")

def weather_check():
    print("Looks great outside! Enjoy your trip.")
    print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

# PARAMETERS AND ARGUMENTS
# def my_function(parameter):
# parameter: defined in the parenthesis of the function
# argument: data passed in when function called

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  # Woohoo coupon of 10!
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)