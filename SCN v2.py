print("=== SISTEMA DE CÁLCULO DE NOTA v2 ===\n")

#1
def ler_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    return [nota1, nota2, nota3]

#2
def calcular_media(notas):
    return sum(notas) / len(notas)

#3
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

#4
def mostrar_resultado(nome, media, situacao):
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {situacao}")

while True:
    nome = input("Digite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    mostrar_resultado(nome, media, situacao)

    repetir = input("\nDeseja calcular a média de outro aluno? (s/n): ")
    if repetir == "n":
        print("\nSistema encerrado.")
        break

    print()
