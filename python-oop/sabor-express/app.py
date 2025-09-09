import os

restaurantes = [{'nome':'Ninita', 'categoria':'Brasileira', 'ativo':False},
                {'nome':'Topo do Mundo', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Est Est Est', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls') # limpa o terminal
    print(f'{subtitulo}')
    print('-' * (len(subtitulo) + 2) + '\n')

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados:')
    
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    print('-' * 70)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else "Desativado"
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar o estado de um restaurante')

    listar_restaurantes = []

    for restaurante in restaurantes:
        listar_restaurantes.append(restaurante['nome'])

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    if nome_restaurante not in listar_restaurantes:
        print('Este restaurante não está cadastrado!')
    else:
        for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                restaurante['ativo'] = not restaurante['ativo']
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} desativado com sucesso!'
                print(mensagem)

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()