def adicao(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calcular():
    print("Selecione a operação: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

while True:
    funcao = input("Escolha 1,2,3,4: ")

    if funcao in ('1','2','3','4'):
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        if funcao == '1':
             print('Resultado: ', adicao(num1,num2))
        if funcao == '2':
             print('Resultado: ', subtracao(num1,num2))
        if funcao == '3':
             print('Resultado: ', multiplicacao(num1,num2))
        if funcao == '4':
            if num2 != 0:
                  print('Resultado: ', divisao(num1,num2))
            else:
             print("Divisão por 0 é inválida!")
    else:
        print("Escolha inválida")
    continuar = input("Deseja continuar calculando? (s/n)")
    if continuar == 'n':
        print("Calculadora Encerrada")
        break
    
    calcular()