import ast
from pathlib import Path
from time import sleep

cadastros = []
try:
    with open('cadastros.txt', 'r') as cadastro:
        for linha in cadastro:
            cadastros.append(ast.literal_eval(linha.strip()))
except FileNotFoundError:
    cadastros = []
# Login
opcao = int(input('[1] Logar\n[2] Cadastrar\nR: '))
if opcao == 1:
    c = 0
    logado = False
    while logado == False:
        c+=1
        email = str(input("Email: ")).strip()
        senha = str(input("Senha: ")).strip()
        for nome_user, email_user, senha_user in cadastros:
            if email == email_user and senha == senha_user:
                print('\033[1;32mLOGADO COM SUCESSO!\033[m')
                sleep(2)
                logado = True
                break
            else:
                print('\033[1;31mEMAIL OU SENHA INCORRETOS!\033[m')
                sleep(2)
            if c == 3:
                print('LIMITE DE 3 TENTATIVAS ALCANÇADO!')
                sleep(2)
                exit()
# Cadastro
cadastrado = False
if opcao == 2:
        while True:
            while True:
                nome = str(input('Nome completo: ')).strip().title()
                if len(nome.split()) > 2:
                    break
                print('\033[1;37mDeve conter seu nome completo.\033[m')
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
                print('\033[1;32mCADASTRADO COM SUCESSO!\033[m')
                sleep(2)
                break
            else:
                print('\033[1;31mEMAIL JÁ CADASTARDO!\033[m')
                sleep(2)
if opcao == 3:
    email = str(input('Email do cadastro: ')).strip()
    nova_senha = str(input('Nova senha: ')).strip()
    #for pos, linha in enumerate(cadastros):
      #  if email in cadastros[linha]
#Formatação email
email.replace('@', "_").replace(".", "_")
ARQUIVO = f'{email}.txt'
# carrega o arquivo para ser usado no código
try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        Tarefas = [linha.strip() for linha in arquivo if linha.strip()]
except FileNotFoundError:
    with open(ARQUIVO, "x", encoding="utf-8") as arquivo:
        Tarefas = []
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
# adiciona o que estiver dentro dele no documento.
with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
# adiciona os elementos da lista um em cada linha
    for t in Tarefas:
        arquivo.write(f'{t}\n')
print('\033[1;32mLista salva.\033[m')
sleep(1)
