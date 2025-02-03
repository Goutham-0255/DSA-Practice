"""1.Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read from the console and consists of two integers: n and l within the range [1 … 9], each on a single line.

Output Data
Print on the console all "stupid" passwords in alphabetical order, separated by space"""


def S_password(n,l):

    S_Password = []


    # loop through 1 - last digit
    for digit1 in range(1,n+1):
        for digit2 in range(1, n+1):


            # changing them to ord because python range doesnt include alphabets
            for char1 in range(ord('a'), ord('a')+l):
                for char2 in range(ord('a'), ord('a')+l):


                    for digit3 in range(1, n+1):

                        # checks if the digit 3 is greater than 1 and 2 
                        if digit3 > digit1 and digit3 > digit2:

                            password = str(digit1) + str(digit2) + chr(char1) + chr(char2) + str(digit3)

                            S_Password.append(password)
    return S_Password

print(S_password(3,2))