menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] SAIR

==> """

saldo = 1500
saque_dia = 0
limite_operacao = 500
limite_diario = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if(opcao == "1"):
        print("Depósito")
        valor = int(input("Insira o Valor Do Depósito: "))
        
        if(int(valor) > 0):
            saldo += valor
            extrato += ("+" + str(valor) + "\n" )
        else:
            print("")
            print("Valor Inserido Invalido!")

        print("")
        print("Extrato: \n" + extrato)
        print(f"Seu Saldo É De: R${saldo:.2f}")
        
    elif(opcao == "2"):
        print("Saque")
        valor = int(input("Insira o Valor Para Saque: "))
        #print("SALDO DIA "+str(int(valor) + saque_dia))

        if(int(valor) <= saldo and int(valor) > 0 and int(valor) <= 500 and ((int(valor) + saque_dia) <= 1500) and numero_saques < LIMITE_SAQUES):
            saldo -= valor
            extrato += ("-" + str(valor) + "\n" )
            numero_saques += 1
            saque_dia += valor
            print("")
            print("Saques Disponiveis: "+str(LIMITE_SAQUES-numero_saques))
            print("Valor Sacado Dia: "+str(saque_dia))
        else:
            print("")
            print("Valor Inserido Invalido!")
            print("Saques Disponiveis: "+str(LIMITE_SAQUES-numero_saques))
            print("Valor Sacado Dia: "+str(saque_dia))

        print("")
        print("Extrato: \n" + extrato)
        print(f"Seu Saldo É De: R${saldo:.2f}")

    elif(opcao == "3"):
        print("Extrato:")
        print(extrato)
        if(extrato == ""):
            print("*Sem Operações No Dia!*")
            print("")
        print(f"Seu Saldo É De: R${saldo:.2f}")
         
    elif(opcao == "4"):
        print("Bye")
        break

    else:
        print("Seleção Inválida, Por Favor Tente Novamente")
        

