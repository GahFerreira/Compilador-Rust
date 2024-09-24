#include "ExpressaoSoma.hpp"

void *ExpressaoSoma::calcular_valor()
{
    if (esquerda->tipo == NULL or direita->tipo == NULL)
    {
        throw "[Erro] Soma com expressao nula!\n";
    }

    if (esquerda->tipo->nome == "bool" or direita->tipo->nome == "bool")
    {
        throw "[Erro] Soma com booleano!\n";
    }

    if (esquerda->tipo->nome != direita->tipo->nome)
    {
        throw "[Erro] Soma entre tipos diferentes!\n";
    }

    tipo = esquerda->tipo;

    void *a = esquerda->calcular_valor();
    void *b = direita->calcular_valor();
    void *c;

    if (esquerda->tipo->nome == "i32")
    {
        c = malloc(sizeof(int));
        *(int *)c = *(int *)a + *(int *)b;
    }
    else
    {
        c = malloc(sizeof(double));
        *(double *)c = *(double *)a + *(double *)b;
    }

    free(a);
    free(b);

    return c;
}