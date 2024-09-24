#pragma once

#include "Arvore.hpp"
#include "Type.hpp"

class Expressao 
{
public:
    Type *tipo;
    void *calcular_valor();
    static Expressao *extrai_Expressao(No_arv_parse *no);

    // TOKEN_ID* nome_funcao;
    // Type* tipo_retorno;
    // vector<Variavel*> parametros;
    // // vector<Variavel*> variaveis;
    // vector<Expressao*> expressao;

    // Function();
    // static Function* extrai_Function(No_arv_parse *arv);
    // void debug();
};