#calcular desconto
preco = float(input("Digite o preço do produto: "))
desconto = preco*(5/100)
total = (preco-desconto)
print(f"O preço do produto é R${(preco)} e o seu desconto é de: R${(desconto)}\n O total é de: R${(total)}")