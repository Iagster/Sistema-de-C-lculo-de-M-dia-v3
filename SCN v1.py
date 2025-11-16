print("=== SISTEMA DE CÁLCULO DE NOTA ===\n")

while True:
    #1
    nome = input("Digite o nome do aluno: ")

    #2
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    #3
    media = (nota1 + nota2 + nota3) / 3

    #4
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Resultado: Aprovado")
    elif media >= 5:
        print("Resultado: Recuperação")
    else:
        print("Resultado: Reprovado")

    #5
    repetir = input("\nDeseja calcular a média de outro aluno? (s/n): ")

    if repetir == "n":
        print("\nSistema encerrado.")
        break

    print()





