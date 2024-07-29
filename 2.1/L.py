a = input()
a3 = int(a) % 10
a2 = int(a) // 10 % 10
a1 = int(a) // 100 % 10
b = input()
b3 = int(b) % 10
b2 = int(b) // 10 % 10
b1 = int(b) // 100 % 10
third = (a3 + b3) % 10
second = (a2 + b2) % 10
first = (a1 + b1) % 10
print(str(first) + str(second) + str(third))
