numbers = { 1, 2, 3, 4, 5, 7, 8, 9, 15, 17}
even_numbers = {2, 4, 6, 8, 10, 12, 14}
odd_numbers = {1, 3, 5, 7, 9}

all_numbers = even_numbers.union(odd_numbers)
all_numbers_version_2 = even_numbers | odd_numbers

print("Union: ", all_numbers)
print("Union version 2: ", all_numbers_version_2)

update_set = {1}
update_set.update(odd_numbers)
print("Update: ", update_set)

intersection_set = even_numbers.intersection(numbers)
print("Intersection: ", intersection_set)

some_set = {2, 3, 5, 6, 8}
some_set.intersection_update(even_numbers)
print("Intersection update: ", some_set)


difference_set = numbers.difference(even_numbers)
## or
# difference_set = numbers - even_numbers
print("Difference: ", difference_set)

another_set = {1, 2, 3, 4, 5, 7, 8, 9, 15}
another_set.difference_update(even_numbers)
print("Difference update: ", another_set)

sym_diff_set = even_numbers.symmetric_difference(numbers)
print("Symmetric difference: ", sym_diff_set)

sym_diff_update_set = {1, 2, 6, 4, 13, 7, 8, 9, 15}
sym_diff_update_set.symmetric_difference_update(even_numbers)
print("Symmetric difference update: ", sym_diff_update_set)


