#aula 10 pt 2

while True:
    
    dist = float(input("qual a distancia da viagem??: "))
    if dist <= 200 :
        preço1 = dist * 0.45
        print("a viagem custara {} por KM".format(preço1))
    else:
        preço2 = dist * 0.50
        print("a viagem custara {} por KM!!".format(preço2))
        
