import streamlit as st

st.set_page_config(page_title="SysVoid // Veri Yönetim", layout="wide")

# Sistem Hafızası (Rastgele değil, kayıtlı veri)
if 'makine_verisi' not in st.session_state:
    st.session_state.makine_verisi = {
        "durum": "SAĞLIKLI",
        "pet": 0,
        "cam": 0,
        "teneke": 0,
        "sira": 0
    }

st.title("⚡ SYSVOID // MANUEL VERİ GİRİŞİ")

# Veri Girişleri
col1, col2 = st.columns(2)
with col1:
    st.subheader("Makine Durumunu Güncelle")
    st.session_state.makine_verisi["pet"] = st.number_input("Pet Doluluk (%)", 0, 100)
    st.session_state.makine_verisi["cam"] = st.number_input("Cam Doluluk (%)", 0, 100)
    st.session_state.makine_verisi["teneke"] = st.number_input("Teneke Doluluk (%)", 0, 100)
    st.session_state.makine_verisi["sira"] = st.number_input("Sırada Bekleyen", 0, 50)

# Dashboard (Sadece senin girdiğin veriyi gösterir)
with col2:
    st.subheader("CANLI PANEL")
    st.metric("SAĞLIK DURUMU", st.session_state.makine_verisi["durum"])
    
    c1, c2, c3 = st.columns(3)
    c1.metric("PET", f"%{st.session_state.makine_verisi['pet']}")
    c2.metric("CAM", f"%{st.session_state.makine_verisi['cam']}")
    c3.metric("TENEKE", f"%{st.session_state.makine_verisi['teneke']}")
    
    sira_yazisi = "Sıra Yok" if st.session_state.makine_verisi["sira"] == 0 else f"{st.session_state.makine_verisi['sira']} Kişi"
    st.metric("SIRADAKİ KİŞİ", sira_yazisi)
