
from datetime import datetime
from calcula_conexao import criar_conexao, fechar_conexao


def insere_entradas(con, valor, data, nome, recorrente):
    valor_entradas = float(input('Valor da conta:'))
    data_entradas = str(input('Digite a data: '))
    data_format = datetime.strptime(data_entradas, '%d-%m-%Y')
    nome_entradas = str(input('Nome da Entrada: '))
    recorrente_entradas = str(input('Recorrente: ')).strip().upper()
    if recorrente_entradas in 'Ss':
        recorrente_entradas = 'sim'
    else:
        recorrente_entradas = 'nao'
    cursor = con.cursor()
    entradas_sql = "INSERT INTO ENTRADAS (valor, data, nome, recorrente) values (%s, %s, %s, %s)"
    input_entradas = (valor_entradas, data_format,
                      nome_entradas, recorrente_entradas)
    cursor.execute(entradas_sql, input_entradas)
    con.commit()
    print('valores de entradas inseridos com sucesso!')
    cursor.close()


def insere_saidas(con, valor, vencimento, nome, recorrente):
    valor_saida = float(input('Valor da saida: '))
    data_saida = str(input('Data da saida: '))
    data_format1 = datetime.strptime(data_saida, '%d-%m-%Y')
    nome_saida = str(input('Descrição da saida: '))
    recorrente_saida = str(input('recorrente: ')).strip().upper()
    if recorrente_saida in 'sS':
        recorrente_saida = 'sim'
    else:
        recorrente_saida = 'nao'
    cursor = con.cursor()
    saida_sql = 'INSERT INTO SAIDAS (valor, vencimento, nome, recorrente) values (%s, %s, %s, %s)'
    input_saida = (valor_saida, data_format1, nome_saida, recorrente_saida)
    cursor.execute(saida_sql, input_saida)
    con.commit()
    print('valores de saídas inseridos com sucesso!')
    cursor.close()


def insere_pagamento(con, valor, data, descricao, id_saidas, id_entradas, pago):
    valor_pagamento = float(input('Valor do pagamento: '))
    data_pagamento = str(input('Data do pagamento: '))
    data_format_pagamento = datetime.strptime(data_pagamento, '%d-%m-%Y')
    descricao_pagamento = str(input('Descrição do pagamento: '))
    input_id_saidas = int(input('ID da saida: '))
    input_id_entradas = int(input('ID da entrada:'))
    input_pago = str(input('Pago [sim/nao]: '))
    cursor = con.cursor()
    pagamento_sql = 'INSERT INTO pagamento (valor, data, descricao, id_saidas, id_entradas, pago) values (%s, %s, %s, %s, %s, %s)'
    input_pagamento = (valor_pagamento, data_format_pagamento,
                       descricao_pagamento, input_id_saidas, input_id_entradas, input_pago)
    cursor.execute(pagamento_sql, input_pagamento)
    con.commit()
    print('valores de saídas inseridos com sucesso!')
    cursor.close()


def consulta_entradas(con, valor, data, nome, recorrente, id_entradas):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM entradas")
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor R$:', coluna[0], end='')
        print(data, '|', 'data:', coluna[1], end='')
        print(nome, '|', 'nome:', coluna[2], end='')
        print(recorrente, '|', 'recorrente', coluna[3], end='')
        print(id_entradas, '|', 'ID entradas:', coluna[4], '\n')
        print('▀' * 95)


def consulta_saidas(con, valor, vencimento, nome, recorrente):
    input_filtro_saidas = str(input('Nome da conta: '))
    consulta_saidas1 = (
        "SELECT * FROM saidas WHERE nome='"+input_filtro_saidas+"'")
    cursor = con.cursor()
    cursor.execute(consulta_saidas1)
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor:', coluna[0], 'R$')
        print(vencimento, coluna[1])
        print(nome, 'nome:', coluna[2])
        print(recorrente, coluna[3])


def consulta_todas_saidas(con, valor, vencimento, nome, recorrente, id_saidas):
    consulta_saidas1 = 'SELECT * FROM saidas'
    cursor = con.cursor()
    cursor.execute(consulta_saidas1)
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor R$:', coluna[0], end='')
        print(vencimento, '|', 'vencimento:', coluna[1], end='')
        print(nome, '|', 'nome:', coluna[2], end='')
        print(recorrente, '|', 'recorrente:', coluna[3], end='')
        print(id_saidas, '|', 'ID saidas:', coluna[4], '\n')
        print('▀' * 95)


def consulta_pagamentos(con, valor, data, descricao, id_saidas, id_entradas, pago):
    id_entrada_pagamento = str(input('Digite o ID da entrada: '))
    pagamento_sql1 = "SELECT * FROM pagamento WHERE id_entradas=" + id_entrada_pagamento
    cursor = con.cursor()
    cursor.execute(pagamento_sql1)
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor R$:', coluna[0], end='')
        print(data, '|', 'data:', coluna[1], end='')
        print(descricao, '|', 'descrição:', coluna[2], end='')
        print(id_saidas, '|', 'ID saidas', coluna[3], end='')
        print(id_entradas, '|', 'ID entradas:', coluna[4], end='')
        print(pago, '|', 'pago:', coluna[5], '\n')
        print('▀' * 95)


def calculo(con, valor):
    calculo_input = str(input('ID de entrada para a soma: '))
    calculo_sql = 'SELECT SUM(valor) FROM pagamento WHERE id_entradas=' + \
        calculo_input
    cursor = con.cursor()
    cursor.execute(calculo_sql)
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, coluna[0])


def main():

    while True:
        con = criar_conexao("localhost", "root", "", "calcula_python")
        print('''Digite a opção desejada:
        [1] inserir entradas
        [2] inserir saidas
        [3] inserir pagamento
        [4] consultar entradas
        [5] consulta todas as saidas
        [6] consultar saidas pelo nome
        [7] consultar pagamentos por ID de entrada
        [8] calculo total por ID de entrada
        [9] sair do programa
        ''')

        opcao = int(input('Qual opção você deseja? '))
        if opcao == 1:
            insere_entradas(con, "", "", "", "")
        elif opcao == 2:
            insere_saidas(con, '', '', '', '')
        elif opcao == 3:
            insere_pagamento(con, '', '', '', '', '', '')
        elif opcao == 4:
            consulta_entradas(con, '', '', '', '', '')
        elif opcao == 5:
            consulta_todas_saidas(con, '', '', '', '', '')
        elif opcao == 6:
            consulta_saidas(con, '', '', '', '')
        elif opcao == 7:
            consulta_pagamentos(con, '', '', '', '', '', '')
        elif opcao == 8:
            calculo(con, '')
        elif opcao == 9:
            print('Obrigado, Volte sempre!')
            break

        fechar_conexao(con)


if __name__ == "__main__":
    main()
