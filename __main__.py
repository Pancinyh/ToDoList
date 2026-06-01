from pathlib import Path
from time import sleep
from funcoes import *
from os import system
import json
from rich import print
from datetime import date

# Classes -------------------------------------------------------------------------------------------------------------------------------------------------
class Tarefas:
    def __init__(self):
        self.lista = []

    def adicionar_tarefa(self, nome):
        dados = dict()
        dados['nome'] = nome
        dados['criacao'] = date.today()
        self.lista.append(dados)
    
    def to_dict(self):
        tarefas = self.lista.copy()
        for tarefa in tarefas:
            tarefa['criacao'] = tarefa['criacao'].strftime('%d/%m/%Y')
        return tarefas

cadastros = []
try:
    with open('cadastros.json', 'r') as arq:
        cadastros = json.load(arq)

except FileNotFoundError:
    with open('cadastros.json', 'w') as arq:
        json.dump([], arq)
print(cadastros)
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

email.replace('@', "_").replace(".", "_")
ARQUIVO = f'{email}.json'

# Carrega o arquivo para ser usado no código -------------------------------------------------------------------------------------------

tarefas = Tarefas()

try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        for tarefa in dados:
            dados['criacao'] = dados['criacao'].strptime(dados['criacao'], '%d/%m/%Y')
        tarefas.lista = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump([], arquivo)

# Programa principal ---------------------------------------------------------------------------------------------------------------------------------

print('| [bold blue]TO DO LIST[/] |'.center(50, '-'))

while True:
    escolha = menu('Adicionar tarefa', 'Remover tarefas', 'Ver lista de tarefas', 'Sair')
    if escolha == 1:
        tarefa = str(input('Tarefa que será adicionada: ').strip().title())
        tarefas.adicionar_tarefa(tarefa)
        print(f'[blue]Tarefa [bold yellow]{tarefa}[blue] foi adicionada![/]')
        salvar(ARQUIVO, tarefas)

    elif escolha == 2:
        if len(tarefas) > 0:
            print('[bold white]| TAREFAS |[/]'.center(50, '-'))
            for pos, tar in enumerate(tarefas):
                print(f'[yellow]{pos+1} [white]• [blue]{tarefas[pos]}[/]')
            indice = int(input('[bold blue]Qual o número da tarefa que deseja remover?[/]\nR: '))
            if tarefas[indice-1] not in tarefas:
                print(f'[red]A tarefa de número [yellow]{indice}[red] não existe.[/]')
            else:
                print(f'Tarefa [green]{tarefas[indice-1]}[/] foi removida!')
                tarefas.remove(tarefas[indice-1])
                salvar(ARQUIVO, tarefas)
        else:
            print('[red]Não há tarefas no momento.[/]')
            
    elif escolha == 3:
        print(f'[bold white]Lista de tarefas:[/]')
        if len(tarefas) == 0:
            print('[red]Nenhuma tarefa adicionada até o momento.[/]')
        else:
            qntd = 0
            for l in range(0, len(tarefas)):
                qntd += 1
                print(f'\033[1;33m{qntd}\033[m • {tarefas[l]}')
    elif escolha == 4:
        break
    sleep(2)
    system('cls')