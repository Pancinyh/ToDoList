from pathlib import Path
from time import sleep
from funcoes import *
from os import system
import json
from rich import print
from datetime import date
from models import *

cadastros = []
try:
    with open('cadastros.json', 'r') as arq:
        cadastros = json.load(arq)

except FileNotFoundError:
    with open('cadastros.json', 'w') as arq:
        json.dump([], arq)
opcao = menu('Logar', 'Cadastrar')

# Login ------------------------------------------------------------------------------------------------------------------------------------------------------
if opcao == 1:
    while True:
        Logado = False
        email = str(input('E-mail: ').strip())
        senha = str(input('Senha: ').strip())
        for cadastro in cadastros:
            if cadastro['email'] == email and cadastro['senha'] == senha:
                Logado = True
                break
        if Logado == True:
            break
        print('[bold red]Erro. E-mail ou Senha incorretos.[/]')

# Cadastro -------------------------------------------------------------------------------------------------------------------------

cadastrado = False
if opcao == 2:
    while True:
        nome = str(input('Nome completo: ').strip().title())
        email = str(input('E-mail: ').strip())
        senha = str(input('Senha: ').strip())
        c = 0
        for cadastro in cadastros:
            if cadastro['email'] == email or cadastro['senha'] == senha:
                c += 1
        if c == 0:
            dados = {
                'nome': nome,
                'email': email,
                'senha': senha
            }
            cadastros.append(dados)
            with open('cadastros.json', 'w') as arq:
                json.dump(cadastros, arq)
            break

email_formatado = email.replace('@', "_").replace(".", "_")
ARQUIVO = f'{email_formatado}.json'

# Carrega o arquivo para ser usado no código -------------------------------------------------------------------------------------------
tarefas = BancoTarefas()

try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        for tarefa in dados:
            criacao = date.strptime(tarefa['criacao'], '%d/%m/%Y')
            termino = date.strptime(tarefa['termino'], '%d/%m/%Y')
            tarefas.adicionar_tarefa(nome=tarefa['nome'], motivo=tarefa['motivo'],
                                     data_criacao=criacao, data_termino=termino)
            
except (FileNotFoundError, json.JSONDecodeError):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump([], arquivo)

# Programa principal ---------------------------------------------------------------------------------------------------------------------------------
print('| [bold blue]TO DO LIST[/] |'.center(50, '-'))

while True:
    escolha = menu('Adicionar tarefa', 'Remover tarefas', 'Ver lista de tarefas', 'Sair')
    if escolha == 1:
        tarefa = str(input('Tarefa que será adicionada: ').strip().capitalize())
        motivo = str(input('Descreva brevemente o motivo da tarefa: ').strip().capitalize())
        print(f'Prazo de término: ')
        dia = leia('Dia: ')
        mes = leia('Mês: ')
        ano = leia('Ano: ')
        data = date(day=dia, month=mes, year=ano)
        tarefas.adicionar_tarefa(tarefa, motivo, data_termino = data)
        print(f'[blue]Tarefa [bold yellow]{tarefa}[blue] foi adicionada![/]')
        salvar(ARQUIVO, tarefas)

    elif escolha == 2:
        if len(tarefas.lista) > 0:
            print('[bold white]| TAREFAS |[/]'.center(50, '-'))
            for tar in tarefas.lista:
                print(f'[yellow]- [white]• [blue]{tar.nome}[/]')
            tarefa = str(input('Qual a tarefa que deseja remover?\nR: ').strip().capitalize())
            if tarefas.buscar_tarefa(tarefa):
                print(f'Tarefa [green]{tarefa}[/] foi removida!')
                tarefas.lista.remove(tarefas.buscar_tarefa(tarefa))
                salvar(ARQUIVO, tarefas)
            else:
                 print(f'[red]A tarefa [yellow]{tarefa}[red] não existe.[/]')
        else:
            print('[red]Não há tarefas no momento.[/]')
            
    elif escolha == 3:
        print(f'[bold white]Lista de tarefas:[/]')
        if len(tarefas.lista) == 0:
            print('[red]Nenhuma tarefa adicionada até o momento.[/]')
        else:
            conteudo = ''
            for tarefa in tarefas.lista:
                conteudo += f'- {tarefa.nome} | Motivo: {tarefa.motivo} | Prazo de término: {tarefa.termino.strftime('%d/%m/%Y')}'
            painel = Panel.fit(
                conteudo,
                title='Tarefas'
            )
            print(painel)
    elif escolha == 4:
        break
    sleep(2)
    system('cls')