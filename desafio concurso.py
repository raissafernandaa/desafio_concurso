quantidade_pessoas = int(input("Qual a quantidade de pessoas? "))

nomes = []
notas_etapa1 = []
notas_etapa2 = []
medias = []

for i in range(quantidade_pessoas):
    nome = input(f"Digite os dados da {i+1}a pessoa:\nNome: ")
    nota_etapa1 = float(input("Nota etapa 1: "))
    nota_etapa2 = float(input("Nota etapa 2: "))

    nomes.append(nome)
    notas_etapa1.append(nota_etapa1)
    notas_etapa2.append(nota_etapa2)
    medias.append((nota_etapa1 + nota_etapa2) / 2)

print("TABELA:")
for i in range(quantidade_pessoas):
    print(f"{nomes[i]}, {notas_etapa1[i]}, {notas_etapa2[i]}, MEDIA = {medias[i]:.2f}")

aprovados = []
for i in range(quantidade_pessoas):
    if medias[i] >= 70:
        aprovados.append(nomes[i])

print("PESSOAS APROVADAS:")
if len(aprovados) == 0:
    print("Não há candidatos aprovados")
else:
    for nome in aprovados:
        print(nome)

porcentagem_aprovacao = len(aprovados) / quantidade_pessoas * 100
print(f"Porcentagem de aprovação: {porcentagem_aprovacao:.1f} %")

maior_media = nomes[medias.index(max(medias))]
print(f"Maior média: {maior_media}")

notas_aprovados = [medias[i] for i in range(quantidade_pessoas) if medias[i] >= 70]
if len(notas_aprovados) == 0:
    print("Nota média dos aprovados: Não há candidatos aprovados")
else:
    media_aprovados = sum(notas_aprovados) / len(notas_aprovados)
    print(f"Nota média dos aprovados: {media_aprovados:.2f}")
