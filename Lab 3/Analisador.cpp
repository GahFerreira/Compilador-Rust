#include <iostream>

#include "Analisador.hpp"

using namespace std;

void *aloca_variavel(const Type& t)
{
    void *resp;

    if (t.nome == "i32") resp = malloc(sizeof(int));
    else if (t.nome == "f64") resp = malloc(sizeof(double));
    else resp = malloc(sizeof(bool));

    return resp;
}

string Analisador::calcula_ultimo_valor(Function *f, const vector<void *> &params)
{
    if (params.size() != f->parametros.size())
    {
        cout << "Numero de parametros errado\n";
        return "";
    }

	map<string, void*> T;

    for (size_t i = 0; i < params.size(); ++i)
    {
        T[f->parametros[i]->nome] = params[i];
    }

    for (const auto& expressao : f->expressoes)
    {
        if (expressao);
    }
	
	return 0;
}
