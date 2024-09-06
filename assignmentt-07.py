# user's name
name = "Izza"
print(name)

# user's favorite numbers
numbers = [5, 7, 9]
print(numbers)

# Greet the user
print(f"\nSalam, {name}! Let's explore your favorite numbers.")

# Check the numbers are even or odd
even_odd_info = []
for num in numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even"))
    else:
        even_odd_info.append((num, "odd"))

# display the number is even or odd
for num, status in even_odd_info:
    print(f"Number {num} is {status}.")
    # Create tuples of each number and its square
for num in numbers:
    print(f"Number {num} squared is {num**2}.")
# Calculate the sum of the numbers
total_sum = sum(numbers)
# writ an encouraging message
print("Great! You've picked interesting numbers.")
# to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i != 0:
            continue
        else:
            return False
    return True
# Check if the sum is a prime number
if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
