def count_chars(string):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0
    for i in range(len(string)):  
        ch = string[i]  
        if ch.isalpha():  
            if ch in vowels:  
                v = v + 1  
            else:
                c += 1  
    return v, c

s = "Hey there, How are you?"
vowel_count, cons_count = count_chars(s)
print("Vowels: ", vowel_count)
print("Consonants: ", cons_count)
