saldo = 1000
saque = 200
limite = 100
conta_especial = True
historico = []

print(saldo >= saque)
print(saque <= limite)

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)

print(not saldo >= saque)
print(saldo >= saque and not saque <= limite)

print(not historico)

print((saldo >= saque and saque <= limite) or
      (conta_especial and saldo >= saque))
