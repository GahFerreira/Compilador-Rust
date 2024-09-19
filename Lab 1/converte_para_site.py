# Algoritmo que converte o arquivo de saída do Lab 1 para ser testado no site JsMachines

while True:
    try:
        print(input().split(' ')[0], end=' ')
    except EOFError:
        break