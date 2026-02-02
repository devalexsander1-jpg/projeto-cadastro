class RepositorioClientes:
	def __init__(self):
		self.clientes = []

	def adicionar(self, cliente):
		self.clientes.append(cliente)

	def listar(self):
		return self.clientes


