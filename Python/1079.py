for _ in range(int(input())):
    value_1, value_2, value_3 = map(float, input().split())
    print(f'{(value_1 * 2 + value_2 * 3 + value_3 * 5) / 10:.1f}')