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
        valor = float(input("Insira o Valor Do Depósito: "))
        
        if((valor) > 0):
            saldo += valor
            extrato += (f"R$ {valor:.2f}\n" )
        else:
            print("")
            print("Valor Inserido Invalido!")

        print("")
        print("Extrato: \n" + extrato)
        print(f"Seu Saldo É De: R${saldo:.2f}")
        
    elif(opcao == "2"):
        print("Saque")
        valor = float(input("Insira o Valor Para Saque: "))
        #print("SALDO DIA "+str(int(valor) + saque_dia))

        if(valor > saldo):
            print("")
            print("Operação Cancelada")
            print("Saldo Insuficiente!")
        elif(valor < 0):
            print("")
            print("Operação Cancelada")
            print("Valor Informado Inválido!")
        elif(valor > 500):
            print("")
            print("Operação Cancelada")
            print(f"Tentativa De Saque: {valor} -> Máximo Permitido: R$500.00!")
        elif(float(valor) + saque_dia > 1500):
            print("")
            print("Operação Cancelada")
            print(f"Valor Sacado Dia: {saque_dia} -> Máximo Permitido: R$1500.00!")
        elif(numero_saques >= LIMITE_SAQUES):
            print("")
            print("Operação Cancelada")
            print(f"Saques Realizado no Dia: {numero_saques} -> Máximo Permitido: {LIMITE_SAQUES}!")
        else:
        
        #if((valor) <= saldo and float(valor) > 0 and float(valor) <= 500 and ((float(valor) + saque_dia) <= 1500) and numero_saques < LIMITE_SAQUES):
            saldo -= valor
            extrato += (f"R$ -{valor:.2f}\n" )
            numero_saques += 1
            saque_dia += valor
            print("")
            print("Saques Disponiveis: "+str(LIMITE_SAQUES-numero_saques))
            print("Valor Sacado Dia: "+str(saque_dia))
        #else:
            #print("")
            #print("Valor Inserido Invalido!")
            #print("Saques Disponiveis: "+str(LIMITE_SAQUES-numero_saques))
            #print("Valor Sacado Dia: "+str(saque_dia))
            #print("Valor Máximo Por Saque: R$ 500.00")

        print("")
        print("Extrato: \n" + extrato)
        print(f"Seu Saldo É De: R${saldo:.2f}")

    elif(opcao == "3"):
        print("--------------------Extrato--------------------")
        print(extrato)
        print("*Sem Operações No Dia!*" if not extrato else extrato)
        print("")
        print(f"Seu Saldo É De: R${saldo:.2f}")
        print(" ----------------------------------------------")
         
    elif(opcao == "4"):
        print("Bye")
        break

    else:
        print("Seleção Inválida, Por Favor Tente Novamente")
        

