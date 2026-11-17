notas = [float(input(f"Digite a {i}ª nota: ")) for i in range(1, 5)]
media = sum(notas) / 4


print(f"Média: {media:.2f}")


if media > 7:
    print("Aprovado")
elif media > 5:
    print("Em recuperação")
else:
    print("Reprovado")