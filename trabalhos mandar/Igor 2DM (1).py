import numpy as np
pais = np.array(["Iêmen", "Itália", "Irlanda", "Ilhas Marshall", "Israel"])
area = np.array([527970 ,301340 ,70280, 37548, 22145])
população = np.array ([40500000, 58800000 ,54360000, 100000, 10024000])

dp = população / area
print ("a densidade populacional é igual a: ",dp)

imad= np.argmax(dp)
imed= np.argmin(dp)
print("pais com maior densidade demografica:  {}".format(pais[imad]))
print("pais com menos densidade demografica:  {} ".format(pais[imed]))

media_densidade= np.mean(dp)
print(" a media de densidade populacional é igual a: ",media_densidade)
acima_media = pais[dp > media_densidade]

print("os paises acima da media são",(acima_media))

crescimento = população * 1.1
print(" a população futura de cada pais com um crescimento de 10% : {}",crescimento)

areatotal = area.sum()
poptotal = população.sum()
print("area total dos paises: {}".format(areatotal))
print("população total dos paises: {}".format(poptotal))