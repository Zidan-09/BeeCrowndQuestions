total = []
repetion = int(input())

for _ in range(repetion):
    number = int(input())

    if number in range(10, 21):
        total.append(number)

print(f'{len(total)} in\n{repetion - len(total)} out')