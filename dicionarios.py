pessoa = {"nome": "Marcinho", "idade": 31}
print (pessoa)
pessoa = dict(nome= "Marcinho", idade= 31)
print (pessoa)
pessoa["telefone"] = "1234-5678"
print (pessoa)

dados = {"nome": "Marcinho", "idade": 31, "telefone": "1234-5678"}
print(dados["nome"])
dados["nome"] = "Darlan"
print(dados["nome"])

contatos = {
    "marcio@marcio.com": {"nome": "Marcinho", "idade": 31, "telefone": "1234-5678"},
    "darlan@darlan.com": {"nome": "Darlan", "idade": 31, "telefone": "876-54321", "extra": {"hello": "world"}},
}

print(contatos["marcio@marcio.com"])
print(contatos["marcio@marcio.com"]["idade"])
print(contatos["darlan@darlan.com"]["extra"]["hello"])

#for chave in contatos:
    #print(chave)
    #print(contatos[chave])
    #print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
