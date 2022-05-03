""" Kütüphaneler """
import pandas as pd
import matplotlib.pyplot as plt


""" pandas kütüphanesi ile yapılan analizler """
df = pd.read_csv('data.csv')
#df.head()
#print(df)
countrys = df.value_counts('origin_country')
#print(countrys)
liste = list(countrys)
#print(liste)


""" matplotlip kütüphanesi ile yapılabilecek grafikler """
plt.ylabel("Havadaki Uçak Sayısı")
plt.xlabel("Ülkeler")
plt.xticks(countrys, rotation='vertical', size=8)
plt.plot(liste, 'go-')
plt.show()








