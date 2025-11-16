from funcoes import ler_notas, calcular_media, verificar_situacao, mostrar_resultado

print("=== SISTEMA DE CÁLCULO DE MÉDIA — v3 ===\n")

alunos = []

while True:
    nome = input("Digite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    mostrar_resultado(nome, media, situacao)


    alunos.append({
        "nome": nome,
        "media": media,
        "situacao": situacao
    })

    repetir = input("\nDeseja calcular a média de outro aluno? (s/n): ")
    if repetir == "n":
        break

    print()



