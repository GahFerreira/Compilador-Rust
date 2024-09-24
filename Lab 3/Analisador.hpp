#pragma once

#include "Function.hpp"
#include <vector>
#include <map>
using namespace std;

class Analisador {
public:
    string calcula_ultimo_valor(Function *f, const vector<void *> &params);
};

