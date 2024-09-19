#include "TOKEN_ID.hpp"

TOKEN_ID* TOKEN_ID::extrai_TOKEN_ID(No_arv_parse* no) 
{
  TOKEN_ID* resp = new TOKEN_ID();
  resp->nome = no->dado_extra;
  
  return resp;
}
