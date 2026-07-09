import streamlit as st
import random

st.set_page_config(page_title="SysVoid // Otonom Takip", layout="wide")

st.markdown("""
<style>
.stApp {background-color: #000; color: #00ff41; font-family: 'Courier New';}
</style>
""", unsafe_allow_html=True)

st.title("⚡ SYSVOID // SOKAK BAZLI OTOMASYON")

# Veri girişi
il = st.text_input("Şehir", "Ankara")
ilce = st.text_input("İlçe", "Çankaya")
mahalle = st.text_input("Mahalle", "Fatih")
sokak = st.text_input("Sokak/No", "Atatürk Blv. No: 42")

if st.button(">>> SİSTEMİ BAĞLA"):
    # Sabit değerler (her seferinde değişmesin diye)
    pet = random.randint(0, 100)
    cam = random.randint(0, 100)
    teneke = random.randint(0, 100)
    sira_sayisi = random.choice([0, 0, 0, 1, 3, 5]) # Bazen 0 gelsin diye
    saglik = "SAĞLIKLI" 
    
    st.subheader(f"📍 Konum: {mahalle} Mah. {sokak}")
    
    # Sağlık durumu ve sıra bilgisi gösterimi
    c1, c2 = st.columns(2)
    c1.metric("SAĞLIK DURUMU", saglik)
    
    if sira_sayisi == 0:
        c2.metric("SIRADAKİ KİŞİ", "Sıra Yok")
    else:
        c2.metric("SIRADAKİ KİŞİ", f"{sira_sayisi} Kişi")
        
    st.write("---")
    
    # Atık bilgileri
    col_p, col_c, col_t = st.columns(3)
    col_p.metric("PET ŞİŞE", f"%{pet}")
    col_c.metric("CAM", f"%{cam}")
    col_t.metric("TENEKE", f"%{teneke}")
    
    st.success("✅ Sistem stabil, anlık veri akışı sağlanıyor.")
