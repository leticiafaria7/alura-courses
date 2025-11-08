# Testes criam um roadmap das regras de negócio que a aplicação deve obedecer, além de incentivar a refatoração do códigopippip

from bytebank import Funcionario

# lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
# print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f"Teste = {funcionario_teste.idade()}")

teste_idade()

# no terminal: pip freeze > requirements.txt