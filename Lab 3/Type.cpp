#include "Type.hpp"

Type* Type::extrai_Type(No_arv_parse* no) 
{
  Type* resp = new Type();
  resp->nome = no->dado_extra;
  
  return resp;
}
