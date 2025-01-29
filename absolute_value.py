"""You have two numbers, and your challenge is to write a program that performs both 
addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results?
For example, consider two numbers 20 and 15. 
Addition of 2 values: 20 + 15 = 35.
Subtraction of 2 values: 20 - 15 = 5. 
For example, consider two numbers 20 and -150. 
Addition of 2 values: 20 + (-150) = -130 Absolute value of (-130) = 130.
Subtraction of 2 values: 20 - (-150) = 170."""


# finding absolute value without builin function 
def absolute_value(x):
    if x < 0:
        return -x

# normal addtion and subtratioin
def add_sub(num1,num2):
    addtion = num1 + num2

    #used the absolute value funtion for negative value to return it as positive 
    subtract = absolute_value(num1 - num2)

    return addtion,subtract
print(add_sub(50,80))



