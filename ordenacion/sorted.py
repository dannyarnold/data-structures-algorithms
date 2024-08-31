numbers = [3, 6, 1, 8, 2, 9, 99, 101, 5]
sorted_numbers = []
while numbers:
    minimum = numbers[0]  # Set the first element as the current minimum
    for x in numbers:
        # If any element is smaller than the current minimum, then update the minimum
        if x < minimum:
            minimum = x
        # Add minimum to the sorted_numbers list
    sorted_numbers.append(minimum)
    # remove minimum from the numbers list
    numbers.remove(minimum)
print(sorted_numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(numbers)
numbers.sort()
print(numbers)

numbersListTuple = [('Ram', '21'), ('Shyam', '10'),
                    ('Sita', '7'), ('Gita', '30')]
# print(type(numbersListTuple))
# print(type(numbersListTuple[0]))


def get_second_element_as_int(t):
    return int(t[1])


numbersListTuple.sort(key=get_second_element_as_int)
print(numbersListTuple)
