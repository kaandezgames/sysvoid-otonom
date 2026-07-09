import streamlit as st
import pandas as pd

st.set_page_config(page_title="SysVoid // Otonom Kontrol", layout="wide")

# Google Sheets'ten veriyi otomatik çeken Otonom Motor
def get_live_data():
    # Buraya kendi oluşturduğun Google Sheets dosyasının linkini yapıştıracaksın
    sheet_url = "SENİN_GOOGLE_SHEETS_LİNKİN" 
    return pd.read_csv(sheet_url)

st.title("⚡ SYSVOID // OTONOM SİSTEM AĞI")

if st.button(">>> SİSTEMİ TARA VE OTOMATİK GÜNCELLE"):
    try:
        df = get_live_data()
        st.table(df) # Tüm makinelerin anlık durumu burada görünecek
        st.success("Sistem Otonom Olarak Güncellendi.")
    except:
        st.warning("Veri kaynağına bağlanılamadı. Sheets dosyanı 'Herkese Açık' yapmayı unutma!")
