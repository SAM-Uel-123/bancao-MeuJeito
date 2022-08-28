import os
import csv
from commandline_interface import *
from validacoes import *
import conta

#======================= #
#     -   Variaveis   -   
#======================= #
linhas = lambda msg: cli.detalhes.linhas(msg)
clear = lambda: os.system('clear')
cliOpcoes = None
conta_atual = None
limpar = True





while True:
    if limpar: 
        clear()

    linhas('Bancão Maneirão')

    print(''' 
 1 - Criar conta
 2 - Entrar em sua conta
 3 - Encerrar conta

 0 - Sair
''')
    opcao = validar_entradas.inputInts(' Opção: ')

    if opcao == 0:
        linhas(' Encerrado, volte sempre')
        break

    if opcao == 1:
        while True:
            conta_atual = conta.ContaBanco()
            titular_da_conta = input('Seu nome: ')
            if titular_duplicado(titular_da_conta):
                print(' esse usuario já existe, tente outro')
                continue

            linhas('Tipos de conta')
            print(' cc: Conta Corente,  cp: Conta Poupança.')
            tipo_da_conta = input('Opção: ')
            senha = ''
            while not senha:
                tmp_senha = input(' Senha ')
                if not tmp_senha:
                    print(' Preencha o espaço da senha. ')
                    continue

                confirmar = ''
                while not senha:
                    confirmar = input(' Deseja usar essa senha? [S/N]: ')
                    if confirmar == 's':
                        senha = tmp_senha
                        break

                    elif confirmar == 'n':
                        break
                    
                    else:
                        print('Opção invalida, tente somente (S) para sim e (N) para não.')
            break


        conta_atual.abrir_conta(titular_da_conta, tipo_da_conta)
        if conta_atual.status_da_conta:
            print(' Parabens! sua conta foi criada com sucesso.')
            conta_atual.senha = senha
            with open('contas.csv', '+a') as arq:
                informacoes_da_conta = []
                informacoes_da_conta.append(conta_atual._id_da_conta)
                informacoes_da_conta.append(conta_atual.status_da_conta)
                informacoes_da_conta.append(senha)
                informacoes_da_conta.append(conta_atual.titular_da_conta)
                informacoes_da_conta.append(conta_atual.tipo_da_conta)
                informacoes_da_conta.append(conta_atual.divida_da_conta)
                informacoes_da_conta.append(conta_atual.saldo_da_conta)

                warq = csv.writer(arq)
                warq.writerow(informacoes_da_conta)

            cliOpcoes = cli.opcoes_conta(conta_atual)
            cliOpcoes.menu(limpar = limpar)

    elif opcao == 2:
        conta_atual =  autenticacao.logar_na_conta()
        if conta_atual:
            cliOpcoes = cli.opcoes_conta(conta_atual, conta_atual.senha)
            cliOpcoes.menu(limpar = limpar)


    input(' Precione "ENTER" para continuar.')