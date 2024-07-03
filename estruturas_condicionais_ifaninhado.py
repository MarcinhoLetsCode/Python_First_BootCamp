conta_normal = False #True
conta_universitaria = False #
conta_especial = True
cheque_especial = 500
saldo = 5000

def restante(saldo, saque, cheque_especial):
    if saldo >= saque:
        saldo -= saque
        #print(saldo)
        return saldo
    else:
        cheque_especial += saldo
        cheque_especial -= saque
        return cheque_especial

saque = int(input("Digite o Valor do Saque: "))
    
if conta_normal:
    if saldo >= saque:
        print("Saque Realziado Com Sucesso!")
        saldo = restante(saldo, saque, cheque_especial)
    elif saque <= (saldo + cheque_especial):
        print("Saque Realizado Com Uso Do Cheque Especial!")
        cheque_especial = restante(saldo, saque, cheque_especial)
        saldo = 0
    else:
        print("Saldo Insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado Com Sucesso!")
        restante(saldo)
    else:
        print("Saldo Insuficiente!")
elif conta_especial:
    print("Conta Especial Selecionada")
else:
    print("Tipo De Conta Desconhecido")

print ("Saldo Restante: R$" + str(saldo))
print ("cheque_especial: R$" + str(cheque_especial))
