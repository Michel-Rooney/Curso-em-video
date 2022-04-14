#2012

times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo", "Corinthians", "Internacional", "Cruzeiro", "São Paulo", "Atlético Mineiro", "Botafogo", "Fluminense", "Coritiba", "Bahia", "Goiás", "Guarani", "Sport", "Portuguesa", "Atlético Paranaense", "Vitória" )

print('-='*30)
print(f'Os times são {times}')
print('-='*30)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-='*30)
print(f'Os 4 ultimos times são {times[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabetica são {sorted(times)}')
print('-='*30)
print(f'Corinthians está na {times.index("Corinthians")+1}ª posição')