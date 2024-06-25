from modelos.cliente import Livro


livro_1 = Livro('Memórias póstumas de Brás Cubas', 'Machado de Assis', 1881)
livro_1.emprestar()
livro_2 = Livro('Storytelling with data', 'Cole Knaflic', 2015)

Livro.livros = [livro_1, livro_2]

# print(livro_1)
# print(livro_2)

print(Livro.verificar_disponibilidade(1881))

livro_2.emprestar()

# print(livro_2.emprestado)