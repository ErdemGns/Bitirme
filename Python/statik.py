""" Kütüphaneler """
import requests
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.tile_providers import get_provider, OSM
from bokeh.io import show, curdoc, output_notebook

""" Kodun Notebook üzerinde çıktı vermesi için """
output_notebook()

""" Gelen coğrafi koordinatları web mercator dönüştür """
def wgs84_to_web_mercator(df, lon="long", lat="lat"):
    k = 6378137
    df["MercatorX"] = df[lon] * (k * np.pi/180.0)
    df["MercatorY"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df


""" Türkiye'yi içine alan coğrafi koordinatlar """
lon_min,lat_min = 25, 35
lon_max,lat_max = 45, 45
""" REST API üzerinden veri çekmek için gerekli argümanlar """
user_name = ''
password = ''
url_data = 'https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)


""" REST API üzerinden istekte bulun """
response = requests.get(url_data).json()
#print(response)
#print(type(response))
""" Gelen verinin sutün ismi """
col_name = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity','true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']
""" Verileri DataFrame tipine çevir """
flight_df = pd.DataFrame(response['states'])
#print(flight_df)
#print(type(flight_df))
""" Sutün isimlerini numaralandır """
flight_df = flight_df.loc[:,0:16]
#print(flight_df)
#print(type(flight_df))
""" Sutün numaraları yerine col_name kısmındaki isimlendirmeleri ile değiştir """
flight_df.columns = col_name
#print(flight_df.columns)
#print(type(flight_df.columns))
""" NAN tipinde gelen boş alanları hata almamak amaçlı No Data yap flight_df"""
flight_df = flight_df.fillna('No Data') #replace NAN with No Data
#print(flight)
#print(type(flight))

""" Fonsiyonu çağır """
wgs84_to_web_mercator(flight_df)
flight_df['rot_angle'] = flight_df['true_track']*-1
icon_url = 'https://cdn-icons-png.flaticon.com/512/1679/1679938.png'
flight_df['url'] = icon_url



""" Nerelere şekil çizileceğine dair bilgileri gir """
p = figure(plot_width=900, plot_height=700, x_range=(3000000, 5000000), y_range=(3500000, 6000000),
           x_axis_type="mercator", y_axis_type="mercator", tooltips=[("Ülke", "@origin_country"), 
            ("Uçak Adı", "@callsign"), ("(Long, Lat)", "(@long, @lat)")], title = "Anlık Uçak Konumları")


""" Harita altlığını çağır """
tile_provider = get_provider(OSM)
""" Karanlık mod ekle """
curdoc().theme = 'dark_minimal'
""" Harita altlığını p şekilleri ile birleştir """
p.add_tile(tile_provider)


""" Uçak figürlerini çizdir """
p.image_url(url='url', x='MercatorX', y='MercatorY', source=flight_df, anchor='center', angle_units='deg', angle='rot_angle', h_units='screen', w_units='screen', w=25, h=25)


""" Çizilecek şekilleri ayarla """
p.circle(x="MercatorX", y="MercatorY", size=7, fill_color="red", line_color="black", fill_alpha=1, source=flight_df)


""" Haritayı göster """
show(p)

output_file(filename="statik.html", title="Static HTML file")
save(p)

