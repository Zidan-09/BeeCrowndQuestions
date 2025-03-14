valores = []
for _ in range(5):
    valores.append(float(input()))

pares = []
impares = []
positivos = []
negativos = []

for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

    if i > 0:
        positivos.append(i)
    elif i == 0:
        pass
    else:
        negativos.append(i)

print(f'{len(pares)} valor(es) par(es)\n{len(impares)} valor(es) impar(es)\n{len(positivos)} valor(es) positivo(s)\n{len(negativos)} valor(es) negativo(s)')