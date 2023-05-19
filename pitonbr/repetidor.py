from pitonbr import ValorIncorreto
from pitonbr import escreva
from pitonbr import tipo
from pitonbr.erro import TipoIncorreto


class repita:
    def __init__(self, execução=False):
        if execução:
            self.execução = execução

    def de(self, início):
        self.início = início
        return self

    def até(self, término):
        self.término = término
        if hasattr(self, 'execução'):
            return self.faça(self.execução)
        else:
            return self

    def passo(self, n):
        self.n = n

    def faça(self, execução=escreva, retorno="repetições"):

        self.início = self.início if hasattr(self, 'início') else 0
        self.término = self.término if hasattr(self, 'término') else 1
        if hasattr(self, 'n'):
            passo = self.n
        else:
            passo = 1 if self.início <= self.término else -1

        repetições = 0
        retornos_execução = []

        atual = self.início

        if passo == 0:
            raise ValorIncorreto("Erro ao executar, passo não pode ser zero.")

        if self.início == self.término:
            raise ValorIncorreto(
                "Erro ao executar, início da repetição não pode ser igual ao término.")

        if (self.início < self.término and passo <= 0):
            raise ValorIncorreto(
                "Erro ao executar, se o início for menor que o término o passo deve ser maior que zero.")

        if (self.início > self.término and passo >= 0):
            raise ValorIncorreto(
                "Erro ao executar, se o início for maior que o término o passo deve ser menor que zero.")

        if passo > 0:
            alcançou = atual > self.término

        if passo < 0:
            alcançou = atual < self.término

        while not alcançou:
            retornos_execução.append(execução(atual))
            atual += passo
            repetições += 1

            if passo > 0:
                alcançou = atual > self.término

            if passo < 0:
                alcançou = atual < self.término

        if retorno == "último":
            return retornos_execução[-1]
        elif retorno == "todos":
            return retornos_execução
        else:
            return repetições


class enquanto:
    def __init__(self, condição):
        if callable(condição):  # Verifica se a variável é uma função
            self.condição = condição
        else:
            raise TipoIncorreto("Condição deve ser uma função.")

    def faça(self, execução=escreva, retorno="repetições"):
        repetições = 0
        retornos_execução = []

        while self.condição():
            repetições += 1
            retornos_execução.append(execução())

        if retorno == "último":
            return retornos_execução[-1]
        elif retorno == "todos":
            return retornos_execução
        else:
            return repetições
