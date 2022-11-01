registro = [{
        'mes_ano_referencia' : '10-2022',
        'total_habitantes' : 1000000,
        'total_obitos' : 20000
    },
    {
        'mes_ano_referencia': '08-2022', 
        'total_habitantes': 100, 
        'total_obitos': 10
    }, 
    {
        'mes_ano_referencia': '09-2022', 
        'total_habitantes': 500, 
        'total_obitos': 20
    },
    {
        'mes_ano_referencia': '09-2021',
        'total_habitantes': 567,
        'total_obitos': 123
    },
    {
        'mes_ano_referencia': '05-2021',
        'total_habitantes': 345,
        'total_obitos': 214
    },
    {
        'mes_ano_referencia': '05-2019',
        'total_habitantes': 1000,
        'total_obitos': 10
}
]

def menuPrincipal():
    print("**-- Menu Principal --**\n1 – Cadastrar mês de referência\n2 – Exibir dados do mês de referência [pesquisa por mês]\n3 – Relatório comparativo – Referência 2019\n4 – Listar todos os meses cadastrados")
    escolha = input("Digite a opção desejada: ")
    return int(escolha)


def cadastrandoMesAno(mesAno, tHab, tObi):
    newDict = dict(zip(['mes_ano_referencia', 'total_habitantes', 'total_obitos'], [mesAno, int(tHab), int(tObi)]))
    registro.append(newDict)
    print("***** Gravado com sucesso *****")

def consultaMesAno(mesAno):
    retorno = ''

    for r in registro:
        if r['mes_ano_referencia'] == mesAno:
            retorno = r

    if retorno == '':
        return "\n\t***** Mês-ano não cadastrado! *****\n"
    else:
        return f"\n\tMês-ano..............: {retorno['mes_ano_referencia']}\n\tTotal de Habitantes..: {retorno['total_habitantes']}\n\tTotal de óbitos......: {retorno['total_obitos']}\n"

def pesquisaAno(anoASerComparado):
    totalHab = 0
    totalObt = 0
    taxaAno = 0
    taxa2019 = 15.0
    comparativo = 0

    for r in registro:
        ano = r['mes_ano_referencia'].split("-")[1]
        if ano == str(anoASerComparado):
            totalHab += r['total_habitantes']
            totalObt += r['total_obitos']
    
    if totalHab != 0 and totalObt != 0:
        print(f'\n\tTotal de Habitantes..............: {totalHab}')
        print(f'\tTotal de óbitos..................: {totalObt}')
        print(f'\tTaxa por 100k habitantes - {ano}..: {taxaAno}')
        print(f'\tTaxa por 100k habitantes - 2019..: {taxa2019}')
        print(f'\tComparativo % entre 2021-2019....: {comparativo}\n')
    else:
        print(f"\n\t***** Não há dados referente a este ano *****\n")

repeat = True

while repeat:
    escolha = menuPrincipal()
    if escolha == 1:
        repeatEscolha1 = True
        mesAno = input("\nMês-ano..............: ")
        tHab   = input("Total de Habitantes..: ")
        tObi   = input("Total de óbitos......: ")
        cadastrandoMesAno(mesAno, tHab, tObi)

        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 2:
        mesAno = input("\nDigite o mês-ano desejado (mm-aaaa): ")
        print(consultaMesAno(mesAno))
        
        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 3:
        anoASerPesquisado = input("Digite ano a ser comparado: ")
        pesquisaAno(anoASerPesquisado)
        
        aux = input("\nDeseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    elif escolha == 4:
        print("Opção número 4")
        
        aux = input("Deseja continuar? (sim ou nao): ")
        if aux == 'nao':
            repeat = False
    else:
        print("\n\tOpção inválida, escolha entre 1, 2 ,3 ou 4\n")

# print(registro)