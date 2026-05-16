import streamlit as st
import requests
from PIL import Image

# =========================
# 📱 SEITE EINSTELLEN
# =========================
st.set_page_config(page_title="Schadensaufnahme", layout="centered")

# =========================
# 🎨 DESIGN
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #f5f5f5;
}

/* Karten */
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    border-radius: 12px;
}

/* Eingaben */
textarea, input {
    font-size: 16px !important;
}

/* Überschriften */
h1, h2, h3 {
    color: black;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 🏗️ TITEL
# =========================
st.title("🏗️ Digitale Schadensaufnahme")

# =========================
# 📱 NAVIGATION
# =========================
menu = st.radio("", ["➕ Neuer Schaden", "📄 Bericht"], horizontal=True)

if "bericht" not in st.session_state:
    st.session_state.bericht = ""

# =========================
# ➕ NEUER SCHADEN
# =========================
if menu == "➕ Neuer Schaden":

    st.info("""
📋 **Schadensaufnahme durchführen**

1. Projekt wählen  
2. Schaden beschreiben  
3. Foto hinzufügen (optional)  
4. Bericht automatisch erzeugen  
""")

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    projekt = st.text_input("📍 Projekt / Bauvorhaben")

    bauteil = st.selectbox(
        "🧱 Bauteil",
        ["Stütze", "Decke", "Wand", "Fundament", "Balkon", "Parkdeck"]
    )

    schaden = st.selectbox(
        "⚠️ Schadensart",
        ["Riss", "Abplatzung", "Korrosion", "Feuchte", "Undichtigkeit"]
    )

    beschreibung = st.text_area(
        "📝 Beschreibung",
        height=150
    )

    bild = st.file_uploader(
        "📸 Foto hochladen",
        type=["jpg", "png", "jpeg"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if bild:
        image = Image.open(bild)
        st.image(image, use_column_width=True)

    if st.button("🤖 Bericht erstellen"):

        if not beschreibung:
            st.warning("Bitte Beschreibung eingeben")
            st.stop()

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": f"""
Analysiere folgenden Betonschaden:

Projekt: {projekt}
Bauteil: {bauteil}
Schaden: {schaden}
Beschreibung: {beschreibung}

Gib aus:
- Bewertung
- Ursache
- Dringlichkeit
- Sanierungsvorschlag
""",
                    "stream": False
                },
                timeout=60
            )

            result = response.json()
            st.session_state.bericht = result["response"]

            st.success("✅ Bericht erstellt → Tab 'Bericht' wechseln")

        except:
            st.error("⚠️ Ollama läuft nicht")

# =========================
# 📄 BERICHT
# =========================
if menu == "📄 Bericht":

    if not st.session_state.bericht:
        st.info("Noch kein Bericht vorhanden")
    else:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write(st.session_state.bericht)

        text = st.session_state.bericht.lower()

        if "hoch" in text:
            st.error("🔴 Hohe Dringlichkeit")
        elif "mittel" in text:
            st.warning("🟡 Mittlere Dringlichkeit")
        else:
            st.success("🟢 Niedrig")

        st.markdown("</div>", unsafe_allow_html=True)
