import os
import re
from pitonbr.conversor import literal
from pitonbr.tipo import tipo

def escreva(dado=""):
    if tipo(dado) == "literal":
        pass
    
    elif tipo(dado) == "sem tipo":
        dado = "Nenhum"
        
    else:
        dado = literal(dado)
        
        dado = dado.replace("function", "função")
        padrao = r'(função )([^ ]+)'
        dado = re.sub(padrao, r"\1'\2'", dado)
        
        dado = dado.replace("class", "classe")
        
        dado = dado.replace("object", "objeto") 
        padrao = r'<([^ ]+) (objeto)'
        dado = re.sub(padrao, r"<\2 '\1'", dado)
        
        dado = dado.replace("module", "módulo")
        
        dado = dado.replace(" at ", "no endereço de memória")
        dado = dado.replace("from", "localizado em")
    
    return print(dado)

def escreva_e_pule_linha(valor=""):
    retorno = escreva(valor)
    pule_linha()

    return retorno

def pule_linha(linhas=1):
    for linha in range(linhas):
        retorno = escreva("")

    return retorno

def limpe_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')