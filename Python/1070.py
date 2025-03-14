number = int(input())

if number % 2 == 0:
    number += 1
    
for _ in range(6):
    print(number)
    number += 2
