import streamlit as st
import random

st.set_page_config(page_title="SysVoid // Otonom Takip", layout="wide")

st.markdown("""
<style>
.stApp {background-color: #050505; color: #00FF00;}
[data-testid="stMetricValue"] {color: #00FF00;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ SYSVOID // KONUM BAZLI ATIK YÖNETİMİ")

# Konum bazlı makine veritabanı simülasyonu
def get_location_data(ilce, mahalle):
    # Bu kısım gerçek veritabanına bağlandığında o mahalleye özel verileri çekecek
    return [
        {"Konum": f"{mahalle} / Meydan", "Pet": random.randint(0, 100), "Cam": random.randint(0, 100), "Teneke": random.randint(0, 100), "Sira": random.randint(0, 10)},
        {"Konum": f"{mahalle} / Park Yanı", "Pet": random.randint(0, 100), "Cam": random.randint(0, 100), "Teneke": random.randint(0, 100), "Sira": random.randint(0, 20)}
    ]

# Girdi Alanları
col1, col2, col3 = st.columns(3)
with col1: il = st.text_input("Şehir", "Ankara")
with col2: ilce = st.text_input("İlçe", "Çankaya")
with col3: mahalle = st.text_input("Mahalle/Semt", "Kızılay")

if st.button(">>> KONUMU TARA"):
    st.subheader(f"📍 {mahalle} Bölgesi Aktif Makineler")
    
    makineler = get_location_data(ilce, mahalle)
    
    for m in makineler:
        with st.expander(f"KONUM: {m['Konum']}", expanded=True):
            c1, c2, c3 = st.columns(3)
            c1.metric("PET ŞİŞE", f"%{m['Pet']}")
            c2.metric("CAM", f"%{m['Cam']}")
            c3.metric("TENEKE", f"%{m['Teneke']}")
            
            st.write(f"👥 **Sıradaki Kişi Sayısı:** {m['Sira']}")
            
            # Doluluk uyarısı
            if m['Pet'] > 90 or m['Cam'] > 90 or m['Teneke'] > 90:
                st.error("⚠️ KRİTİK: Haznelerden biri dolmak üzere! Müdahale gerekiyor.")
            else:
                st.success("✅ Sistem stabil, kapasite uygun.")
