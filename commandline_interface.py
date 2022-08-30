from validacoes import *
from os import system

clear = lambda: system('clear')


class cli:
    """
    Essa Classe serve para criar uma interface em linha de comandos,
 "facil" (na medida do possivel)

    """
    class detalhes:
        """
    Essa Classe trata de detalhes, para a interface, coisas que não são tão
 importantes para a funcionalidade do programa.

        """
        def linhas(msg, linha = '-=', limpar = 0):
            """
    Essa Função cria uma linha em cima e em baixo de uma mensagem passada.
    Com ela, você pode escolher até o tipo de linha que você vai usar
            """
            if limpar:
                from os import system
                system('clear')

            print(linha * 30)
            print(f'{msg:^60}')
            print(linha * 30)

    class opcoes_conta:
        """
    Essa Classe trata da interface que o usuario utilizará quando se logar,
 ela tratará de opções que o usuario poderá escolher.

        """        
        def __init__(self, conta_atual):
            self.conta_atual = conta_atual
            self.senha = conta_atual.senha

        def menu(self, limpar = 1):
            """
    Essa Função cria um loop, com uma tela de escolha para o usuario. 

    Com ela, o usuario pode fazer operações em sua conta.
            """

            while True:
                cli.detalhes.linhas(f' Bem-vindo Sr(a). {self.conta_atual.titular_da_conta}', limpar= limpar)
                print('''
    1 - Sacar 
    2 - Depositar
    3 - Informações da sua conta
    4 - Pagar Dividas
    5 - Apagar conta

    0 - Sair
    ''')
                opcao = validar_entradas.inputInts(' Opção: ')
                if opcao == 0:
                    autenticacao.deslogar_da_conta(self.conta_atual)
                    break

                elif opcao == 1:
                    if limpar:
                        clear()

                    print(f' Seu saldo atual é: R${self.conta_atual.saldo_da_conta}')
                    valorSaque = validar_entradas.inputFloats('Valor de Saques: R$')
                    self.conta_atual.sacar(valorSaque)

                elif opcao == 2:
                    if limpar:
                        clear()

                    print(f' Seu saldo atual é: R${self.conta_atual.saldo_da_conta}')
                    valorDeposito = validar_entradas.inputFloats(' Valor para depositar: R$')
                    self.conta_atual.depositar(valorDeposito)

                elif opcao == 3:
                    if limpar:
                        clear()

                    print('-=' * 30)
                    print(' ID da sua conta: ', self.conta_atual.id_da_conta)
                    print(' Sua conta está: ', 'Ativa' if self.conta_atual.status_da_conta else 'Desativada')
                    print(' O tipo da sua conta é: ', 'Corrente' if self.conta_atual.tipo_da_conta == 'cc' else 'Poupança')
                    print(f' Seu Saldo atual é de: R${self.conta_atual.saldo_da_conta:.2f}')
                    if self.conta_atual.divida_da_conta:
                        print(f'\033[33m Você ten uma divida de: R${float(self.conta_atual.divida_da_conta):.2f}\033[m')

                    print('-=' * 30)

                elif opcao == 4:
                    if limpar:
                        clear()

                    if self.conta_atual.divida_da_conta:
                        while True:
                            print(f' Você tem uma divida de: R${self.conta_atual.divida_da_conta}')
                            pagar = input('Deseja paga-la [S/N]: ')
                            if pagar:
                                if pagar == 's':
                                    if self.conta_atual.saldo_da_conta >= self.conta_atual.divida_da_conta:
                                        self.conta_atual.saldo_da_conta -= self.conta_atual.divida_da_conta
                                        self.conta_atual.divida_da_conta = 0
                                        cli.detalhes.linhas('Divida quitada com sucesso', limpar= limpar)
                                        
                                    else:
                                        #    Aqui posso colocar uma forma de pagamento parcelado,
                                        # mas deixa para outra hora :)

                                        print('Você não tem saldo  o suficiente para pagar ela toda.')
                                    
                                    break

                                elif pagar == 'n':
                                    break

                                else:
                                    print('Digite somente (S) para SIM e (N) para NÃO')

                    else:
                        print('Você não tem nenhuma divida pendente.')

                elif opcao == 5:
                    if limpar:
                        clear()

                    if self.conta_atual.saldo_da_conta > 0:
                        print(' Sua conta ainda tem saldo, por favor, esvazie ela para não perder.')


                    elif self.conta_atual.divida_da_conta > 0:
                        print(' Você tem uma divida para pagar, por favor,quite-a antes de encerrar sua conta.')


                    else:
                        self.conta_atual.desativar_conta()
                        if self.conta_atual.status_da_conta:
                            autenticacao.apagar_conta(self.conta_atual)
                            print('Conta apagada com sucesso.')
                            break
                        
                        else:
                            print(' Não foi possivel encerrar sua conta.')

                input('Pressione "ENTER" para continuar.')

                