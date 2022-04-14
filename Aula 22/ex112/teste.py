from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
a = int(input('Aumento %'))
r = int(input('Redução %'))
moeda.resumo(p, a, r)