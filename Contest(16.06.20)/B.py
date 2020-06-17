string_ = input()
string = list()
for i in string_:
    string.append(i)
for i in range(len(string) - 1):
    for j in range(len(string) - 1):
        if (ord(string[j]) > ord(string[j + 1])):
            temp = string[j]
            string[j] = string[j + 1]
            string[j + 1] = temp

print(*string, sep = "")
