#include "Function.hpp"
// #include "debug-util.hpp"
#include <iostream>

Function::Function() {}

Function* Function::extrai_Function(No_arv_parse *no) 
{
//   if (no->regra != 1)   return NULL;
//   // Dependente da gramatica. Regra 1 = Funcao.
//   // S -> ID ID ( LP ) { LV LC }

    cerr << "---_$$$_---\n";
    no = no->filhos[0];
    no = no->filhos[0];
    // no = no->filhos[0];  
    // no = no->filhos[0];
    // no->debug_no(no);

    // Aqui meu no é a minha função
    Function* resp = new Function();

    resp->nome_funcao = TOKEN_ID::extrai_TOKEN_ID(no->filhos[1]);
    resp->tipo_retorno = Type::extrai_Type(no->filhos[5]);

    // no->filhos[3] é a regra: FunctionParameters?
    if (no->filhos[3]->filhos.size() != 0) {
        const auto& no_FunctionParameters = no->filhos[3]->filhos[0];

        // O primeiro é diferente
        resp->parametros.push_back(Variavel::extrai_Variavel(no_FunctionParameters->filhos[0]));

        for (size_t i_parametro = 1; i_parametro < no_FunctionParameters->filhos.size(); ++i_parametro)
        {
            resp->parametros.push_back(Variavel::extrai_Variavel(no_FunctionParameters->filhos[i_parametro]->filhos[0]->filhos[1]));
        }
    }

    // no->filhos[3]->debug_no(no->filhos[3]);
    cerr << "Dado Extra: " << no->filhos[3]->dado_extra << '\n';
    cerr << "Regra: " << no->filhos[3]->regra << '\n';
    cerr << "Simb: " << no->filhos[3]->simb << '\n';
    
    cerr << "Numero de filhos: " << no->filhos[3]->filhos.size() << '\n';

    return resp;
}

    //cerr << "Nome Funcao: " << no->filhos[1]->dado_extra << '\n';
    // cerr << "Ponei: [" <<no->simb<<","<< no->regra << ","<<no->dado_extra << ":";

    // while (no != NULL)
    // {
    //     #include "Arvore.hpp"
    //     cerr << "---_$$$_---\n";
    //     // cerr << "Dado Extra: " << no->dado_extra << '\n';
        
    //     no = no->filhos[0]; // Crate -> ItemList
    // }

    
    // cerr << "Dado Extra: " << no->dado_extra << '\n';
    // no = no->filhos[0]; // ItemList -> Item
    // cerr << "Dado Extra: " << no->dado_extra << '\n';
    // no = no->filhos[0]; // Item -> Function

    // no = no->filhos[0];

    // Function* resp = new Function();
    // resp->nome_funcao = TOKEN_ID::extrai_TOKEN_ID(no->filhos[1]);

    // cout << "Nome da Funcao: " << resp->nome_funcao << '\n';

//   res->tipo_retorno = ID::extrai_ID(no->filhos[0]);
//   res->parametros = Variavel::extrai_lista_parametros(no->filhos[3]);
//   res->variaveis = Variavel::extrai_lista_variaveis(no->filhos[6]);
//   res->comandos = Comando::extrai_lista_comandos(no->filhos[7]);
    // return resp;


// void debug_variaveis(const vector<Variavel*> &vars, int tab) {
//   for (int iv = 0; iv < vars.size(); ++iv) {
//     tab3(tab);
//     vars[iv]->debug_com_tab(tab+1);
//   }
// }

// void debug_comandos(const vector<Comando*> &coms, int tab) {
//   for (int ic = 0; ic < coms.size(); ++ic) {
//     coms[ic]->debug_com_tab(tab+1);
//   }  
// }

void Function::debug() 
{
  if (tipo_retorno == NULL) cerr << "Tipo de retorno: NULL" << endl;
  if (nome_funcao == NULL) cerr << "Nome da funcao: NULL" << endl;

  cerr << "Funcao:[retorno=" << tipo_retorno->nome << "][nome=" << nome_funcao->nome << "]" << endl;
//   cerr << "      (Param:(";
//   fflush(stderr);
//   for (int i_par = 0; i_par < parametros.size(); ++i_par) {
//     cerr << (parametros[i_par])->tipo->nome << " " <<
//       (parametros[i_par])->nome->nome << ", ";
//   }
//   cerr << ") { " << endl;
//   debug_variaveis(variaveis, 1);
//   debug_comandos(comandos, 1);
//   cerr << "}" <<  endl;
}
