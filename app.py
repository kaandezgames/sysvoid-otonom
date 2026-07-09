import streamlit as st

st.set_page_config(page_title="SysVoid // TR Ağ Tarayıcı", layout="wide")

st.title("⚡ SYSVOID // TÜRKİYE GENELİ ATIK AĞI")

# OTONOM OKUYUCU MOTORU (Şehir/İlçe/Mahalle hiyerarşisi)
def turkiye_ag_oku(sehir, ilce, mahalle):
    # Otonom Mimar'ın genişletilmiş veri ağı
    ag = {
        "ankara": {
            "cankaya": {
                "fatih": {"pet": 45, "cam": 88, "teneke": 12, "sira": 0, "durum": "SAĞLIKLI"},
                "kızılay": {"pet": 92, "cam": 5, "teneke": 70, "sira": 15, "durum": "BAKIM GEREKİYOR"}
            }
        }
    }
    
    # Kademeli Okuma
    try:
        return ag[sehir.lower()][ilce.lower()][mahalle.lower()]
    except:
        return None

# Arayüz
col1, col2, col3 = st.columns(3)
with col1: sehir = st.text_input("Şehir:")
with col2: ilce = st.text_input("İlçe:")
with col3: mahalle = st.text_input("Mahalle:")

if st.button(">>> AĞI TARA"):
    sonuc = turkiye_ag_oku(sehir, ilce, mahalle)
    
    if sonuc:
        st.subheader(f"📍 {sehir.upper()} / {ilce.upper()} / {mahalle.upper()}")
        
        # Okuyucu Paneli
        c1, c2, c3 = st.columns(3)
        c1.metric("PET", f"%{sonuc['pet']}")
        c2.metric("CAM", f"%{sonuc['cam']}")
        c3.metric("TENEKE", f"%{sonuc['teneke']}")
        
        st.metric("SAĞLIK DURUMU", sonuc['durum'])
        st.write(f"👥 Sırada: {'Sıra Yok' if sonuc['sira'] == 0 else str(sonuc['sira'])+' Kişi'}")
    else:
        st.error("Ağda bu lokasyon bulunamadı. (Test için: Ankara / Cankaya / Fatih)")
