while True:
    opcao = int(input("Informe Um Número: "))
    if opcao == 10:
        break
    print(opcao)


for numero in range(100):
    if numero == 10:
        break
    print(numero, end="")

print()
for numero in range(12):
    if numero == 10:
        continue #Pula Para o Proximo Valor Do Laço
    print(numero)

print()
for numero in range(12):
    if numero % 2 == 0:
        continue
    print(numero)
