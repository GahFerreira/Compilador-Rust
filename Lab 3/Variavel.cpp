#include "Variavel.hpp"

Variavel::Variavel() {}

Variavel* Variavel::extrai_Variavel(No_arv_parse *no)
{
    Variavel* resp = new Variavel;
    
    resp->nome = no->filhos[0]->dado_extra;
    resp->tipo = Type::extrai_Type(no->filhos[2]);

    return resp;
}


// Function::Function() {}

// Function* Function::extrai_Function(No_arv_parse *no) 