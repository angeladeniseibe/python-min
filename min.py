numbers = input("Enter numbers: ")
numbers_list = [float(num) for num in numbers.split(",")]
min_number = min(numbers_list)
print("The Minimum number is:", min_number)