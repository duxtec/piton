from pitonbr.ledor import leia
from pitonbr.escritor import escreva
from pitonbr.escritor import limpe_tela

limpe_tela()

a = leia("Digite algo:")

escreva("Você digitou:")
escreva(a)
