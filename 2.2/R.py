a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c) ** 2 * 2
other = a ** 2 + b ** 2 + c ** 2

if maximum == other:
    print('100%')
elif maximum > other:
    print('велика')
else:
    print('крайне мала')
