from pitonbr.importador import importe
from pitonbr.importador import de
from pitonbr.escritor import limpe_tela
from pitonbr.escritor import escreva_e_pule_linha

limpe_tela()

numpy = importe("numpy")
escreva_e_pule_linha(numpy)

DataFrame, Series = de("pandas").importe("DataFrame", "Series")
escreva_e_pule_linha(DataFrame)
escreva_e_pule_linha(Series)

int()
