def cabecalho():
    """
    Função para formatar um cabeçalho para o programa.
    :return: string
    """
    texto = "Weather around World - Using API by OpenWeather"
    print(f'{"=" * len(texto) + 10 * "="}')
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f"++++ {texto} ++++")
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f'{"=" * len(texto) + 10 * "="}')


def kelvin_para_celsius(temperatura_kelvin):
    """
    - Função para converter temperatura de Kelvin para Celsius.
    - Formula: (Kelvin) - 273.15
    :param temperatura_kelvin: Entrada, temperatura em Kelvin.
    :return: Retorna a temperatura em Celsius.
    """
    temperatura_celsius = temperatura_kelvin - 273.15
    return temperatura_celsius


def valida_saida():
    """
    Função para verificar se o usuário deseja continuar executando
    o programa.
    :return: Entrada do usuário.
    """

    while True:
        continuar = input("\nDeseja realizar outra pesquisa? [S/N]: ")
        if continuar.lower() == 's':
            break

        elif continuar.lower() == 'n':
            print("Encerrando o programa...")
            print("Obrigado, até a próxima!!!")
            exit(0)

        else:
            print('OOOPS! Digite "S" para SIM ou "N" para NÃO.')
            continue
