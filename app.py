,import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="SysVoid // Otonom Ağ", layout="wide")

# Dosya okuma yok, veri kodun içinde (File Not Found hatası bitti)
csv_data = """Sehir,Ilce,Mahalle,Pet,Cam,Teneke,Durum
Ankara,Sincan,Fatih,45,88,12,SAĞLIKLI
Ankara,Sincan,Törekent,10,5,2,SAĞLIKLI
Ankara,Çankaya,Kızılay,92,50,70,BAKIM GEREKİYOR
Ankara,Etimesgut,Bağlıca,30,40,50,SAĞLIKLI
Ankara,Yenimahalle,Demetevler,60,60,60,SAĞLIKLI"""

df = pd.read_csv(io.StringIO(csv_data))

st.title("⚡ SYSVOID // TÜRKİYE VERİ AĞI")

sehir = st.selectbox("Şehir:", df['Sehir'].unique())
ilce = st.selectbox("İlçe:", df[df['Sehir'] == sehir]['Ilce'].unique())
mahalle = st.selectbox("Mahalle:", df[df['Ilce'] == ilce]['Mahalle'].unique())

if st.button(">>> AĞI TARA"):
    sonuc = df[(df['Sehir'] == sehir) & (df['Ilce'] == ilce) & (df['Mahalle'] == mahalle)].iloc[0]
    st.subheader(f"📍 {mahalle.upper()} // ANLIK VERİ")
    c1, c2, c3 = st.columns(3)
    c1.metric("PET", f"%{sonuc['Pet']}")
    c2.metric("CAM", f"%{sonuc['Cam']}")
    c3.metric("TENEKE", f"%{sonuc['Teneke']}")
    st.metric("SAĞLIK", sonuc['Durum'])
