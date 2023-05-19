class literal:
    def __new__(self, valor) -> str:
        return str(valor)

class inteiro:
    def __new__(self, valor) -> int:
        return int(valor)

class flutuante:
    def __new__(self, valor) -> float:
        return float(valor)

class complexo:
    def __new__(self, real, imaginario=None) -> complex:
        if imaginario is None:
            return complex(real)
        else:
            return complex(real, imaginario)

class booleano:
    def __new__(self, valor) -> bool:
        return bool(valor)

class lista:
    def __new__(self, *valor) -> list:
        return list(*valor)

class conjunto:
    def __new__(self, valor) -> set:
        return set(valor)

class dicionario:
    def __new__(self, **valor) -> dict:
        return dict(valor)

class tupla:
    def __new__(self, valor) -> tuple:
        return tuple(valor)

