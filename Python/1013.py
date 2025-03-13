a, b, c = map(int, input().split())
print(f'{(((a + b + abs(a - b)) // 2) + c + abs(((a + b + abs(a - b)) // 2) - c)) // 2} eh o maior')