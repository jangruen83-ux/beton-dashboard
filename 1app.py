import streamlit as st
import requests

# 🌆 Layout
st.set_page_config(page_title="Beton Dashboard", layout="wide")

# 🎨 Design
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1581092160607-ee22621dd758");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.card {
    background-color: rgba(0,0,0,0.7);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin: 10px;
    color: white;
}

div.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 18px;
    border-radius: 12px;
}

h1, h2 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 🏗️ Titel
st.title("🏗️ Beton-Instandsetzung")

# 📱 Auswahlbereich
col1, col2 = st.columns(2)

# Zustand speichern (welcher Bereich aktiv ist)
if "mode" not in st.session_state:
    st.session_state.mode = "home"

with col1:
    if st.button("🔍 Schadensanalyse"):
        st.session_state.mode = "analyse"

with col2:
    if st.button("📊 Projektübersicht"):
        st.session_state.mode = "projekt"

# =========================
# 🤖 KI SCHADENSANALYSE
# =========================

if st.session_state.mode == "analyse":
    st.header("🔍 KI-Schadensanalyse")

    user_input = st.text_area(
        "Beschreibe den Schaden:",
        placeholder="z.B. Risse in Stütze, Bewehrung sichtbar, Feuchtigkeit vorhanden..."
    )

    if st.button("Analyse starten"):
        if user_input:

            with st.spinner("KI analysiert..."):

                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": "llama3",
                            "prompt": f"""
Du bist Experte für Betoninstandsetzung.

Analysiere folgenden Schaden fachlich:

{user_input}

Gib strukturiert aus:
1. Schadensart
2. Ursache
3. Dringlichkeit (hoch/mittel/niedrig)
4. Sanierungsempfehlung
""",
                            "stream": False
                        },
                        timeout=60
                    )

                    result = response.json()

                    st.success("Analyse abgeschlossen ✅")
                    st.write(result["response"])

                except:
                    st.error("⚠️ Ollama läuft nicht! Bitte lokal starten.")

# =========================
# 📊 PROJEKTÜBERSICHT
# =========================

if st.session_state.mode == "projekt":
    st.header("📊 Projektübersicht")

    st.info("Hier kommen später deine Projektdaten rein 📈")

# =========================
# 🏠 HOME
# =========================

if st.session_state.mode == "home":
    st.write("Wähle eine Funktion oben 👆")
