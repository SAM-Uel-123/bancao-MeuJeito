class validar_entradas:
    """
    Essa Classe trata de entradas de dados, para facilitar 
 a vida de quem está programando, automatizando o processo de 
 validação de entradas, de acordo com as necessidades.

    Tem a validação para numeros inteiros, para utilizar em escolhas de menus por exemplo,
 ou para valores quebrados, como na hora de sacar dinhero do banco por exemplo.

    """
    def inputInts(msg) -> int:
        """
    Essa Função trata a entrada de dados, deixando passar somente numeros inteiros.

        """
        while True:
            valor = input(msg)
            if valor:
                try:
                    valor = int(valor)
                    return int(valor)

                except:
                    print('valor Invalido, tente somente numeros.')
                    continue

            else:
                print('Digite algo.')


    def inputFloats(msg) -> float:
        """
    Essa Função trata a entrada de dados, deixando passar somente numero do tipo float.

        """
        while True:
            valor = input(msg)
            if valor:
                try:
                    valor = float(valor)
                    return float(valor)

                except:
                    print('valor Invalido, tente somente numeros.')
                    continue

            else:
                print('Digite algo.')

class validar_informacoes:
    """
    Essa classe trata sobre validações de informações, como:
 checar se nosso "Banco de Dados" está "online", salvar informações alteradas
 testar se existe usuarios duplicados.

    """

    def checar_arquivos_de_contas():
        """
    Essa Função trata de checar se nosso "Banco de Dados" está "online"
 usando o modulo CSV.
    
    Testando se ele existe e se tem dados nele.

        """

        import csv
        infos = None
        dados = []
        try:
            with open('contas.csv', 'r') as arq:
                arq.close()

        except:
            with open('contas.csv', 'w') as arq:
                csv.writer(arq).writerow('')


        with open('contas.csv', 'r') as rarq:
            interator = csv.reader(rarq)
            for linha in interator:
                if linha and len(linha) == 7:
                    dados.append(linha)


        with open('contas.csv', 'w') as warq:
            wcsv = csv.writer(warq, delimiter=',')
            if dados:
                for d in dados:
                    wcsv.writerow(d)

            if not  dados or len(dados[0]) < 7:
                infos = ['id', 'status', 'senha', 'titular', 'tipo_da_conta', 'divida', 'saldo']
                wcsv.writerow(infos)

    def _salvar_informacoes(obj_conta):
        """
    Essa Função Sincroniza as informações alteradas com o "Banco de Dados".

        """
        import csv
        validar_informacoes.checar_arquivos_de_contas()
        dados = []
        informacoes_da_conta = []
        informacoes_da_conta.append(obj_conta.id_da_conta)
        informacoes_da_conta.append(obj_conta.status_da_conta)
        informacoes_da_conta.append(obj_conta.senha)
        informacoes_da_conta.append(obj_conta.titular_da_conta)
        informacoes_da_conta.append(obj_conta.tipo_da_conta)
        informacoes_da_conta.append(obj_conta.divida_da_conta)
        informacoes_da_conta.append(obj_conta.saldo_da_conta)

        with open('contas.csv', 'r') as rarq:
            iterator = csv.reader(rarq)
            for linha in iterator:
                if linha:
                    if obj_conta.titular_da_conta == linha[3] and obj_conta.senha == linha[2]:
                        linha = informacoes_da_conta
                    dados.append(linha)
                

        with open('contas.csv', 'w') as warq:
            arqWriter = csv.writer(warq, delimiter= ',')
            for dado in dados:
                arqWriter.writerow(dado)


    def titular_duplicado(titular):
        """
    Essa Função checa se existe usuarios com o mesmo nome que foi passa para ela.

        """
        import csv
        checar_arquivos_de_contas()
        with open('contas.csv', 'r') as rarq:
            iterator = csv.reader(rarq)
            for linha in iterator:
                if titular == linha[3]:
                    return True

        return False


class autenticacao:
    """
    Essa classe trata de operações de autenticações, como:
 Logins, Saidas de contas.

    com esse modulo, é possivel se autenticar com "segurança" em sua conta
do nosso "Bancâo" ;).


    """
    def deslogar_da_conta(obj_conta):
        """
    Função para tratar o desligamento de sua sessão
com sua conta.

    para utilizala, você precisa passar como parametro o objeto
de conta, que foi usado para criar sua conta.
        """

        if obj_conta.status_da_conta:
            validar_informacoes._salvar_informacoes(obj_conta)


    def logar_na_conta(usuario = '', senha = ''):
        """
    Função para efetuar a entrada com "segurança" em sua conta, por meio
 de exigencia de credenciais e dados VALIDOS escolhidos por você ;).

    para utilizala, basta somente passar o usuario de sua conta e sua senha,
 que a função buscará no nosso "Banco de Dados" por seu usuario e em seguida,
 ira valida-lo.
        """

        import csv
        import conta
        validar_informacoes.checar_arquivos_de_contas()
        conta_atual = None
        logado = 0
        if not usuario:
            usuario = input(' Seu nome: ')

        if not senha:
            senha = input('Sua senha: ')

        with open('contas.csv', 'r') as rarq:
            next(rarq)
            contas = csv.reader(rarq)
            for linha in contas:
                if usuario == linha[3]:
                    logado = 1
                    if senha == linha[2]:
                        print('Logado com sucesso.') 
                        conta_atual = conta.ContaBanco()
                        conta_atual.id_da_conta = int(linha[0])
                        conta_atual.status_da_conta = linha[1]
                        conta_atual.senha = linha[2]
                        conta_atual.titular_da_conta = linha[3]
                        conta_atual.tipo_da_conta = linha[4]
                        conta_atual.divida_da_conta = float(linha[5])
                        conta_atual.saldo_da_conta = float(linha[6])
                        
                        logado = 0
                        break
                    break
                    
                logado = 2

        if not logado:
            return conta_atual

        elif logado:
            print(' Erro ao efetuar o login.')

        elif logado == 1:
            print(' Senha incorreta')

        elif logado == 2:
            print(' Titular errado')
        
        return False