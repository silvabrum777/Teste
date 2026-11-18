def celsius_para_fahrenheit(c):
    """
    Converte uma temperatura de Celsius para Fahrenheit.


    Parâmetro:
        c (float): Temperatura em graus Celsius.


    Retorno:
        float: Temperatura em graus Fahrenheit.
    """
    return (c * 9/5) + 32




def km_para_milhas(km):
    """
    Converte quilômetros para milhas.


    Parâmetro:
        km (float): Distância em quilômetros.


    Retorno:
        float: Distância em milhas.
    """
    return km * 0.621371




def kg_para_libras(kg):
    """
    Converte quilogramas para libras.


    Parâmetro:
        kg (float): Peso em quilogramas.


    Retorno:
        float: Peso em libras.
    """
    return kg * 2.20462




def menu():
    """
    Exibe o menu principal e permite escolher
    qual conversão será realizada.
    """


    while True:
        print("\n===== CONVERSOR DE UNIDADES =====")
        print("1 - Celsius para Fahrenheit")
        print("2 - Quilômetros para Milhas")
        print("3 - Quilogramas para Libras")
        print("0 - Sair")


        opcao = input("\nEscolha uma opção: ")


        if opcao == "1":
            try:
                c = float(input("Digite a temperatura em Celsius: "))
                resultado = celsius_para_fahrenheit(c)
                print(f"Resultado: {resultado:.2f} °F")
            except ValueError:
                print("Erro! Digite um número válido.")


        elif opcao == "2":
            try:
                km = float(input("Digite a distância em quilômetros: "))
                resultado = km_para_milhas(km)
                print(f"Resultado: {resultado:.2f} milhas")
            except ValueError:
                print("Erro! Digite um número válido.")


        elif opcao == "3":
            try:
                kg = float(input("Digite o peso em quilogramas: "))
                resultado = kg_para_libras(kg)
                print(f"Resultado: {resultado:.2f} libras")
            except ValueError:
                print("Erro! Digite um número válido.")


        elif opcao == "0":
            print("\nPrograma encerrado. Obrigado por utilizar!")
            break


        else:
            print("\nOpção inválida! Tente novamente.")




# Inicia o programa
if __name__ == "__main__":
    menu()