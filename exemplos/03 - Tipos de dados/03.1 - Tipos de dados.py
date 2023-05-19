from pitonbr.tipo import tipo
from pitonbr.tipo import Nenhum
from pitonbr.escritor import escreva
from pitonbr.escritor import pule_linha
from pitonbr.repetidor import repita
from pitonbr.escritor import limpe_tela
import pitonbr

limpe_tela()

a = "1"
b = 1
c = 1.0
d = 1 + 0j
e = True
f = [1]
g = {1}
h = {1: "1"}
i = (1, 2)
j = tipo
k = repita
l = repita()
m = pitonbr
n = Nenhum


escreva(a)
escreva(f"é do tipo: {tipo(a)}")
pule_linha()

escreva(b)
escreva(f"é do tipo: {tipo(b)}")
pule_linha()

escreva(c)
escreva(f"é do tipo: {tipo(c)}")
pule_linha()

escreva(d)
escreva(f"é do tipo: {tipo(d)}")
pule_linha()

escreva(e)
escreva(f"é do tipo: {tipo(e)}")
pule_linha()

escreva(f)
escreva(f"é do tipo: {tipo(f)}")
pule_linha()

escreva(g)
escreva(f"é do tipo: {tipo(g)}")
pule_linha()

escreva(h)
escreva(f"é do tipo: {tipo(h)}")
pule_linha()

escreva(i)
escreva(f"é do tipo: {tipo(i)}")
pule_linha()

escreva(j)
escreva(f"é do tipo: {tipo(j)}")
pule_linha()

escreva(k)
escreva(f"é do tipo: {tipo(k)}")
pule_linha()

escreva(l)
escreva(f"é do tipo: {tipo(l)}")
pule_linha()

escreva(m)
escreva(f"é do tipo: {tipo(m)}")
pule_linha()

escreva(n)
escreva(f"é do tipo: {tipo(n)}")
pule_linha()
