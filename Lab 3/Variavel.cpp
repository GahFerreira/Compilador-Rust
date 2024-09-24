#include <iostream>

#include "Variavel.hpp"

using namespace std;

Variavel::Variavel() {}

Variavel* Variavel::extrai_Variavel(No_arv_parse *no)
{
    Variavel* resp = new Variavel;
    
    resp->nome = no->filhos[0]->dado_extra;
    resp->tipo = Type::extrai_Type(no->filhos[2]);

    return resp;
}

void Variavel::debug() 
{
    cout << "VARIAVEL:\n[\n"
         << "\tNome: " << nome << "\n"
         << "\tTipo: " << ((tipo == NULL) ? "NULL" : tipo->nome) << "\n"
         << "]\n";

//   cout << "      (Param:(";
//   fflush(stderr);
//   for (int i_par = 0; i_par < parametros.size(); ++i_par) {
//     cout << (parametros[i_par])->tipo->nome << " " <<
//       (parametros[i_par])->nome->nome << ", ";
//   }
//   cout << ") { " << endl;
//   debug_variaveis(variaveis, 1);
//   debug_comandos(comandos, 1);
//   cout << "}" <<  endl;
}


// Function::Function() {}

// Function* Function::extrai_Function(No_arv_parse *no) 