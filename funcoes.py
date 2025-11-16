def ler_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    return [nota1, nota2, nota3]


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {situacao}")
