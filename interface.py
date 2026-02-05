import tkinter as tk

class Interface:
	def __init__(self, repositorio):
		self.repo = repositorio
		self.janela = tk.Tk()
		self.janela.title("Cadastro Clientes")
		self.janela.geometry("1200x900")
		self.criar_botoes()

	def criar_botoes(self):
		tk.Button(
			self.janela,
			text="Cadastrar Cliente",
			command=self.cadastrar
		).pack(pady=10)

		tk.Button(
			self.janela,
			text="Listar Clientes",
			command=self.listar
		).pack(pady=10)

		tk.Button(
			self.janela,
			text="sair",
			command=self.janela.quit
		).pack(pady=10)

	def cadastrar(self):
		print("Cadastrar clientes")

	def listar(self):
		print("listar clientes")

	def iniciar(self):
		self.janela.mainloop()
