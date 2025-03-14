positivos = []
for _ in range(6):
    number = float(input())

    if number > 0:
        positivos.append(number)

print(f'{len(positivos)} valores positivos')