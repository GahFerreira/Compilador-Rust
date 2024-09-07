# Algoritmo para ordenar os valores da linha L da Planilha do Lab 2

# Espera como entrada: um arquivo de texto, com os valores da linha L, um por linha
# Dá como saída: um arquivo de texto com esses valores ordenados pelo primeiro número da linha

def cmp(elem):
    a = elem.split(' ')
    return int(a[0])

entrada = []

while True:
    try:
        entrada.append(input())

    except EOFError:
        entrada = sorted(entrada, key = cmp)

        for elem in entrada:
            print(elem)

        break