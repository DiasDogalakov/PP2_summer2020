coordinates = input().split()
x1 = int(coordinates[0])
y1 = int(coordinates[1])
x2 = int(coordinates[2])
y2 = int(coordinates[3])
z1 = int(coordinates[4])
z2 = int(coordinates[5])

if(z1 >= x1 and z1 <= x2 and z2 >= y2 and z2 <= y1):
    print("yes")
else:
    print("no")
