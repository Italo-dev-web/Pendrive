import numpy as np
pais = np.array(["Argentina", "Bolívia", "Chile", "china", "Canadá"])
area = np.array([2736000 ,1098000 ,756180, 9596548, 9984005])
população = np.array ([45500000, 13800000 ,20360000, 1412000000, 39024000])

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