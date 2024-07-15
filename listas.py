frutas = ["Laranja", "Banana", "Abacate"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 420000, 2900, "São Paulo", True]
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
matriz[-1][-1]#c

lista = ["p","y","t","h","o","n",]
lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

for car in carro:
    print(car)
for indice, car in enumerate(carro):
    print(f"{indice}: {car}")

pares =[]
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero %2 == 0]
quadrado = [quadrado**2 for quadrado in numeros]
print(pares)
print(quadrado)

[].append()
[].clear()
[].copy()
[].count()
[].extend()
[].index()
[].pop()
[].remove()
[].reverse()
[].sort()-.sort(key=lambda x: len(x)) .sort(key=lambda x: len(x)m reverse=True)
[].len()
sorted(lista, key = lambda x: len(x))
