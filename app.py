import streamlit as st
import requests

# Bu fonksiyon, makinenin içindeki sensörden "çekme" yapar
def makine_verisi_cek(makine_ip):
    try:
        # Gerçek makine protokolü (API endpoint)
        response = requests.get(f"http://{makine_ip}/api/status", timeout=2)
        return response.json()
    except:
        return {"hata": "Makineyle bağlantı koptu veya IP yanlış"}

st.title("⚡ SYSVOID // PROFESYONEL VERİ HATTI")

ip = st.text_input("Makine IP Adresi:", "192.168.1.50")

if st.button(">>> SENSÖR VERİSİNİ ÇEK"):
    data = makine_verisi_cek(ip)
    if "hata" in data:
        st.error(data["hata"])
    else:
        st.write("Veri akışı başarılı:", data)
