#Mostrar quantos dolares dá pra comprar
print("Compre dolar aqui: ----->")
money = float(input('Digite a quantia que você tem: '))
converter = money/5.8
print(f"Você tem uma quantia de R${(money)} e você pode comprar {(converter):.2f} em dólares. ")