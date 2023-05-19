from piton.ledor import leia
from piton.escritor import escreva
from piton.escritor import limpe_tela

limpe_tela()

a = leia("Digite algo:")

escreva("Você digitou:")
escreva(a)
