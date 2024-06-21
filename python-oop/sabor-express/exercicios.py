

# par ou ímpar ------------------------------------------------------------------------------------

# numero = int(input("Escolha um número: "))
# if numero % 2 == 0:
#     print("Este número é par")
# else:
#     print(f"O número {numero} é ímpar")

# classificar idade -------------------------------------------------------------------------------

# idade = int(input("Qual a sua idade? "))
# match idade:
#     case _ if idade <= 12:
#         print('Você é uma criança')
#     case _ if idade <= 18:
#         print('Você é um adolescente')
#     case _:
#         print('Você é um adulto')

# verificar senha ---------------------------------------------------------------------------------
from pwinput import pwinput

usuario = 'leticia123'
senha = '@literalbadge'

usuario_fornecido = input('Usuário: ')
senha_fornecida = pwinput(prompt = "Senha: ")

if usuario_fornecido != usuario:
    print('O usuário fornecido não existe no sistema.')
elif senha_fornecida != senha:
    print('Senha incorreta')
else:
    print('Acesso concedido')