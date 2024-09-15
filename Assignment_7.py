# user's name:
name = input(" Hey! What's your name:")
# user's favourit 3 numbers:
num1 = int(input("Tell me your first favourite number:"))
num2 = int(input("Tell me your second favourite number:"))
num3 = int(input("Tell me your third favourite number:"))
print(f"Hey, {name}! lets explore your favourite numbers")
# check if the numbers are even or odd:
for num in [num1, num2, num3]:
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
# display the numbers and their squares:
print(f"The number {num1} and its square: {num1**2}")
print(f"The number {num2} and its square: {num2**2}")
print(f"The number {num3} and its square: {num3**2}") 
# Calcuate the sum of the numbers
total_sum = num1 + num2 + num3
print(f"\nGreat! The sum of your favorite numbers is: {total_sum}")
# Check if the sum is a prime number or not:
num = int(input("Please, enter your number here:"))
if num ==1:
    print("Sorry, the sum of your numbers are not prime.")
if num > 1:
    for i in range (2,num):
        if num%i == 0:
            print ("Sorry, the sum of your numbers are not prime number.")
            break
    else:
        print("yay! your number is a prime number")