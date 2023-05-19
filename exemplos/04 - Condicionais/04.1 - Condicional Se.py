from pitonbr.condicionador import se
from pitonbr.ledor import leia
from pitonbr.escritor import escreva
from pitonbr.tipo import tipo
from pitonbr.conversor import inteiro
from pitonbr.escritor import limpe_tela
from pitonbr.escritor import pule_linha
from datetime import date

limpe_tela();
diaDaSemana = date.today().weekday()

escreva('Demonstração 1 - "Se" executando funções.')
se(diaDaSemana > 4, lambda: escreva("Bom final de semana!"))

#
pule_linha()
#

escreva('Demonstração 2 - "Se" / "Senão" executando funções.')
número = inteiro(leia("Digite um número:"))
se(número%2 == 0, (lambda: escreva("O número é par!")))\
.senão((lambda: escreva("O número é impar!")))\

#
pule_linha()
#

escreva('Demonstração 3 - "Se" / "Senão Se" / "Senão" executando funções.')
temperatura = inteiro(leia("Digite a temperatura:"))

se(temperatura < 20,
    lambda: escreva("A temperatura está fria!")
)\
.senão_se(temperatura > 30,
    lambda: escreva("A temperatura está quente!")
)\
.senão(
    lambda: escreva("A temperatura está agradável!")
)

#
pule_linha()
#

escreva('Demonstração 4 - "Se" / "Senão Se" / "Senão" com retorno.')
número = inteiro(leia("Digite um número:"))
resultado = se(número > 0, "positivo").senão_se(número < 0, "negativo").senão("zero")
escreva(f"O número é {resultado}")