from rich import print
from rich.panel import Panel
import json

def leia(msg, tipo=int):
    while True:
        try:
            opcao = tipo(input(msg))
        except ValueError, TypeError:
            print('[red]Erro. Tente novamente.[/]')
        else:
            return opcao

def menu(*opcoes):
    conteudo = ''
    for i, op in enumerate(opcoes):
        conteudo += f'[blue]{i+1}[/] - [bold white]{op}[/]\n'
    altura_panel =0
    altura_panel = altura_panel + (2*len(opcoes))
    tabela = Panel(
        conteudo,
        title='[bold blue]OPÇÕES[/]',
        width=30,
        height=altura_panel
    )
    print(tabela)
    while True:
        opcao = leia('Sua Opção: ')
        if len(opcoes)>= opcao > 0:
            return opcao
        print(f'[red]Erro. O número deve ser entre 1 e {len(opcoes)}.[/]')

def salvar(arq, lista_tarefas):
    with open(arq, 'w', encoding='utf-8') as arquivo:
        for t in lista_tarefas:
            arquivo.write(f'{t}\n')