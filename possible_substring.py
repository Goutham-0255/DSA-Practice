string = "sak"

# inner loop through first and outer loop do it to print the substring
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])
