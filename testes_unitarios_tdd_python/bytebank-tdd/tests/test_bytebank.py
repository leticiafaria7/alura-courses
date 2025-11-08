import sys, os

path_codigo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'codigo'))

if path_codigo not in sys.path:
    sys.path.append(path_codigo)

from bytebank import Funcionario

# método given-when-then
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_25(self):

        # given (contexto)
        entrada = '13/03/2000'
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # when (ação)
        resultado = funcionario_teste.idade()

        # then (desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # when

        assert resultado == esperado

# no terminal: pytest tests/test_bytebank.py