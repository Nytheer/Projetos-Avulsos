def fibonacci(numb):
    if numb <= 0:
        return []
    elif numb == 1:
        return [0]

    nacci = [0, 1]

    while len(nacci) < numb:
        proximo = nacci[-1] + nacci[-2]
        nacci.append(proximo)

    return nacci

#print(fibonacci(add numero))
#exemplo
#print(fibonacci(10))
#SAIDA: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
