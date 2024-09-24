#include "Expressao.hpp"
#include "ExpressaoLet.hpp"

Expressao *Expressao::extrai_Expressao(No_arv_parse *no)
{
    if (no->filhos[0]->simb == "LetStatement")
    {
        return ExpressaoLet::extrair_ExpressaoLet(no->filhos[0]);
    }
}