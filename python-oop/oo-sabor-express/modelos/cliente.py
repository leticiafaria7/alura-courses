# class Pessoa:

#     def __init__(self, nome, idade, profissao):
#         self._nome = nome
#         self._idade = idade
#         self._profissao = profissao

#     def __str__(self):
#         return(f'{self.nome}, {self.nome} anos, {self.profissao}')

#     @property
#     def saudacao(self):
#         return f"Olá, sou {self.nome}! Atuo como {self._profissao}."
    
#     def aniversario(self):
#         self.idade +=1

# class ContaBancaria:

#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativa = False

#     def __str__(self):
#         return f'Titular da conta: {self._titular} | Saldo: {self._saldo}'
    
#     @classmethod
#     def ativar_conta(cls, conta):
#         conta._ativa = True
    
# titular_1 = ContaBancaria('Fulaninho', 'R$ 3.500,00')
# ContaBancaria.ativar_conta(titular_1)
# titular_2 = ContaBancaria('Ciclaninha', 'R$ 5.600,00')

# print(titular_1)


class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f"Título: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicacao} | Disponível: {self.emprestado}"
    
    def emprestar(self):
        self._disponivel = False
    
    @property
    def emprestado(self):
        return 'Disponível' if self._disponivel else 'Emprestado'
    
    @staticmethod
    def verificar_disponibilidade(ano_fornecido):
        livros_do_ano = []
        for livro in Livro.livros:
            if ano_fornecido == livro._ano_publicacao:
                livros_do_ano.append(livro._titulo)

        return livros_do_ano
