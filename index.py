registro = [{
    'mes_ano_referencia' : '10-2022',
    'total_habitantes' : 1000000,
    'total_obitos' : 20000
    }
]

def menuPrincipal():
    print("**-- Menu Principal --**\n1 – Cadastrar mês de referência\n2 – Exibir dados do mês de referência [pesquisa por mês]\n3 – Relatório comparativo – Referência 2019\n4 – Listar todos os meses cadastrados")
    escolha = input("Digite a opção desejada: ")
    return int(escolha)


def cadastrandoMesAno(mesAno, tHab, tObi):
    newDict = dict(zip(['mes_ano_referencia', 'total_habitantes', 'total_obitos'], [mesAno, tHab, tObi]))
    registro.append(newDict)
    print("***** Gravado com sucesso *****")

repeat = True

while repeat:
    escolha = menuPrincipal()
    if escolha == 1:
        repeatEscolha1 = True
        mesAno = input("Mês-ano..............: ")
        tHab   = input("Total de Habitantes..: ")
        tObi   = input("Total de óbitos......: ")
        cadastrandoMesAno(mesAno, tHab, tObi)

        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 2:
        print("Opção número 2")
        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 3:
        print("Opção número 3")
        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 4:
        print("Opção número 4")
        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    else:
        print("\n\tOpção inválida, escolha entre 1, 2 ,3 ou 4\n")

print(registro)