a = int(input())
b = 0

while a != 0:
    if a % 6 == 0 and a % 10 == 4:
        b += a 
    a = int(input())

print(b)
