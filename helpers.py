def cabecalho():
    """
    Função para formatar um cabeçalho para o programa.
    :return: string
    """
    texto = "Weather around World - API by OpenWeather"
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f"++++ {texto} ++++")
    print(f'{"*" * len(texto) + 10 * "*"}')
