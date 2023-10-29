def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
        result = sum(filtered_numbers)
    else:
        result = sum(numbers)
    return result

input_str = input("Enter a list of numbers separated by spaces: ")

number_strings = input_str.split()

try:
    numbers = [int(num) for num in number_strings]
except ValueError:
    numbers = [float(num) for num in number_strings]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ")
exclude_negative = exclude_negative_input.lower() == "yes"

result = sum_of_elements(numbers, exclude_negative)


if exclude_negative:
    print("Sum of non-negative numbers:", result)
else:
    print("Sum of all numbers:", result)