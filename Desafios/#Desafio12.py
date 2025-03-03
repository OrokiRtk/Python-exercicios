#calcule área de uma parede
largura = int(input("Diga a largura da parede: "))
altura = int(input("Diga a altura da parede: "))
area = (largura*altura)
quantidadeDeTinta = 2
totalTinta = (area/quantidadeDeTinta)
print(f"A área da parede é {(area)}M e será necessário {(totalTinta)}L de tinta.")