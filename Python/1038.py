valores = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

id, qty = map(int, input().split())

print(f'Total: R$ {valores[id] * qty:.2f}')