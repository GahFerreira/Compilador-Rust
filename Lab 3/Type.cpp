#include "Type.hpp"

#include <iostream>

Type* Type::extrai_Type(No_arv_parse* no) 
{
  Type* resp = new Type();

  // Type -> BasicType -> TOKEN_bool | TOKEN_i32 | TOKEN_f64
  resp->nome = no->filhos[0]->filhos[0]->dado_extra;
  
  return resp;
}