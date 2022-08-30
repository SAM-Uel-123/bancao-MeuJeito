import os
import csv
from commandline_interface import *
from validacoes import *
import conta

#======================= #
#     -   Variaveis   -   
#======================= #
limpar = True
linhas = lambda msg, limpar = limpar: cli.detalhes.linhas(msg, limpar = limpar)
clear = lambda: os.system('clear')
cliOpcoes = None
conta_atual = None






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
            if limpar:
                clear()

            conta_atual = conta.ContaBanco()
            while True:
                if limpar:
                    clear()

                titular_da_conta = input('Seu nome: ')
                if validar_informacoes.titular_duplicado(titular_da_conta):
                    print(' esse usuario já existe, tente outro')
                
                else:
                    break

                input(' Precione "ENTER" para continuar')

            while True:
                linhas('Tipos de conta', limpar = limpar)
                print(' cc: Conta Corente,  cp: Conta Poupança.')
                tipo_da_conta = input('Opção: ')
                if tipo_da_conta in ['cc', 'ca']:
                    break
                    
                else:
                    print(' Escolha somente as opções listadas.')

                input(' Precione "ENTER" para continuar.')

            senha = ''
            while not senha:
                linhas('Digite uma senha', limpar = limpar)
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

        
        conta_atual.ativar_conta(titular_da_conta, tipo_da_conta)
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
            cliOpcoes = cli.opcoes_conta(conta_atual)
            cliOpcoes.menu(limpar = limpar)


    input(' Precione "ENTER" para continuar.')