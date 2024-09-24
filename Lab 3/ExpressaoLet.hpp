#pragma once

#include "Arvore.hpp"
#include "Expressao.hpp"
#include "Variavel.hpp"

class ExpressaoLet : public Expressao
{
public:
    Variavel *nova_variavel;
    
    static ExpressaoLet *extrair_ExpressaoLet(No_arv_parse *no);
};