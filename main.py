import os

mensagem = "Bem-vindo à locadora de carros!"
divisoria = len(mensagem)*"="

def limpar_tela():
    """Usar "clear" para o Linux e "cls" para o Windows"""
    os.system("clear")

carros = [("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 90),
          ("Chevrolet Spin", 150),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Moni", 70),
          ("Fiat Pulse", 130)]

alugados = []

def exibir_lista_de_carros(lista_de_carros):
    """Recebe a lista carros ou alugados, formata e exibe"""
    for i, car in enumerate(lista_de_carros):
        # À seguir, car[0] é o nome do carro e car[1] o preço para alugar.
        print("[{}] {} - R$ {}/dia.".format(i, car[0], car[1]))
        
exibir_lista_de_carros(carros)

while True:
    limpar_tela()
    print(divisoria)
    print(mensagem)
    print(divisoria)
    print("O que deseja fazer?")
    print("0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro")
    resposta = int(input())

    limpar_tela()
    if resposta == 0:
        exibir_lista_de_carros(carros)
    elif resposta == 1:
        exibir_lista_de_carros(carros)
        print(divisoria)
        print("Escolha o código do carro")
        codigo = int(input())
        print("Por quantos dias você deseja alugar esse carro?")
        dias = int(input())
        limpar_tela()

        print("Você escolheu o carro {} por {} dias.".format(carros[codigo][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[codigo][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns! Você alugou o {} por {} dias.".format(carros[codigo][0], dias))
            alugados.append(carros.pop(codigo)) # .append() recebe o retorno de .pop()
        
    elif resposta == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            exibir_lista_de_carros(alugados)
            print("\nEscolha o código do carro que deseja devolver:")
            codigo = int(input())
            if codigo == 0:
                print("Obrigado por devolver o carro {}".format(alugados[codigo][0]))
                carros.append(alugados.pop(codigo))

    print()
    print(divisoria)
    print("Digite 0 para CONTINUAR | Digite 1 para SAIR")
    if int(input()) == 1:
        break
