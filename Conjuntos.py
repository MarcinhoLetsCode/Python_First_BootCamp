num = set([1,2,3,1,4])
num2 = set([7,2,5,1,4])
fru = set("Abacaxi")
car = set(("Palio", "Gol", "Celta", "Palio"))

print(num)
print(fru)
print(car)

lin = {"Py", "Ja", "Py"}
print(lin)

numeros = list(num)
#print(num[0])
print(numeros[0])

for linguas in lin:
    print(linguas)

for indice, linguas in enumerate(lin):
    print(f"{indice}: {linguas}")

print(num.union(fru))
print(num.intersection(num2))
print(num.difference(num2))
print(num.symmetric_difference(num2))
print(num.issubset(num2))
print(num.issuperset(num2))
print(num.isdisjoint(num2))

#print(num.add(10))
num.add(10)
print(num)
num.add(1)
print(num)

number = num.copy()
num.clear()
print(num)
print(number)

number.discard(10)
print(number)

number.pop()
print(number)

number.remove(2)
print(number)

print(len(number))
print(1 in number)


