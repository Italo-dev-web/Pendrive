
print ("\033[30mdigite x para uma multiplicação \ndigite + para uma soma \ndigite - para uma subtração \ndigite / para uma divisão ")
oq= input("que tipo de conta voce deseja fazer??  ")
if oq == 'x':
        n1= int(input("coloque o primeiro numero: "))
        n2 = int(input("coloquue o segundo numero: "))
        x = n1 * n2
        print("a multiplicação de {} x {} é igual a {}".format(n1,n2,x))
elif oq == "+":
        n1 = int(input("primeiro numero: "))
        n2 = int(input("segundo numero: "))
        mais = n1 + n2
        print("a soma de {} mais {} é igual a {}".format(n1,n2,mais))
elif oq == "-":
        n1 = int(input("primeiro numero: "))
        n2 = int(input("segundo numero: "))
        sub = n1 - n2
        print("a subtração de {} menos {} é igual a {}".format ( n1,n2,sub))
elif oq == "/":
        n1 = int(input("primeiro numero: "))
        n2 = int(input("segundo numero: "))
        div = n1 / n2
        print("a divisão de {} dividido por {} é igual a {}".format(n1,n2,div))
else:
        print("\033[31m!! Operação Invalida !!")
print("|")
print("|")   