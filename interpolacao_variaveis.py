#OLD STYLE
nome = "Márcinho"
idade = 31
peso = 80.80
profissao = "FullStack"
linguagem = "All"

print(round(peso, 2))
print("Hello, i'm %s, i'm %d years old, i weight %f" %(nome, idade, peso))


#METODO FORMAT
nome = "Márcinho"
idade = 31
peso = 80.79
profissao = "FullStack"
linguagem = "All"

print("Hello, i'm {0}, i'm {1} years old, i weight {2}".format(nome, idade, round(peso, 2)))
print("Hello, i'm {nome}, i'm {idade} years old, i weight {peso}".format(nome=nome, idade=idade, peso = round(peso, 2)))
#print("Hello, i'm {nome}, i'm {idade} years old, i weight {peso}".format(**pessoa))


#f-string
nome = "Márcinho"
idade = 31
peso = 80.7910
profissao = "FullStack"
linguagem = "All"

print(f"Hello, i'm {nome}, i'm {idade} years old, i weight {peso:20.5f}")


