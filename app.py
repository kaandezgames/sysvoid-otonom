import streamlit as st
import random
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="SysVoid // DİM Yönetim Ağı", layout="wide")

# Hacker/Otonom Arayüz Stili
st.markdown("""
<style>
.main {background-color: #000000;}
h1, h2, h3 {color: #00FF00; font-family: 'Courier New';}
.stMetric {background-color: #111; padding: 15px; border-radius: 10px; border: 1px solid #00FF00;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ SYSVOID // MERKEZİ DİM YÖNETİM AĞI")

# Konum ve Makine Veritabanı (Simülasyon)
def generate_live_data(sehir, ilce):
    return [
        {"ID": f"{ilce.upper()}-001", "Durum": "AÇIK", "Doluluk": random.randint(10, 95), "Sira": random.randint(0, 15)},
        {"ID": f"{ilce.upper()}-002", "Durum": "MOLA", "Doluluk": random.randint(50, 99), "Sira": 0},
        {"ID": f"{ilce.upper()}-003", "Durum": "ARIZALI", "Doluluk": 100, "Sira": 0},
    ]

# Arama Paneli
col1, col2 = st.columns(2)
with col1:
    sehir = st.text_input("Şehir Gir:", "Ankara")
with col2:
    ilce = st.text_input("İlçe Gir:", "Çankaya")

if st.button(">>> SİSTEMİ TARA VE BAĞLAN"):
    st.success(f"{sehir}/{ilce} ağındaki üniteler başarıyla tarandı.")
    
    makineler = generate_live_data(sehir, ilce)
    
    for m in makineler:
        with st.container():
            col_a, col_b, col_c = st.columns(3)
            
            # Durum Rengi
            color = "green" if m['Durum'] == "AÇIK" else "red" if m['Durum'] == "ARIZALI" else "orange"
            
            col_a.subheader(f"Unit: {m['ID']}")
            col_b.metric("Doluluk", f"%{m['Doluluk']}")
            col_c.metric("Sıra", f"{m['Sira']} Kişi")
            
            st.markdown(f"**Durum:** :{color}[{m['Durum']}]")
            st.progress(m['Doluluk'] / 100)
            st.write("---")

st.sidebar.title("SİSTEM LOGLARI")
st.sidebar.code("System Online\nAuto-Update: ON\nNetwork: SECURE")
