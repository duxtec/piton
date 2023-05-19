class se():
    def __init__(self, condição, execução):
        self.condição = condição
        if self.condição:
            if callable(execução):
                self.retorno = execução()
            else:
                self.retorno = execução
      
    def senão_se(self, condição, execução):
        if not hasattr(self, "retorno"):
            self.condição = condição
            if self.condição:
                if callable(execução):
                    self.retorno = execução()
                else:
                    self.retorno = execução
        return self
        
    def senão(self, execução):
        if not hasattr(self, "retorno"):
            if callable(execução):
                self.retorno = execução()
            else:
                self.retorno = execução
                
        return self.retorno
                
    def retorne(self):
        if not hasattr(self, "retorno"):
            return self.retorno

class escolha():
    def __init__(self, variável):
        self.variável = variável
    
    def caso(self, valor, retorno):
        if not hasattr(self, "retorno"):
            if self.variável == valor:
                self.retorno = retorno
                
        return self
    
    def padrão(self, retorno):
        if not hasattr(self, "retorno"):
            self.retorno = retorno
            
        return self.retorno