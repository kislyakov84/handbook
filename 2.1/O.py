hours = int(input())
minutes = int(input())
lag = int(input())

minutes = minutes + lag
hours = (hours + minutes // 60) % 24
minutes = minutes % 60

print(f'{hours:02d}:{minutes:02d}')
