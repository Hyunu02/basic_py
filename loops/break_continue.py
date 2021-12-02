dog_breeds_available_for_adoption = ["dalmatian", "french_bulldog", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "french_bulldog"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# THIS IS A BAR WHERE ONLY 21+ CAN DRINK SODA!
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)