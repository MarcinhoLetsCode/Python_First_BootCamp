texto = "Hello World!" #input("Informe Um Texto: ")
VOGAIS = "AEIOU"
cont_vogais = 0
verifica_vogais = ""

#ITERAVEL
print()
print("Palavra Digitada: "+texto)
for letra in texto:
    #print(letra, end=" ")
    if letra.upper() in VOGAIS:
        if cont_vogais == 0:
            print("Vogais: ", end="")
        
        if not letra.upper() in verifica_vogais:
            print(letra, end=", ")
            verifica_vogais += letra.upper()

        cont_vogais += 1
else:
    print()
    print("FIM")

#RANGE
print()
for numero in range(0, 10):
    print(numero, end="")

print()
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()
for numero in range(10, -1, -1):
    print(numero, end=" ")
