from pitonbr.repetidor import enquanto
from pitonbr.escritor import escreva_e_pule_linha
from pitonbr.escritor import escreva
from pitonbr.escritor import pule_linha
from pitonbr.escritor import limpe_tela
from pitonbr.conversor import literal

limpe_tela()

escreva_e_pule_linha("Demonstração da repetição Enquanto")

def condição():
    número  = int(input("Digite um número par: "))
    return número % 2 != 0

def execução():
    return escreva_e_pule_linha("Você inseriu um número impar!")
    

loop = enquanto(condição).faça(execução)

escreva("Obrigado por inserir um número par.")