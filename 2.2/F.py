year = int(input())
if year % 4 or not year % 100 and year % 400:
    print('NO')
else:
    print('YES')
    