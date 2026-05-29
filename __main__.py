import ast
from pathlib import Path
from time import sleep
from funcoes import *
from os import system

cadastros = []
try:
    with open('cadastros.txt', 'r') as cadastro:
        for linha in cadastro:
            cadastros.append(ast.literal_eval(linha.strip()))
except FileNotFoundError:
    cadastros = []

opcao = menu('Logar', 'Cadastrar')

if opcao == 1:
    c = 0
    logado = False
    while logado == False:
        c+=1
        email = str(input("Email: ")).strip()
        senha = str(input("Senha: ")).strip()
        for nome_user, email_user, senha_user in cadastros:
            if email == email_user and senha == senha_user:
                print('[green]LOGADO COM SUCESSO![/]')
                sleep(2)
                logado = True
                break
            else:
                print('[red]EMAIL OU SENHA INCORRETOS![/]')
                sleep(2)
            if c == 3:
                print('[red]LIMITE DE 3 TENTATIVAS ALCANÇADO[/]')
                sleep(2)
                exit()
    print(f'[bold yellow]Bem-vindo [bold blue]{nome_user}[/]')
    sleep(1)

# Cadastro -------------------------------------------------------------------------------------------

cadastrado = False
if opcao == 2:
        while True:
            nome = str(input('Nome completo: ')).strip().title()
            email = str(input('Email: ')).strip()
            senha = str(input('Senha: ')).strip()
            c = 0
            for nome_u, email_u, senha_u in cadastros:
                if email == email_u:
                    c += 1
            if c == 0:
                dados = (nome, email, senha)
                cadastros.append(dados)
                with open('cadastros.txt', 'w') as cadastro:
                    for linha in cadastros:
                        cadastro.write(str(linha) + '\n')
                print('[green]CADASTRADO COM SUCESSO![/]')
                sleep(2)
                break
            else:
                print('[red]EMAIL JÁ CADASTARDO![/]')
                sleep(2)
if opcao == 3:
    email = str(input('Email do cadastro: ')).strip()
    nova_senha = str(input('Nova senha: ')).strip()
email.replace('@', "_").replace(".", "_")
ARQUIVO = f'{email}.txt'
# Carrega o arquivo para ser usado no código -------------------------------------------------------------------------------------------
try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        Tarefas = [linha.strip() for linha in arquivo if linha.strip()]
except FileNotFoundError:
    with open(ARQUIVO, "x", encoding="utf-8") as arquivo:
        Tarefas = []
print('-' * 40)
print('| [bold blue]TO DO LIST[/] |'.center(50, '-'))
escolha = -1
while escolha != 0:
    escolha = menu('Adicionar tarefa', 'Remover tarefas', 'Ver lista de tarefas', 'Sair')
    if escolha == 1:
        tarefa = str(input('[bold blue]Tarefa que será adicionada:[/] ').strip().title())
        if tarefa in Tarefas:
            print(f'[red]A tarefa [yellow]{tarefa}[red] já existe.[/]')
        else:
            Tarefas.append(tarefa)
            print(f'[blue]Tarefa [bold yellow]{tarefa}[blue] foi adicionada![/]')
            salvar(ARQUIVO, Tarefas)
    if escolha == 2:
        if len(Tarefas) > 0:
            print('[bold white]| TAREFAS |[/]'.center(50, '-'))
            for pos, tar in enumerate(Tarefas):
                print(f'[yellow]{pos+1} [white]• [blue]{Tarefas[pos]}[/]')
            indice = int(input('[bold blue]Qual o número da tarefa que deseja remover?[/]\nR: '))
            if Tarefas[indice-1] not in Tarefas:
                print(f'[red]A tarefa de número [yellow]{indice}[red] não existe.[/]')
            else:
                print(f'Tarefa [green]{Tarefas[indice-1]}[/] foi removida!')
                Tarefas.remove(Tarefas[indice-1])
                salvar(ARQUIVO, Tarefas)
        else:
            print('[red]Não há tarefas no momento.[/]')
    if escolha == 3:
        print(f'[white]Lista de tarefas:[/]')
        if len(Tarefas) == 0:
            print('[red]Nenhuma tarefa adicionada até o momento.[/]')
        else:
            qntd = 0
            for l in range(0, len(Tarefas)):
                qntd += 1
                print(f'\033[1;33m{qntd}\033[m • {Tarefas[l]}')
    if escolha == 4:
        break
    sleep(2)
    system('cls')