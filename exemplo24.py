import random as rnd

def calcula_media(v):   
    """
    Funcao que calcula a media dos valores de uma lista
    """
    if len(v) > 10:
        return sum(v)/len(v)
    else:
        return 0 

def inicializa_lista(quantidade=5):
    lista = []
    for _ in range(quantidade):
        valor = rnd.randint(0,100)
        lista.append(valor)
    return lista

def pesquisa (valor, lista):
    return valor in lista

def menu():
    print('='*10)
    print('1- iniciar lista aletoria')
    print('2- calcular media')
    print('3- pesquisar valor')
    print('4- sair')
    return int(input('Digite sua opcao: '))
# main
if __name__ == '__main__':
    v = []
    op=0
    while op !=4:
        op = menu()
        if op == 1:
            v = inicializa_lista()
            print(v)
        elif op == 2:
            media = calcula_media(v)
            print(f"a media eh {media:.2f}")
        elif op == 3:
            buscar_valor = int(input('digite valor a ser procurado: '))
            if pesquisa(buscar_valor, v):
                print(f'{buscar_valor} esta na lista')
            else:
                print(f'{buscar_valor} nao esta na lista')
    else:
        print('Saindo....')

    # media = calcula_media(v)
    # print(v)
    # print(f"a media eh {media:.2f}")