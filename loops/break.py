dog_breeds_available_for_adoption = ["dalmatian", "french_bulldog", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "french_bulldog"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break