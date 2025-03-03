#Calcular salario
salarioBase = float(input("Digite o sálario do funcionario: "))
aumento = salarioBase*(15/100)
salarioFinal = (salarioBase + aumento)
print(f"O salário base é de: R${(salarioBase)},o aumento foi de R$+{(aumento)} e o salário final é de R${(salarioFinal)}")