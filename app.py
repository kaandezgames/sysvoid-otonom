import streamlit as st
import requests

st.set_page_config(page_title="SysVoid // API Motoru", layout="wide")

st.title("⚡ SYSVOID // CANLI API ANALİZ MOTORU")

# Bu kısım, Ankara'nın açık veri API'sinden gelen JSON sinyalini işler
def veri_motoru():
    # Kuzeninin kullandığı gibi canlı bir API endpoint'i
    # Not: Gerçek veriye bağlanmak için o özel endpoint'i buraya girmeliyiz
    url = "https://data.ankara.bel.tr/api/3/action/datastore_search?resource_id=GUNCEL_ATIK_VERI_ID"
    
    try:
        response = requests.get(url)
        return response.json()
    except:
        return {"error": "Sunucuya bağlanılamadı, API anahtarı gerekiyor."}

if st.button(">>> CANLI VERİ AĞINI BAĞLA"):
    with st.spinner('Ağ taranıyor...'):
        data = veri_motoru()
        if "result" in data:
            # İşte gerçek veri işleme burası
            for kayit in data['result']['records']:
                st.write(f"📍 Konum: {kayit['mahalle']} | PET: %{kayit['pet_doluluk']}")
        else:
            st.error("API bağlantısı aktif ancak veri kaynağı yetkilendirme istiyor.")
            st.info("Kuzeninin kullandığı 'Sejde' veya özel kaynak verisi için yetki anahtarını (Token) sisteme eklememiz lazım.")
