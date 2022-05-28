""" Kütüphaneler """
import pandas as pd
import matplotlib.pyplot as plt

""" pandas kütüphanesi ile yapılan analizler """
df = pd.read_csv('data.csv')
countrys = df.value_counts('callsign') #origin_country
print(countrys)

""" matplotlip kütüphanesi ile yapılabilecek grafikler """
plt.ylabel("Havadaki Uçak Sayısı")
plt.xlabel("Ülkeler")
plt.xticks(rotation='vertical', size=8)
plt.plot(countrys, 'go-')
plt.show()