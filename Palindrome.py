
     
def palindrome(s):

    # remove spaces
    s = s.replace(" ", "")
        
    # reverse the str and check if it is same
    if s == s[::-1]:
        print("is palindrome")
    else:
        print("not palindrome")

s = "121"
palindrome(s)