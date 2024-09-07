# Programa para gerar código em JavaCC de reconhecimento léxico da linguagem Go.

nome_da_classe = 'Compilador'
prefixo_token = 'TOKEN_'
posfixo_token = ''
comentario_como_token = False

# Responde se o token é ou não final. 
# Por ex.: digitos que comporão números não são tokens finais.
def eh_token_final(nome_do_token):
  if nome_do_token[0] == '#':
    return False

  return True

# Adapta o nome do token para a regra usada.
def adaptar(nome_do_token):
  nome_final = None

  # Para tokens que não sejam finais, como digitos que comporão números.
  if eh_token_final(nome_do_token) == False:
    nome_final = '#' + prefixo_token + nome_do_token[1:] + posfixo_token

  else:
    nome_final = prefixo_token + nome_do_token + posfixo_token

  return nome_final

## Tokens normais: seus nomes e valores são iguais.
tipos = [ 'bool', 
          'i8', 'i16', 'i32', 'i64', 'i128',
          'u8', 'u16', 'u32', 'u64', 'u128', 
          'f32', 'f64',
          'char', 'str'
        ]

# Nota: não comporta as palavras-chaves fracas (union, macro_rules, 'static)
palavras_chave = [ 'as', 'async', 'await', 'break', 'const',
                   'continue', 'crate', 'dyn', 'else', 'enum',
                   'extern', 'false', 'fn', 'for', 'if', 'impl',
                   'in', 'let', 'loop', 'match', 'mod', 'move',
                   'mut', 'pub', 'ref', 'return', 'self', 'Self',
                   'static', 'struct', 'super', 'trait', 'true',
                   'type', 'unsafe', 'use', 'where', 'while'
                 ]

## Tokens especiais: seus nomes e valores são distintos.
comentarios = \
{
  'LINE_COMMENT': f'''"//" (~["\\n", "\\r"])*'''

  # Comentários multilinha são realizados através do estado léxico IN_GENERAL_COMMENT
}

espacos_brancos = \
{
  'SPACE': '" "',
  'HORIZONTAL_TAB': '"\\t"',
  'CARRIAGE_RETURN': '"\\r"',
  'NEWLINE': '"\\n"'
}

operadores = \
{
  'ARROW': '"->"',

  'PLUS_ASSIGN': '"+="',
  'PLUS': '"+"',

  'MINUS_ASSIGN': '"-="',
  'MINUS': '"-"',

  'MULTIPLY_ASSIGN': '"*="',
  'MULTIPLY': '"*"',

  'DIVIDE_ASSIGN': '"/="',
  'DIVIDE': '"/"',

  'REMAINDER_ASSIGN': '"%="',
  'REMAINDER': '"%"',

  'OR': '"||"',
  'BIT_OR_ASSIGN': '"|="',
  'BIT_OR': '"|"',

  'AND': '"&&"',
  'BIT_AND_ASSIGN': '"&="',
  'BIT_AND': '"&"',

  'BIT_XOR_ASSIGN': '"^="',
  'BIT_XOR': '"^"',

  'COMMA': '","',
  'DOT_DOT_ASSIGN': '"..="',
  'DOT_DOT': '".."',
  'DOT': '"."',
  'COLON': '":"',
  'SEMICOLON': '";"',

  'LEFT_SHIFT_ASSIGN': '"<<="',
  'LEFT_SHIFT': '"<<"',
  'RIGHT_SHIFT_ASSIGN': '">>="',
  'RIGHT_SHIFT': '">>"',
  
  'LESS_EQUAL': '"<="',
  'LESS': '"<"',
  'GREATER_EQUAL': '">="',
  'GREATER': '">"',
  'DIFFERENT': '"!="',
  'NOT': '"!"',
  'EQUAL': '"=="',

  'ASSIGN': '"="',

  'OPEN_PARENTHESIS': '"("',
  'CLOSE_PARENTHESIS': '")"',

  'OPEN_BRACKET': '"["',
  'CLOSE_BRACKET': '"]"',

  'OPEN_BRACE': '"{"',
  'CLOSE_BRACE': '"}"',

  'QUESTION': '"?"',
  'AT': '"@"',
  'TILDE': '"~"',
}

