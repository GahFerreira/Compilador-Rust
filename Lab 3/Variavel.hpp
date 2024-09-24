#pragma once

#include <string>
#include "Arvore.hpp"
#include "Type.hpp"

using namespace std;

// Vai ser chamada para os parâmetros da função
class Variavel
{
public:
    string nome;
    Type *tipo;

    Variavel();
    static Variavel* extrai_Variavel(No_arv_parse* no);
    void debug();
};