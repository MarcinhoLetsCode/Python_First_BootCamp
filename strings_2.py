nome = "Márcinho"
idade = 31
peso = 80.80
profissao = "FullStack"
linguagem = "All"

dados = {"nome": "Marcinho", "idade": "31"}

print("Nome: %s Idade: %d" %(nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {name} Idade: {age} Nome: {name}{name}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
