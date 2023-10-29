input_str = input("Enter a list of numbers separated by spaces: ")
numbers = input_str.split()
try:
    numbers = [int(num) for num in numbers]
except ValueError:
    numbers = [float(num) for num in numbers]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)