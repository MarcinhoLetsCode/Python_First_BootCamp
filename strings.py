#MAIUSCULO, MINUSCULO E TITULO
curso = "pYtHon"
print(curso.upper())
print(curso.lower())
print(curso.title())
print()

#ELIMINAR ESPACOS EM BRANCO
curso = "    pYtHon "
print("." + curso.strip() + ".") #REMOVE DIREITA + ESQUERDA
print("." + curso.lstrip() + ".") #REMOVE ESQUERDA
print("." + curso.rstrip() + ".") #REMOVE DIREITA
print()

#JUNCOES E CENTRALIZACAO
curso = "Python"
x = 0
print(curso.center(10, "#"))
print(curso.ljust(10, "#"))
print(curso.rjust(10, "#"))
print(".".join(curso))
print(str(len(curso)).join(curso.center(9, "#")))
