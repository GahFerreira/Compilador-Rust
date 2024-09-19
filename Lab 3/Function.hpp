#pragma once
// #include<vector>
#include "TOKEN_ID.hpp"
#include "Type.hpp"
#include "Variavel.hpp"
// #include "Comando.hpp"
#include "Arvore.hpp"
// using namespace std;

class Function 
{
public:
  TOKEN_ID* nome_funcao;
  Type* tipo_retorno;
  vector<Variavel*> parametros;
  // vector<Variavel*> variaveis;
  // vector<Comando*> comandos;

  Function();
  static Function* extrai_Function(No_arv_parse *arv);
  void debug();
};