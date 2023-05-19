Nenhum = None

def tipo(var = Nenhum):
    switcher = {
        "str": "literal",
        "int": "inteiro",
        "float": "flutuante",
        "complex": "complexo",
        "bool": "booleano",
        "dict": "dicionário",
        "list": "lista",
        "tuple": "tupla",
        "set": "conjunto",
        "function": "função",
        "type": "classe",
        "module": "módulo",
        "NoneType": "sem tipo"
    }

    tipo = str(type(var)).replace("<class '", "").replace("'>", "")

    if "." in tipo:
        return f'objeto da classe {tipo.replace("__main__.", "")}'

    return switcher.get(tipo, tipo)
