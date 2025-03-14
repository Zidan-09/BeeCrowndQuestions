pares = []
for _ in range(5):
    number = float(input())

    if number % 2 == 0:
        pares.append(number)

print(f'{len(pares)} valores pares')