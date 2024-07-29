number = input()
minimum = min(number[0], number[1], number[2])
maximum = max(number[0], number[1], number[2])
if int(minimum) + int(maximum) == int(number[0]) * 2:
    print('YES')
elif int(minimum) + int(maximum) == int(number[1]) * 2:
    print('YES')
elif int(minimum) + int(maximum) == int(number[2]) * 2:
    print('YES')
else:
    print('NO')
    