petya = int(input())
vasya = int(input())
tolya = int(input())

first = "AAAA"
second = "BBBB"
third = "CCCC"

if petya > vasya > tolya or petya > tolya > vasya:
    first = "Петя"
elif vasya > petya > tolya or vasya > tolya > petya:
    first = "Вася"
elif tolya > vasya > petya or tolya > petya > vasya:
    first = "Толя"

if petya > vasya > tolya or tolya > vasya > petya:
    second = "Вася"
elif vasya > petya > tolya or tolya > petya > vasya:
    second = "Петя"
elif petya > tolya > vasya or vasya > tolya > petya:
    second = "Толя"

if petya > vasya > tolya or vasya > petya > tolya:
    third = "Толя"
elif petya > tolya > vasya or tolya > petya > vasya:
    third = "Вася"
elif tolya > vasya > petya or vasya > tolya > petya:
    third = "Петя"

print(" " * 10 + first + " " * 10)
print("  " + second + " " * 18)
print(" " * 18 + third + " " * 2)
print(" " * 3 + "II" + " " * 6 + "I " + " " * 5 + "III" + " " * 2)
