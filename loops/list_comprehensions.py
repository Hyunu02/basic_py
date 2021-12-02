# create another list with 10 more points of each grade
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [num + 10 for num in grades]
print(scaled_grades)


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# create another list with conditional
can_ride_coaster = [height for height in heights if height > 161]
# to use if/else statement, conditionals have to be before for
cant_ride_coaster = [height if height < 160 else height - 100 for height in heights]
print(can_ride_coaster)
print(cant_ride_coaster)