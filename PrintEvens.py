x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x % 2 != 0:
    x += 1

for i in range(x, y, 2):
    print(i)