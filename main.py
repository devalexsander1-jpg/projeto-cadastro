#criar um projeto de cadastro

from cliente import Cliente
from repositorio import RepositorioClientes

repo = RepositorioClientes()

while True :
	name = input("qual o nome do cliente: se quiser sair digite (sair) ")
	
	if name.lower() == "sair":
		break

	cliente = Cliente(name)
	repo.adicionar(cliente)

print("\nClientes cadastrados: ")
for c in repo.listar():
	print(c)
