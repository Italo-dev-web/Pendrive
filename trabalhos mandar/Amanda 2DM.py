import numpy as np
pais = np.array(["Nova Zelândia", "África do Sul", "Albânia", "Alemanha", "Andorra"])
area = np.array([268021, 1219090, 28748, 357022, 468])
população = np.array([5100000, 60000000, 2900000, 83870000, 79000])

dp = população / area
print ("a densidade populacional é igual a: ",dp)

imad= np.argmax(dp)
imed= np.argmin(dp)
print("pais com maior densidade demografica:  ",pais[imad])
print("pais com menos densidade demografica:   ",pais[imed])

media_densidade= np.mean(dp)
print(" a media de densidade populacional é igual a: ",media_densidade)
acima_media = pais[dp > media_densidade]

print("os paises acima da media são",(acima_media))

crescimento = população * 1.1
print(" a população futura de cada pais com um crescimento de 10% : {}",crescimento)

areatotal = area.sum()
poptotal = população.sum()
print("area total dos paises: ",areatotal)
print("população total dos paises: ",poptotal)