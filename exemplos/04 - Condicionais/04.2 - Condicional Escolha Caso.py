from pitonbr import limpe_tela
from pitonbr.condicionador import escolha
from datetime import date

limpe_tela()

diaDaSemana = date.today().weekday()

dia = escolha(diaDaSemana)\
.caso(0, "Segunda-feira")\
.caso(1, "Terça-feira")\
.caso(2, "Quarta-feira")\
.caso(3, "Quinta-feira")\
.caso(4, "Sexta-feira")\
.caso(5, "Sábado")\
.caso(6, "Domingo")\
.padrão("Dia inválido")

print(f"Hoje é {dia}")
