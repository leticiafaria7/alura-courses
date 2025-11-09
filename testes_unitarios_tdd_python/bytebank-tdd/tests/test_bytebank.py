import sys, os
import pytest
from pytest import mark

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

    # @mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100_000
        entrada_nome = 'Paulo Bragança'
        esperado = 90_000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100_000_000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100_000_000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__()

    #     assert resultado == esperado

# no terminal:
# pytest -v tests/test_bytebank.py
# pytest -v -k idade tests/test_bytebank.py (apenas testes de idade)
# pytest -v -m calcular_bonus tests/test_bytebank.py (apenas testes com a tag calcular_bonus)
# pytest --markers (todos os markers)
# pytest --cov=codigo tests/ (ver % do código que está coberto por testes)
# pytest --cov=codigo tests/ --cov-report term-missing (mostra a linha do código que não está coberta por testes)
# pytest --cov=codigo tests/ --cov-report html (gera um html com o relatório)
# pytest --junitxml report.xml

# test-driven development (TDD - desenvolvimento guiado por testes)