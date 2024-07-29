password = input()
result1 = int(password[-1]) + int(password[-2])
result2 = int(password[-2]) + int(password[-3])
print(str(max(result1, result2)) + str(min(result1, result2)))
