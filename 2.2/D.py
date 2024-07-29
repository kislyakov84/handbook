petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

winner1 = ""
winner2 = ""
winner3 = ""

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    winner1 = "Петя"
elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    winner1 = "Вася"
elif tolya_speed > petya_speed and tolya_speed > vasya_speed:
    winner1 = "Толя"

if petya_speed < vasya_speed and petya_speed < tolya_speed:
    winner3 = "Петя"
elif vasya_speed < petya_speed and vasya_speed < tolya_speed:
    winner3 = "Вася"
elif tolya_speed < petya_speed and tolya_speed < vasya_speed:
    winner3 = "Толя"

if petya_speed > vasya_speed and vasya_speed > tolya_speed:
    winner2 = "Вася"
elif tolya_speed > vasya_speed and vasya_speed > petya_speed:
    winner2 = "Вася"

elif vasya_speed > petya_speed and petya_speed > tolya_speed:
    winner2 = "Петя"
elif tolya_speed > petya_speed and petya_speed > vasya_speed:
    winner2 = "Петя"

elif vasya_speed > tolya_speed and tolya_speed > petya_speed:
    winner2 = "Толя"
elif petya_speed > tolya_speed and tolya_speed > vasya_speed:
    winner2 = "Толя"

print("1. " + winner1)
print("2. " + winner2)
print("3. " + winner3)
