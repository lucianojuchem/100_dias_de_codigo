
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Digite um número para ver sua tabuada: "))

tabuada(numero)