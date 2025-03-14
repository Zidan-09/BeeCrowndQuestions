def converter_valor(valor):
    print('NOTAS:')

    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor // nota
        valor -= quantidade * nota
        print(f'{int(quantidade)} nota(s) de R$ {nota},00')
    
    print('MOEDAS:')
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    for moeda in moedas:
        quantidade = valor // moeda
        valor -= quantidade * moeda
        print(f'{int(quantidade)} moeda(s) de R$ {moeda}')

converter_valor(float(input()))