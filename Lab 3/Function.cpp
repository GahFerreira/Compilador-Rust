#include <iostream>

#include "Function.hpp"
// #include "debug-util.hpp"

Function::Function() {}

Function* Function::extrai_Function(No_arv_parse *no) 
{
//   if (no->regra != 1)   return NULL;
//   // Dependente da gramatica. Regra 1 = Funcao.
//   // S -> ID ID ( LP ) { LV LC }

    cout << "---_$$$_---\n";
    no = no->filhos[0];
    no = no->filhos[0];
    // no = no->filhos[0];  
    // no = no->filhos[0];
    // no->debug_no(no);

    // Aqui meu no é a minha função
    Function* resp = new Function();

    resp->nome_funcao = TOKEN_ID::extrai_TOKEN_ID(no->filhos[1]);

    // FunctionReturnType -> TOKEN_ARROW Type
    resp->tipo_retorno = Type::extrai_Type(no->filhos[5]->filhos[1]);

    // no->filhos[3] é a regra: FunctionParameters?
    if (!no->filhos[3]->filhos.empty()) {
        const auto& no_FunctionParameters = no->filhos[3]->filhos[0];

        // O primeiro é diferente
        resp->parametros.push_back(Variavel::extrai_Variavel(no_FunctionParameters->filhos[0]));

        auto& no_CommaParamQuestion = no_FunctionParameters->filhos[1];
        while (!no_CommaParamQuestion->filhos.empty())
        {
            resp->parametros.push_back(Variavel::extrai_Variavel(no_CommaParamQuestion->filhos[0]->filhos[1]));

            no_CommaParamQuestion = no_CommaParamQuestion->filhos[0]->filhos[2];
        }
    }

    for (const auto& param : resp->parametros)
    {
        param->debug();
    }

    auto& no_StatementList = no->filhos[6]->filhos[1];
    while (no_StatementList->filhos.size() > 1)
    {
        resp->expressoes.push_back(Expressao::extrai_Expressao(no_StatementList->filhos[0]));
        no_StatementList = no_StatementList->filhos[1];
    }

    return resp;
}

    //cout << "Nome Funcao: " << no->filhos[1]->dado_extra << '\n';
    // cout << "Ponei: [" <<no->simb<<","<< no->regra << ","<<no->dado_extra << ":";

    // while (no != NULL)
    // {
    //     #include "Arvore.hpp"
    //     cout << "---_$$$_---\n";
    //     // cout << "Dado Extra: " << no->dado_extra << '\n';
        
    //     no = no->filhos[0]; // Crate -> ItemList
    // }

    
    // cout << "Dado Extra: " << no->dado_extra << '\n';
    // no = no->filhos[0]; // ItemList -> Item
    // cout << "Dado Extra: " << no->dado_extra << '\n';
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
  if (tipo_retorno == NULL) cout << "Tipo de retorno: NULL" << endl;
  if (nome_funcao == NULL) cout << "Nome da funcao: NULL" << endl;

  cout << "Funcao:[retorno=" << tipo_retorno->nome << "][nome=" << nome_funcao->nome << "]" << endl;
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