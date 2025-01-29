"""A washing machine works on the principle of Fuzzy System, the weight of clothes put 
inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. 
For low level water, the time estimate is 25 minutes, where approximately weight is 
between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is 
between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is 
above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 
0
minutes. 
If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all 
negative weights, the output is “INVALID INPUT”.
Sample Input-1: 2000, L
Sample Output-1: Time Estimated: 25 minutes
Input should be in the form of integer value. 
Output must have the following format: Time Estimated: NN Minutes"""


def weight(num):


    # check if the wieght is less than 0 or negative numbers
    if num < 0:
        return "Invalid input"
    
    # check the weight and estimate a time for that
    elif num < 2000:
        return "The estimate time is 25 minutes"
    elif 2000 <= num < 4001:
        return "The estimate time is 35 minutes"
    elif 4001 <= num < 7001:
        return "The estimate time is 45 minutes"
    
    # for overwieght which exceeds 7000 grams
    else:
        return "Overload"
    
print(weight(10000))
   