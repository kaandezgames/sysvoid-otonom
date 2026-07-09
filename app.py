import streamlit as st
import random
import time

st.set_page_config(page_title="SysVoid // Otonom Kontrol", layout="wide")

st.markdown("""
<style>
.stApp {background-color: #050505; color: #00FF00;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ SYSVOID // OTONOM SİSTEM AĞI")

# Otonom Veri Motoru
if 'data' not in st.session_state:
    st.session_state.data = {
        "Fatih/No:42": {"Pet": 20, "Cam": 10, "Teneke": 5, "Sira": 0, "Durum": "SAĞLIKLI"},
        "Kızılay/Meydan": {"Pet": 85, "Cam": 90, "Teneke": 40, "Sira": 12, "Durum": "KRİTİK"}
    }

# Otomatik Tarama Butonu
if st.button(">>> SİSTEMİ OTONOM TARA"):
    with st.spinner('Ağ taranıyor...'):
        time.sleep(1) # Sistemin gerçek gibi çalışması için minik bir gecikme
        for konum, veri in st.session_state.data.items():
            st.subheader(f"📍 Konum: {konum}")
            c1, c2, c3 = st.columns(3)
            c1.metric("PET", f"%{veri['Pet']}")
            c2.metric("CAM", f"%{veri['Cam']}")
            c3.metric("TENEKE", f"%{veri['Teneke']}")
            
            durum_rengi = "green" if veri['Durum'] == "SAĞLIKLI" else "red"
            st.markdown(f"**Durum:** :{durum_rengi}[{veri['Durum']}] | **Sıra:** {'Sıra Yok' if veri['Sira']==0 else str(veri['Sira'])+' Kişi'}")
            st.write("---")
