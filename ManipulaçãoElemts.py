# Escreva um programa que recebe 4 valores e armazene em uma lista,
# remova o primeiro e o último, mostre o tamanho da lista e diga se ela está vazia ou não.

c = []

print("Insira 4 valores:")
for i in range(4):
    v = input(f"Valor {i+1}: ")
    c.append(v)

# Remove primeiro e último elemento
if len(c) >= 2:
    c.pop(0)
    c.pop()

# Mostra a lista resultante
print(f"Lista: {c}")

# Mostra o tamanho
print(f"Tamanho da lista: {len(c)}")

# Verifica se está vazia
if len(c) == 0:
    print("A lista está vazia")
else:
    print("A lista >>NÃO<< está vazia")
