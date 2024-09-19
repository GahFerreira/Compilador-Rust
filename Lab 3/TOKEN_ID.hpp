#pragma once

#include <string>
#include "Arvore.hpp"

using namespace std;

class TOKEN_ID {
public:
  string nome;
  static TOKEN_ID* extrai_TOKEN_ID(No_arv_parse* no);
};
