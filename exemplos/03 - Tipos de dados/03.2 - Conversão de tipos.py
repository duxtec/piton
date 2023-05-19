from piton.conversor import literal
from piton.conversor import inteiro
from piton.conversor import literal
from piton.conversor import flutuante
from piton.conversor import literal
from piton.conversor import complexo
from piton.conversor import booleano
from piton.conversor import lista
from piton.conversor import conjunto
from piton.conversor import dicionario
from piton.conversor import tupla

from piton.escritor import limpe_tela

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
