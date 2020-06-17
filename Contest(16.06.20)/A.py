import sys
string = str(input())
length = len(string)

for i in range(length//2):
    if string[i] != string[-1-i]:
        print ("NO")
        sys.exit()
      
print ("YES")
sys.exit()
