numbers = [3, 6, 1, 8, 2, 9, 5]
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
