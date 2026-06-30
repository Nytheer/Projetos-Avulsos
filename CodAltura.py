# ------------------- ALTURAS -------------------
maior_altura = 0
menor_altura = 0

for i in range(1, 5):
    alt = float(input(f"Digite a altura da {i}ª pessoa: "))

    if i == 1:
        maior_altura = alt
        menor_altura = alt
    else:
        if alt > maior_altura:
            maior_altura = alt
        if alt < menor_altura:
            menor_altura = alt

print(f"Maior altura do grupo: {maior_altura}")
print(f"Menor altura do grupo: {menor_altura}")


# ------------------- NÚMEROS -------------------
maior_num = 0
menor_num = 0

for i in range(1, 11):
    num = int(input("Digite um número: "))

    if i == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num

print(f"Maior número: {maior_num}")
print(f"Menor número: {menor_num}")
