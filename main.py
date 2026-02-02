#criar um projeto de cadastro

lista = []

i = 0

while True :
	name = input("qual o nome do cliente: se quiser sair digite (sair) ")
	lista.append(name)
	if name == "sair":
		break

print(lista)
