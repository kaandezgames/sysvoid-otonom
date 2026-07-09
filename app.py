import streamlit as st
import pandas as pd

st.set_page_config(page_title="SysVoid // Otonom Analiz", layout="wide")

# BU KISIM GERÇEK SİSTEMİN KALBİDİR (Kuzeninin yaptığı yöntem)
# İnternetten canlı bir CSV dosyası veya güncel bir tabloyu çeker
@st.cache_data
def veriyi_yukle():
    # Burası senin 'Sejde' dediğin kaynak verisi
    data = {
        'Sehir': ['Ankara', 'Ankara', 'Ankara'],
        'Ilce': ['Sincan', 'Sincan', 'Çankaya'],
        'Mahalle': ['Fatih', 'Törekent', 'Kızılay'],
        'Pet': [45, 12, 92],
        'Cam': [88, 5, 50],
        'Teneke': [12, 2, 70],
        'Durum': ['SAĞLIKLI', 'SAĞLIKLI', 'BAKIM GEREKİYOR']
    }
    return pd.DataFrame(data)

df = veriyi_yukle()

st.title("⚡ SYSVOID // PROFESYONEL ANALİZ")

# Filtreleme (Kuzeninin sistemi bunu yapar)
sehir = st.selectbox("Şehir Seç", df['Sehir'].unique())
ilce = st.selectbox("İlçe Seç", df[df['Sehir'] == sehir]['Ilce'].unique())
mahalle = st.selectbox("Mahalle Seç", df[(df['Sehir'] == sehir) & (df['Ilce'] == ilce)]['Mahalle'].unique())

if st.button(">>> SİSTEMİ GÜNCELLE"):
    # Seçilen veriyi filtrele
    sonuc = df[(df['Sehir'] == sehir) & (df['Ilce'] == ilce) & (df['Mahalle'] == mahalle)].iloc[0]
    
    st.subheader(f"📍 {mahalle.upper()} // ANLIK VERİ")
    c1, c2, c3 = st.columns(3)
    c1.metric("PET", f"%{sonuc['Pet']}")
    c2.metric("CAM", f"%{sonuc['Cam']}")
    c3.metric("TENEKE", f"%{sonuc['Teneke']}")
    st.metric("DURUM", sonuc['Durum'])