# Esses tokens (não finais) são referenciados em outros tokens.
caracteres = \
{
  '#XID_START': '["A"-"Z", "a"-"z"]', #'~["\\n", "0"-"9"]',
  '#XID_CONTINUE': '["A"-"Z", "a"-"z", "0"-"9"]' #'~["\\n"]',
}

# Esses tokens (não finais) são referenciados em outros tokens.
digitos = \
{
  # Digitos Unitários
  '#BINARY_DIGIT': '"0" | "1"',

  '#OCTAL_DIGIT': '["0"-"7"]',

  '#DECIMAL_DIGIT': '["0"-"9"]',

  '#HEX_DIGIT': '["0"-"9", "A"-"F", "a"-"f"]',
}

# Em Rust, apesar de '_42' ser um identificador, '0x_42' é um número literal válido.
numeros = \
{
  # Mantissas e Expoentes
  '#DECIMAL_EXPONENT': 
    f'''("e" | "E") ("+" | "-")? ("_" | < {adaptar('DECIMAL_DIGIT')} > )*''' + 
    f'''< {adaptar('DECIMAL_DIGIT')} > ("_" | < {adaptar('DECIMAL_DIGIT')} > )*''',

  # Ponto Flutuantes - Rust dá suporte apenas para decimal
  'DECIMAL_FLOAT_LITERAL': 
    f'''< {adaptar('DECIMAL_LITERAL')} > "." | ''' + 
    f'''< {adaptar('DECIMAL_LITERAL')} > "." < {adaptar('DECIMAL_LITERAL')} > | ''' +
    f'''< {adaptar('DECIMAL_LITERAL')} > ("." < {adaptar('DECIMAL_LITERAL')} > )? < {adaptar('DECIMAL_EXPONENT')} >''',

  '#FLOAT_LITERAL':
    f'''< {adaptar('DECIMAL_FLOAT_LITERAL')} >''',

  # Números Inteiros
  'BINARY_LITERAL': f'''"0" ("b" | "B") ("_" | < {adaptar('BINARY_DIGIT')} > )*''',

  'OCTAL_LITERAL': f'''"0" ("o" | "O")? ("_" | < {adaptar('OCTAL_DIGIT')} > )*''',

  'DECIMAL_LITERAL': f'''"0" | ( ["1"-"9"] ("_" | < {adaptar('DECIMAL_DIGIT')} > )* )''',

  'HEX_LITERAL': f'''"0" ("x" | "X") ("_" | < {adaptar('HEX_DIGIT')} > )* ''',

  '#INT_LITERAL': 
    f'''< {adaptar('BINARY_LITERAL')} > | < {adaptar('OCTAL_LITERAL')} > | ''' +
    f'''< {adaptar('DECIMAL_LITERAL')} > | < {adaptar('HEX_LITERAL')} >''',
}

strings = \
{
  '#QUOTE_ESCAPE': # '\''
    f'''"\\\\\\\'" | "\\\\\\\""''',

  '#ASCII_ESCAPE': # '\x5F', '\n', '\r', '\t', '\\', '\0'
    f'''"\\\\x" < {adaptar('OCTAL_DIGIT')} > < {adaptar('HEX_DIGIT')} > | ''' + 
    f'''"\\\\n" | "\\\\r" | "\\\\t" | "\\\\\\\\" | "\\\\0"''',

  'CHAR_LITERAL':
    f'''"'" (~["\\'", "\\\\", "\\n", "\\r", "\\t"] | ''' + 
    f'''< {adaptar('QUOTE_ESCAPE')} > | < {adaptar('ASCII_ESCAPE')} > )"'"''',

  'STRING_LITERAL': 
    f'''"\\\"" (~["\\"", "\\\\"] | ''' +
    f'''< {adaptar('QUOTE_ESCAPE')} > | < {adaptar('ASCII_ESCAPE')} >)* "\\\""'''
}

