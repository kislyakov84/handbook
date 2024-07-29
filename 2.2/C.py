petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    print("Петя")
elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    print("Вася")
elif tolya_speed > petya_speed and tolya_speed > vasya_speed:
    print("Толя")
else:
    print("Никто")
    