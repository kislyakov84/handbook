data = input()
palindrome = data[-1] + data[-2] + data[-3] + data[-4]
if data == palindrome:
    print("YES")
else:
    print("NO")
    