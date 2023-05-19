def importe(modulo):
    return (__import__(modulo))


class de:

    def __init__(self, origem):
        self.origem = origem

    def importe(self, *modulos):
        modulos = list(modulos)
        self.modulos = modulos

        de = __import__(f'{self.origem}', fromlist=[])
        return_list = []

        for modulo in self.modulos:
            return_list.append(getattr(de, modulo))

        return return_list
