:: Programa

@echo off

echo __GERADOR_LEXICO__
python gerador_lexico.py > Compilador.jj

call run_javacc.bat

echo __JAVAC__
javac *.java