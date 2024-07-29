num = int(input())

first = num // 100
second = num // 10 % 10
third = num % 10

if first > second:
    first, second = second, first
if first > third:
    first, third = third, first
if second > third:
    second, third = third, second


minimal = first * 10 + second

if minimal < 10:
    minimal = second * 10 + 0
if minimal < 10:
    minimal = third * 10 + 0

maximal = third * 10 + second

print(minimal, maximal)