identificadores = \
{
  'ID':
    f'''< {adaptar('XID_START')} > ( < {adaptar('XID_CONTINUE')} > )* | ''' +
    f'''"_" < {adaptar('XID_CONTINUE')} > ( < {adaptar('XID_CONTINUE')} > )*''',
}

# Listando todas as listas de tokens
listas_de_tokens_normais = \
{
  'Tipos': tipos,

  'Palavras-Chave': palavras_chave,
}

listas_de_tokens_especiais = \
{
  'Caracteres': caracteres,

  'Digitos': digitos,

  'Comentários': comentarios,

  'Operadores': operadores,

  'Números': numeros,

  'Strings': strings,

  'Identificadores': identificadores
}

'''
  Por padrão, JavaCC analisa o código no estado DEFAULT.
  As regras de TOKEN, SKIP e MORE são definidas somente para este estado.
  Quando dentro de `MORE: `, temos uma regra, como `"/*": IN_GENERAL_COMMENT`, isso significa que,
quando o JAVACC ler `/*` do código, ele irá para o estado `IN_GENERAL_COMMENT`.
  Dessa forma, precisamos definir as regras que serão válidas neste estado. Para este exemplo, as
regras são definidas dentro de: `< IN_GENERAL_COMMENT > TOKEN:` e `< IN_GENERAL_COMMENT > MORE:`.
  `< IN_GENERAL_COMMENT > TOKEN:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, haverá uma criação de um token, e a transição de volta ao estado DEFAULT.
  `< IN_GENERAL_COMMENT > MORE:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, ele será pulado, mas fará parte do próximo token a ser criado.
'''
estados_lexicos = \
{
  'IN_GENERAL_COMMENT': 
  {
    'TOKEN' if comentario_como_token == True else 'SPECIAL_TOKEN': ('GENERAL_COMMENT', '"*/"'),
    'MORE': ['< ~[] >'],
    'IN_MORE': '"/*"'
  }
}

# Início dos prints.

ultimo_token_da_ultima_lista = \
  list( (list(listas_de_tokens_especiais.values())[-1]).keys() )[-1]

# Implementa a classe base.
print(f'''\
PARSER_BEGIN({nome_da_classe})

public class {nome_da_classe}
{{
  public static void main(String args[]) throws ParseException, TokenMgrError
  {{
    {nome_da_classe} parser = new {nome_da_classe}(System.in);

    parser.Inicio();
  }}
}}

PARSER_END({nome_da_classe})

''')

print('''\
/*
  Por padrão, JavaCC analisa o código no estado DEFAULT.
  As regras de TOKEN, SKIP e MORE são definidas somente para este estado.
  Quando dentro de `MORE: `, temos uma regra, como `"/*": IN_GENERAL_COMMENT`, isso significa que,
quando o JAVACC ler `/*` do código, ele irá para o estado `IN_GENERAL_COMMENT`.
  Dessa forma, precisamos definir as regras que serão válidas neste estado. Para este exemplo, as
regras são definidas dentro de: `< IN_GENERAL_COMMENT > TOKEN:` e `< IN_GENERAL_COMMENT > MORE:`.
  `< IN_GENERAL_COMMENT > TOKEN:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, haverá uma criação de um token, e a transição de volta ao estado DEFAULT.
  `< IN_GENERAL_COMMENT > MORE:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, ele será pulado, mas fará parte do próximo token a ser criado.
*/\
''')

