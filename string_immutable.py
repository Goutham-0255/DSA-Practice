
#cannot change the value of a string using index value as shown below
var = 'Hello'
var[1] = 'o'
print(var[1])


# but can be done using slicing reconstructing th string or its called creating a new string
var = 'hello'
var = var[0] + 'o' + var[2:]
print(var)


# convert the string to list and then change the value of the list and then join the list to form a string
var = 'hello'
var = list(var)
var[1] = '0'
var = ''.join(var)
print(var)