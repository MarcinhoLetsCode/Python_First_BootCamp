def show_message():
    print("Hello World")
def show_message2(name):
    print(f"Welcome {name}")
def show_message3(name="Unknown"):
    print(f"Welcome {name}")
    
show_message()
show_message2(name="Marcinho")
show_message3()
show_message3(name="Marcinho")


def calcular_total(numeros):
    return sum(numeros)

def return_antecessor_e_sucessor(numero):
    antecessor = numero + 1
    sucessor = numero - 1

    return antecessor, sucessor

total = calcular_total([10,20,30])
print(total)
print(return_antecessor_e_sucessor(2))

def func_3():
    print("Hello World")

print(func_3())

def constr_car(marca, modelo, placa, ano):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{placa}/{ano}")

constr_car("Fiat", "Palio", "abc-1234", 2000)
constr_car(marca="Fiat", modelo="Palio", placa="abc-1234", ano=2000)
constr_car(**{"marca": "Fiat", "modelo": "Palio", "placa": "abc-1234", "ano": 2000})

print("")
def show_poem(data_extenso, *args, **kwargs):
    texto= "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

show_poem(
    "Sexta-Feira, 26 De Agosto De 2022",
    "Zen Python",
    "Beautiful Than Ugly.",
    autor="Tim Petters",
    ano = 1999)
