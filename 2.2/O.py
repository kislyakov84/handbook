num1 = int(input())
num2 = int(input())

a = num1 // 10
b = num1 % 10
c = num2 // 10
d = num2 % 10

summa = a + b + c + d
minimum = min(a, b, c, d)
maximum = max(a, b, c, d)
middle = (summa - minimum - maximum) % 10

print(maximum * 100 + middle * 10 + minimum)
