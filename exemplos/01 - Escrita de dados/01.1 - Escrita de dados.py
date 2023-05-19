from piton.escritor import escreva
from piton.escritor import escreva_e_pule_linha
from piton.escritor import pule_linha
from piton.escritor import limpe_tela

limpe_tela()

escreva("Este texto não irá aparecer, porque a tela será limpa logo abaixo")

limpe_tela()

escreva("Escrita sem pular linha.")

escreva_e_pule_linha("Escrita pulando linha.")

escreva("Abaixo serão puladas 3 linhas.")

pule_linha(3)

escreva("Foram puladas 3 linhas.")
