zoo = ('lizard', 'fox', 'bird', 'zebra', 'lion', 'tiger', 'panda', 'peacock', 'bear', 'name')

print(zoo.index('lion'))

animal_to_find = "lion"
if animal_to_find in zoo:
  print(animal_to_find)

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(third_animal)

list_zoo = list(zoo)

print(list_zoo)

zoo_additions = ('shark', 'kangaroo', 'turtle')

list_zoo.extend(zoo_additions)

print(list_zoo)

back_to_tuple = tuple(list_zoo)

print(back_to_tuple)