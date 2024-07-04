menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] SAIR

==> """

saldo = 0
limite_operacao = 500
limite_diario = 500
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
        else:
            print("Valor Inserido Invalido!")

        print("")
        extrato += ("+" + str(valor) + "\n" )
        print("Extrato: \n" + extrato)
        print(f"Seu Saldo É De: R${saldo:.2f}")
        
    elif(opcao == "2"):
        print("Saque")

    elif(opcao == "3"):
        print("Extrato")
         
    elif(opcao == "4"):
        print("Bye")
        break

    else:
        print("Seleção Inválida, Por Favor Tente Novamente")
        

