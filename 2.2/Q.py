a = float(input())
b = float(input())
c = float(input())
d = float(b * b - 4 * a * c)

if a == b == c == 0:
    print('Infinite solutions')
elif a == b == 0 and c != 0:
    print('No solution')
elif a == 0 and b != 0:
    x = float(-c / b)
    print(f"{x:.2f}")
elif d < 0:
    print('No solution')
elif d == 0:
    x = float((-b) / (2 * a))
    print(f"{x:.2f}")
else:
    x_1 = float(((-b) + (d ** 0.5)) / (2 * a))
    x_2 = float(((-b) - (d ** 0.5)) / (2 * a))
    min_x = min(x_1, x_2)
    max_x = max(x_1, x_2)
    print(f"{min_x:.2f} {max_x:.2f}")
