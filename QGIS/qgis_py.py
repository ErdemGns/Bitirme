""" Kütüphaneler """
import pandas as pd
import matplotlib.pyplot as plt


""" pandas kütüphanesi ile yapılan analizler """
df = pd.read_csv('data.csv') 
#df.head()
#print(df)
liste = list(countrys)
#print(liste)
countrys = df.value_counts('origin_country')
#print(countrys)
countrys_source = dict(countrys)
#print(countrys_source)


""" matplotlip kütüphanesi ile yapılabilecek grafikler """
plt.ylabel("Havadaki Uçak Sayısı")
plt.xlabel("Ülkeler")
plt.xticks(rotation='vertical', size=8)
plt.plot(countrys, 'o-')
plt.show()


    


