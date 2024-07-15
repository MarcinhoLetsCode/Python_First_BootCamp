#OBJETO PRIMEIRA CLASSE
def somar(a, b):
    return a + b

def show_result(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

show_result(10, 10, somar)


#ESCOPO LOCAL E GLOBAL
salario = 2000

def salario_bonus1(bonus):
    #salario
    global salario
    salario += bonus
    return salario

def salario_bonus2(bonus, lista):
    #salario
    global salario
    #print(lista)
    #lista.append(2)
    lista2 = lista.copy()
    lista2.append(2)
    salario += bonus
    return salario, lista2

print(salario_bonus1(500))

lista=[1]
salario_com_bonus = salario_bonus2(500, lista)
print(salario_com_bonus)
print(lista)
