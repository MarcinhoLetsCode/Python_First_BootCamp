if(True):
    print(True)
else:
    print(False)

saldo = 1000
saque = float(input("Informe o Valor Do Saque: "))

#if
print()
print("if")
if (saldo >= saque):
    print("Saque Realizado Com Sucesso!")  
if (saldo < saque):
    print("Saldo Insuficiente")

#if-else
print()
print("if-else")
if (saldo >= saque):
    print("Saque Realizado Com Sucesso!")  
else:
    print("Saldo Insuficiente")

#elif
print()
print("elif")
if (saldo >= saque):
    print("Saque Realizado Com Sucesso!")  
elif (saldo < saque):
    print("Saldo Insuficiente")

print()
opcao = int(input("Informe Opção:\n[1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a Quantia Para o Saque: "))
    print(valor)
elif opcao == 2:
    print("Exibindo o Extrato...")
else:
    import sys
    sys.exit("Opção Inválida")


