class Racional:
    def  __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def calculo(racional1, racional2, operacao):
        if operacao == '+':
            soman, somad = ((racional1.numerador * racional2.denominador) + (racional2.numerador * racional1.denominador)), (racional1.denominador * racional2.denominador)
            return Racional(soman, somad)
        elif operacao == '-':
            subtracaon, subtracaod = ((racional1.numerador * racional2.denominador) - (racional2.numerador * racional1.denominador)), (racional1.denominador * racional2.denominador)
            return Racional(subtracaon, subtracaod)
        elif operacao == '*':
            multiplicacaon, multiplicacaod = (racional1.numerador * racional2.numerador), (racional1.denominador * racional2.denominador)
            return Racional(multiplicacaon, multiplicacaod)
        elif operacao == '/':
            divisaon, divisaod = (racional1.numerador * racional2.denominador), (racional1.denominador * racional2.numerador)
            return Racional(divisaon, divisaod)
    
    def simplificar(racional):
        maior = max(racional.denominador, racional.numerador)
        for i in range(maior, 1, -1):
            if racional.denominador % i == 0 and racional.numerador % i == 0:
                return Racional(racional.numerador // i, racional.denominador // i)
        return racional

for i in range(int(input())):
    numerador1,barra, denominador1, operacao, numerador2, barra, denominador2 = input().split()

    racional1 = Racional(int(numerador1), int(denominador1))
    racional2 = Racional(int(numerador2), int(denominador2))

    resultado = Racional.calculo(racional1, racional2, operacao)

    print(f'{resultado.numerador}/{resultado.denominador} = {Racional.simplificar(resultado).numerador}/{Racional.simplificar(resultado).denominador}')