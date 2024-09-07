# Algoritmo para converter a gramática do site para o algoritmo do Lab 2 que gera a árvore
# Em resumo, substitui as regras vazias de `regra -> ''` para `regra ->`

# Espera como entrada: um arquivo de texto com a sua gramática
# Dá como saída: um arquivo de texto com as regras vazias da gramática convertidas

# Exemplo de uso no terminal: python converte_gramatica.py arquivo_entrada.txt arquivo_saida.txt

import sys

with open(sys.argv[1], "r") as fin:
    with open(sys.argv[2], "w") as fout:
        for regra in fin:
            # Descarta strings vazias ou strings com apenas espaços e quebra de linha
            if regra == "" or regra.isspace():
                continue

            # Regra vazia
            if "->" in regra and "''" in regra:
                regra = regra.split("->", 1)[0] + "->"

            # Retira espaços no final da regra
            while regra[-1].isspace():
                regra = regra[:-1]

            regra += "\n"

            fout.write(regra)