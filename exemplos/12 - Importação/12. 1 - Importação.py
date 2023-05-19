from piton.importador import importe
from piton.importador import de
from piton.escritor import limpe_tela
from piton.escritor import escreva_e_pule_linha

limpe_tela()

numpy = importe("numpy")
escreva_e_pule_linha(numpy)

DataFrame, Series = de("pandas").importe("DataFrame", "Series")
escreva_e_pule_linha(DataFrame)
escreva_e_pule_linha(Series)

int()
