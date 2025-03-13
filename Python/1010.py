id_1, qty_1, price_1 = map(float, input().split())
id_2, qty_2, price_2 = map(float, input().split())
print(f'VALOR A PAGAR: R$ {qty_1 * price_1 + qty_2 * price_2:.2f}')