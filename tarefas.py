from pathlib import Path

ARQUIVO = Path("lista.txt")

# cria o arquivo se não existir
if not ARQUIVO.exists():
    ARQUIVO.write_text("", encoding="utf-8")
# carrega o arquivo para ser usado no código
with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        Tarefas = [linha.strip() for linha in arquivo if linha.strip()]
from time import sleep


print('\033[1;35m-_\033[m'* 10)
print('\033[1;36mTo Do List\033[m')
print('\033[1;35m-_\033[m'* 10)
escolha = -1
while escolha != 0:
    try:
        escolha = int(input('[1] Adicionar tarefa\n[2] Remover tarefa\n[3] Ver lista\n[0] Salvar\nR: '))
        if escolha < 0 or escolha > 4:
            print('Erro: o número deve estar entre \033[1;97m0\033[m e \033[1;97m3\033[m')
        else:
            if escolha == 1:
                tarefa = str(input('Tarefa que será adicionada: ').strip().title())
                if tarefa in Tarefas:
                    print(f'A tarefa \033[1;32m{tarefa}\033[m já existe.')
                else:
                    Tarefas.append(tarefa)
                    print(f'Tarefa \033[1;32m{tarefa}\033[m foi adicionada!')
            if escolha == 2:
                tarefa = str(input('Tarefa que deseja remover: ').strip().title())
                if tarefa not in Tarefas:
                    print(f'A tarefa \033[1;32m{tarefa}\033[m não existe.')
                else:
                    Tarefas.remove(tarefa)
                    print(f'Tarefa \033[1;32m{tarefa}\033[m foi removida!')
            if escolha == 3:
                print(f'\033[1;97mLista de tarefas:\033[m')
                if len(Tarefas) == 0:
                    print('Nenhuma tarefa adicionada até o momento.')
                else:
                    qntd = 0
                    for l in range(0, len(Tarefas)):
                        qntd += 1
                        print(f'{qntd} • {Tarefas[l]}')
            if escolha == 0:
                print('Salvando...')
    except ValueError:
        print('\033[1;31mErro:\033[m Tente novamente.')
    sleep(2)
# adiciona o que estiver dentro dele no documento 'lista.txt'
with open('lista.txt', 'w', encoding='utf-8') as arquivo:
# adiciona os elementos da lista um em cada linha
    for t in Tarefas:
        arquivo.write(f'{t}\n')
print('\033[1;32mLista salva.\033[m')
sleep(1)