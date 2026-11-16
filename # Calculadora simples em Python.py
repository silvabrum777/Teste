# Calculadora simples em Python

print("Calculadora Simples")
print("Operações disponíveis: +, -, *, /")

num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Erro: divisão por zero!")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")