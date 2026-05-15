import streamlit as st

st.title("Beton-Instandsetzung Dashboard")

st.write("Willkommen zur Analyse von Betonschäden 👷‍♂️")

st.header("Beispiel Daten")

st.write({
    "Projekt": ["Brücke A", "Parkhaus B", "Tunnel C"],
    "Schäden": [12, 7, 3]
})
