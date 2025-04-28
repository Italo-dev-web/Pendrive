#aula 10
from random import randint
from time import sleep
while True:
    numero= randint(0,5)
    pergunta= int(input("qual numero de 0 a 5 eu pensei??: "))
    if pergunta == numero:
        print("PARABENS!!! VOCE ACERTOU!!")
    else:
        print("você errou, deixe para a proxima...")
    print("recomeçando")
    for i in range (1,4):
        print (i)
        sleep(1)