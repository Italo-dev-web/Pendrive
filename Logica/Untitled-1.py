x = input("Nome o usuario ")
print("ola Seja bem vindo".lower(),x.upper())

z = int(input("informe sua idade "))
if z >= 18:
    print("Parabens voce .")
else:
    print("infelizmente voce nao tem permissão paar obter CNH.")

while True:
    user_input = input ("")
    if user_input.lower() == 'nao':
        print("orbigado até a proxima")
        break
    else:
        print(" ")