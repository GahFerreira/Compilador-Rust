#pragma once

#include <string>
#include "Arvore.hpp"

using namespace std;

class Type 
{
public:
  	string nome;
	static Type* extrai_Type(No_arv_parse* no);
};