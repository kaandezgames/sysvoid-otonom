import streamlit as st
import random

st.set_page_config(page_title="SysVoid // Otonom Sokak İzleme", layout="wide")

st.markdown("""
<style>
.stApp {background-color: #000; color: #00ff41; font-family: 'Courier New';}
.stMetric {background-color: #0a0a0a; border: 1px solid #00ff41; padding: 10px; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ SYSVOID // SOKAK BAZLI ATIK OTOMASYONU")

# Detaylı Veri Yapısı
def get_detailed_data(sokak):
    durumlar = ["SAĞLIKLI", "BAKIM GEREKİYOR", "KRİTİK HATA", "ÇEVRİMDIŞI"]
    return {
        "Konum": f"{sokak} No: 42",
        "Pet": random.randint(0, 100),
        "Cam": random.randint(0, 100),
        "Teneke": random.randint(0, 100),
        "Sira": random.randint(0, 15),
        "Saglik": random.choice(durumlar),
        "Ping": f"{random.randint(20, 120)}ms"
    }

col1, col2 = st.columns([1, 3])
with col1:
    il = st.text_input("Şehir", "Ankara")
    ilce = st.text_input("İlçe", "Çankaya")
    sokak = st.text_input("Sokak/Cadde", "Atatürk Bulvarı")
with col2:
    if st.button(">>> SOKAK TARAMASINI BAŞLAT"):
        data = get_detailed_data(sokak)
        
        st.subheader(f"📍 Konum: {data['Konum']}")
        
        # Sağlık Durumu Göstergesi
        c1, c2 = st.columns(2)
        c1.metric("SAĞLIK DURUMU", data['Saglik'])
        c2.metric("BAĞLANTI GECİKMESİ", data['Ping'])
        
        st.write("---")
        
        # Atık Dolulukları
        col_p, col_c, col_t = st.columns(3)
        col_p.metric("PET ŞİŞE", f"%{data['Pet']}")
        col_c.metric("CAM", f"%{data['Cam']}")
        col_t.metric("TENEKE", f"%{data['Teneke']}")
        
        st.write(f"👥 **Sırada Bekleyen:** {data['Sira']} kişi")
        
        # Otonom Karar Mekanizması
        if data['Saglik'] != "SAĞLIKLI":
            st.error(f"⚠️ SİSTEM UYARISI: Makine {data['Saglik']} modunda. Otomatik servis kaydı oluşturuldu.")
        else:
            st.success("✅ Tüm sistemler stabil, veriler canlı aktarılıyor.")
