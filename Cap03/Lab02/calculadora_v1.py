# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o numero da operacao desejada: \n")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

op = float(input("Digite sua opcao (1/2/3/4): "))

if (op != 1 and op != 2 and op != 3 and op != 4):
    print("Opcao invalida!")

else:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))

    if op == 1:
        print("\n",n1," + ",n2," = ",n1+n2)
    elif op == 2:
        print("\n",n1," - ",n2," = ",n1-n2)
    elif op == 3:
        print("\n",n1," * ",n2," = ",n1*n2)
    elif op == 4:
        print("\n",n1," / ",n2," = ",n1/n2)

