#pragma once

#include "Arvore.hpp"
#include "Expressao.hpp"

class ExpressaoLiteral : Expressao
{
public:
    Expressao *esquerda, *direita;
    void *calcular_valor();

    // TOKEN_ID* nome_funcao;
    // Type* tipo_retorno;
    // vector<Variavel*> parametros;
    // // vector<Variavel*> variaveis;
    // vector<Expressao*> expressao;

    // Function();
    // static Function* extrai_Function(No_arv_parse *arv);
    // void debug();
};