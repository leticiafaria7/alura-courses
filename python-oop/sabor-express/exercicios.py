from unidecode import unidecode
import re

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
# from pwinput import pwinput

# usuario = 'leticia123'
# senha = '@literalbadge'

# usuario_fornecido = input('Usuário: ')
# senha_fornecida = pwinput(prompt = "Senha: ")

# if usuario_fornecido != usuario:
#     print('O usuário fornecido não existe no sistema.')
# elif senha_fornecida != senha:
#     print('Senha incorreta')
# else:
#     print('Acesso concedido')

# soma dos números ímpares de 1 a 10 --------------------------------------------------------------
# soma = 0
# for _ in range(1, 11):
#     if _ % 2 != 0:
#         soma = soma + _
    
# print(soma)

# números de 1 a 10 de forma decrescente ----------------------------------------------------------
# lista = range(10)
# for idx, _ in enumerate(lista):
#     print(len(lista) - idx)

# tabuada -----------------------------------------------------------------------------------------
# numero = int(input('Digite um número: '))
# print(f'\nTabuada do número {numero}:')
# for _ in range(10):
#     print(numero * (_ + 1))

# média dos valores da lista ----------------------------------------------------------------------
# def criar_lista_numeros():
#     numeros = input('Digite uma lista de números separados por vírgula: ')
#     lista = numeros.replace(' ', '').split(',')
#     lista = [int(numero) for numero in lista]
#     return lista

# while True:
#     try:
#         lista = criar_lista_numeros()
#         break
#     except:
#         print('Um dos números não é válido! Por favor, tente novamente.\n')

# print(f'A média dos números informados é {sum(lista) / len(lista)}')

# contar a frequência de cada palavra em uma frase ------------------------------------------------
def contar_freq_palavras(frase):
    lista = frase.split(' ')

    lista_palavras_tratadas = []
    for palavra in lista:
        palavra_tratada = re.sub('[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', palavra)
        palavra_tratada = palavra_tratada.lower()
        lista_palavras_tratadas.append(palavra_tratada)

    lista_palavras_unicas = []
    for palavra in lista_palavras_tratadas:
        if palavra not in lista_palavras_unicas:
            lista_palavras_unicas.append(palavra)

    dict_palavras = {}
    for palavra in lista_palavras_unicas:
        n_ocorrencias = lista_palavras_tratadas.count(palavra)
        dict_palavras[palavra] = n_ocorrencias

    print(dict_palavras)

frase = input('Escreva uma frase: ')

contar_freq_palavras(frase)