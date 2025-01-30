def isPalindrome(s):


    s = s.lower()


    nonalnum_char = ""


    for char in s:
        if char.isalnum():
            nonalnum_char += char
    return nonalnum_char == nonalnum_char[::-1]

print(isPalindrome("121"))