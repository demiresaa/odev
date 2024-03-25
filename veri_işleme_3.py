
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('C:/Users/nesli/Desktop/veri_tabani.csv', encoding='ISO-8859-1')


veriler
veriler.sample(19)    


verilers=veriler.dropna()
verilers




indirgenmis_salon_listesi = []
salon_isimleri = set()

for index, row in verilers.iterrows():
    if row['spor_salonu_ismi'] not in salon_isimleri:
        salon_isimleri.add(row['spor_salonu_ismi'])
        indirgenmis_salon_listesi.append(row.to_dict())

# indirgenmis_salon_listesi şu anda bir liste, her elemanı bir satırın sözlük temsilini içerir
# Eğer bir DataFrame olarak kullanmak istiyorsanız:
indirgenmis_salon_df = pd.DataFrame(indirgenmis_salon_listesi)

        
        
donusmus_veri_a = []

for i in indirgenmis_salon_df['fiyat_bilgisi_a']:
    if isinstance(i, (float, int)):  # Kontrol ekleyerek float veya int tipinde mi kontrol ediyoruz
        donusmus_veri_a.append(i)

donusmus_veri_a.sort()  # Sıralamayı burada yapın
print(donusmus_veri_a)

donusmus_veri_y = []

for i in indirgenmis_salon_df['fiyat_bilgisi_y']:
    if isinstance(i, (float, int)):  # Kontrol ekleyerek float veya int tipinde mi kontrol ediyoruz
        donusmus_veri_y.append(i)
        

donusmus_veri_y.sort()  # Sıralamayı burada yapın
print(donusmus_veri_y)

fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_goster = donusmus_veri_a[0]
fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_gosterr = donusmus_veri_a[12]

fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_goster 
fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_gosterr 

ali=fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_goster , fiyat_en_uygun_ve_en_pahalı_spor_salon_fiyati_gosterr
ali


