import streamlit as st

st.set_page_config(page_title="SysVoid // Otonom Analiz", layout="wide")

st.title("⚡ SYSVOID // MERKEZİ ANALİZ PANELİ")

# Kuzeninin baktığı basit veri değil, biz "Anomali Tespiti" yapıyoruz
def analiz_et(pet, cam, teneke):
    # Makinenin verimlilik analizi (Profesyonel yaklaşım)
    toplam = pet + cam + teneke
    if toplam > 250:
        return "KRİTİK: Aşırı Yüklenme - Servis Şart"
    elif toplam < 50:
        return "DÜŞÜK VERİM: Kullanım Az"
    else:
        return "SİSTEM STABİL"

col1, col2, col3 = st.columns(3)
p = col1.slider("PET", 0, 100, 50)
c = col2.slider("CAM", 0, 100, 50)
t = col3.slider("TENEKE", 0, 100, 50)

st.write("---")
st.subheader(f"📊 Durum: {analiz_et(p, c, t)}")