for nome_estado, dados_estado in estados_lexicos.items():
  # Printando '< ESTADO > {SPECIAL_}TOKEN:'
  token_kind = 'TOKEN'
  if 'TOKEN' not in dados_estado:
    token_kind = 'SPECIAL_TOKEN'

  print(f'''< {nome_estado} > {token_kind}:''',
        f'''{{''',
        f'''  < {adaptar(dados_estado[token_kind][0])}: {dados_estado[token_kind][1]} > : DEFAULT''',
        f'''}}''',
        f'''''',
        sep = '\n')

  # Printando '< ESTADO > MORE:'
  print(f'''< {nome_estado} > MORE:''',
        f'''{{''',
        f'''  {dados_estado['MORE'][0]}''',
        sep = '\n')

  for regra in dados_estado['MORE'][1:]:
    print(f'|',
          f'  {regra}',
          sep = '\n')

  print('}\n')

# MORE
print ('MORE:',
       '{',
       sep = '\n')

for nome_estado, dados_estado in estados_lexicos.items():
  print(f'''  {dados_estado['IN_MORE']}: {nome_estado}''',
        '|' if nome_estado != list(estados_lexicos.keys())[-1] else '}\n\n',
        sep = '\n')

# SKIP
print('SKIP:',
      '{',
      '  /** Espaços em Branco */',
      sep = '\n')

for nome_token, valor_token in espacos_brancos.items():
  print(f'  < {adaptar(nome_token)}: {valor_token} >',
        f'|' if nome_token != list(espacos_brancos.keys())[-1] else '}\n\n',
        sep = '\n')

# TOKEN
print('TOKEN:',
      '{',
      sep = '\n')

## Tokens Normais
for nome_lista, lista in listas_de_tokens_normais.items():
  print(f'  /** {nome_lista} */')

  for token in lista:
    print(f'  < {adaptar(token)}: "{token}" >',
          f'|',
          sep = '\n')

## Tokens Especiais
for nome_lista, lista in listas_de_tokens_especiais.items():
  if comentario_como_token == False and nome_lista == 'Comentários':
    continue

  print(f'  /** {nome_lista} */')

  for nome_token, valor_token in lista.items():
      print(f'  < {adaptar(nome_token)}: {valor_token} >',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')
    
# SPECIAL TOKEN
if comentario_como_token == False:
  print('SPECIAL_TOKEN:',
        '{',
        sep = '\n')

  for nome_lista, lista in listas_de_tokens_especiais.items():
    if nome_lista != "Comentários":
      continue

    print(f'  /** {nome_lista} */')

    for nome_token, valor_token in lista.items():
        print(f'  < {adaptar(nome_token)}: {valor_token} >',
              '}\n\n',
              sep = '\n')

# Implementação da função de início.
print(f'''\
void Inicio():
{{
  Token t;
}}
{{
  (\
''')

for nome_lista, lista in listas_de_tokens_normais.items():
  for token in lista:
    print(f'    t = < {adaptar(token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(token)} " + t.image);',
          f'    }}',
          f'',
          f'    |',
          f'',
          sep = '\n')

for dados_estado in estados_lexicos.values():
  # Se 'TOKEN' não existir, se trata de comentário marcado para não ser printado
  if 'TOKEN' not in dados_estado:
    continue

  print(f'''    t = < {adaptar(dados_estado[token_kind][0])} >''',
        f'''    {{''',
        f'''      System.out.println("{adaptar(dados_estado[token_kind][0])} " + t.image);''',
        f'''    }}''',
        f'''''',
        f'''    |''',
        f'''''',
        sep = '\n')

for nome_lista, lista in listas_de_tokens_especiais.items():
  if comentario_como_token == False and nome_lista == 'Comentários':
    continue

  for nome_token, valor_token in lista.items():
    if eh_token_final(nome_token) == False:
      continue

    print(f'    t = < {adaptar(nome_token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(nome_token)} " + t.image);',
          f'    }}',
          sep = '\n')

    if nome_token != ultimo_token_da_ultima_lista:
      print(f'',
            f'    |',
            f'',
            sep = '\n')

print(f'''\
  )*

  < EOF >
}}\
''')