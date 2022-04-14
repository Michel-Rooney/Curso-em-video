def voto(ano):
    """
    --> Mostrara se você pode ou não votar:
        Ano: Será o ano de nascimento que o índiviudo passou na var(ano_nas)
    """


    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return(f'Você tem {idade} anos. Você não pode votar.')
    
    elif 16 <= idade < 18 or idade > 65:
        return(f'Você tem {idade} anos. Voto opcional.')
    
    else:
        return(f'Você tem {idade} anos. Voto Obrigatório.')


ano_nas = int(input('Em que ano você nasceu? '))
print(voto(ano_nas))
