for _ in range(int(input())):
    number_1, number_2 = map(int, input().split())

    if number_1 > number_2:
        number_1, number_2 = number_2, number_1
    
    print(sum(i for i in range(number_1 + 1, number_2) if i % 2 != 0))