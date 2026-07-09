import streamlit as st
import pandas as pd

st.set_page_config(page_title="SysVoid // Otonom Ağ", layout="wide")

@st.cache_data
def veriyi_yukle():
    # Buraya data.csv dosyasının olduğu linki veya yolu koy
    return pd.read_csv("data.csv") 

df = veriyi_yukle()

st.title("⚡ SYSVOID // TÜRKİYE VERİ AĞI")

# Dinamik Filtreleme (Sincan, Çankaya, Yenimahalle vs. hepsi buraya otomatik gelir)
sehir = st.selectbox("Şehir:", df['Sehir'].unique())
ilce = st.selectbox("İlçe:", df[df['Sehir'] == sehir]['Ilce'].unique())
mahalle = st.selectbox("Mahalle:", df[df['Ilce'] == ilce]['Mahalle'].unique())

if st.button(">>> AĞI TARA"):
    sonuc = df[(df['Sehir'] == sehir) & (df['Ilce'] == ilce) & (df['Mahalle'] == mahalle)].iloc[0]
    
    st.subheader(f"📍 {mahalle.upper()} // ANLIK SİSTEM VERİSİ")
    c1, c2, c3 = st.columns(3)
    c1.metric("PET", f"%{sonuc['Pet']}")
    c2.metric("CAM", f"%{sonuc['Cam']}")
    c3.metric("TENEKE", f"%{sonuc['Teneke']}")
    st.metric("SAĞLIK", sonuc['Durum'])
