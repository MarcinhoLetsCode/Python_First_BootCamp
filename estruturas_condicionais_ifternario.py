saldo = 1000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} Ao Realizar o Saque!")
