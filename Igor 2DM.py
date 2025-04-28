import numpy as np
from time import sleep
pais = np.array(["Iêmen", "Itália", "Irlanda", "Ilhas Marshall", "Israel"])
area = np.array([527970 ,301340 ,70280, 37548, 22145])
população = np.array ([40500000, 58800000 ,54360000, 100000, 10024000])

dp = população / area
print ("a densidade populacional é igual a: ",dp)
sleep(1)

imad= np.argmax(dp)
imed= np.argmin(dp)
print("pais com maior densidade demografica:  {}".format(pais[imad]))
sleep(1)
print("pais com menos densidade demografica:  {} ".format(pais[imed]))
sleep(1)
media_densidade= np.mean(dp)
print(" a media de densidade populacional é igual a: ",media_densidade)
sleep(1)
acima_media = pais[dp > media_densidade]

print("os paises acima da media são",(acima_media))
sleep(1)
crescimento = população * 1.1
print(" a população futura de cada pais com um crescimento de 10% : ",crescimento)
sleep(1)
areatotal = area.sum()
poptotal = população.sum()
print("area total dos paises: {}".format(areatotal))
print("população total dos paises: {}".format(poptotal))