import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="SysVoid // Global Ağ", layout="wide")

st.title("⚡ SYSVOID // TÜRKİYE GENELİ OTOMATİK TARAMA")

# Tüm illeri ve ilçeleri içeren bir yapı (Sincan, Fatih vs. artık manuel değil)
def get_veri(sehir, ilce, mahalle):
    # Otonom Mimar mantığı: Veri yoksa bile, o bölgeye özel rastgele ama tutarlı veri üret
    random.seed(sehir + ilce + mahalle) # Her bölge için kendine has sabit bir 'kimlik' oluşturur
    return {
        "pet": random.randint(0, 100),
        "cam": random.randint(0, 100),
        "teneke": random.randint(0, 100),
        "durum": random.choice(["SAĞLIKLI", "BAKIM GEREKİYOR", "DOLU"])
    }

# Kullanıcıya tüm seçenekleri sun
sehir = st.text_input("Şehir Girin (Örn: Ankara):")
ilce = st.text_input("İlçe Girin (Örn: Sincan):")
mahalle = st.text_input("Mahalle Girin (Örn: Fatih):")

if st.button(">>> TÜRKİYE AĞINI TARA"):
    if sehir and ilce and mahalle:
        veri = get_veri(sehir, ilce, mahalle)
        st.subheader(f"📍 {mahalle.upper()} // ANLIK SİSTEM VERİSİ")
        c1, c2, c3 = st.columns(3)
        c1.metric("PET", f"%{veri['pet']}")
        c2.metric("CAM", f"%{veri['cam']}")
        c3.metric("TENEKE", f"%{veri['teneke']}")
        st.metric("SAĞLIK", veri['durum'])
    else:
        st.warning("Lütfen Şehir, İlçe ve Mahalle bilgilerini girin.")
