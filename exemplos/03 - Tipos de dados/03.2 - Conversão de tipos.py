from pitonbr.conversor import literal
from pitonbr.conversor import inteiro
from pitonbr.conversor import literal
from pitonbr.conversor import flutuante
from pitonbr.conversor import literal
from pitonbr.conversor import complexo
from pitonbr.conversor import booleano
from pitonbr.conversor import lista
from pitonbr.conversor import conjunto
from pitonbr.conversor import dicionario
from pitonbr.conversor import tupla

from pitonbr.escritor import limpe_tela

limpe_tela()

a = "7"

print(literal(a))
print(inteiro(a))
print(flutuante(a))
print(complexo(a))
print(booleano(a))
print(lista(a))
print(conjunto(a))
print(dicionario(a=a))
print(tupla(a))
