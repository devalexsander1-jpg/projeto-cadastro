#criar um projeto de cadastro

from cliente import Cliente
from repositorio import RepositorioClientes
from interface import Interface

if __name__ == "__main__":
	repo = RepositorioClientes()
	app = Interface(repo)
	app.iniciar()

