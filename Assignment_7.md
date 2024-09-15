# Assignment No. 07 Markdown
## Step no.1:
![Python Code Image](https://res.cloudinary.com/practicaldev/image/fetch/s--5HkvaNUg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o1ltxvdi8spki6tx66zv.png)
### First of all we take input fron the user.
## Step no. 2:
### In this step we enter user's three favourite numbers.
## Step no. 3:
### We print a personalised message along with user's name.
## Step no. 4:
### We check if the numbers are even or odd by using if and else conditions.
## Step no. 5:
### We display numbers along with their squares.
```python
print(f"The number {num1} and its square: {num1**2}")
print(f"The number {num2} and its square: {num2**2}")
print(f"The number {num3} and its square: {num3**2}") 
```
## Step no. 6:
### We calculate the sum of favourite numbers.
## Step no. 7:
### This is the final step in which we check the sum of the numbers is prime ir not.
```python
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
```


