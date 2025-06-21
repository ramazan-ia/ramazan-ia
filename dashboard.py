
import streamlit as st
import time
import random

# Configuration de la page
st.set_page_config(page_title="Ramazan IA", page_icon="💸", layout="wide")

# Titre
st.title("📊 Dashboard Ramazan IA")
st.markdown("Bienvenue Ramazan 👑 Voici le suivi en temps réel de tes revenus passifs IA.")

# Objectif de revenus
OBJECTIF = 200000

# Simuler des revenus cumulés (en attendant données réelles)
revenus_simules = [0, 50, 120, 250, 500, 1000, 1800, 3000, 5000, 7000, 10000, 15000]
revenu_courant = revenus_simules[-1] + random.randint(10, 50)

# Affichage des compteurs
st.subheader("💰 Revenus cumulés")
st.metric(label="Total actuel", value=f"{revenu_courant:,} €")

progress = min(revenu_courant / OBJECTIF, 1.0)
st.progress(progress)

st.caption(f"Objectif fixé à {OBJECTIF:,} €")

# Suivi par branche (à connecter aux données IA réelles)
st.subheader("📦 Détail par branche")
branches = {
    "Instagram IA + POD": 1200,
    "Bot Trading IA (XAU/USD)": 600,
    "Formations IA": 350,
    "Affiliation Amazon/TikTok": 900,
}

for branche, montant in branches.items():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"🔹 {branche}")
    with col2:
        st.write(f"{montant} €")

# Placeholder pour les courbes RSI
st.subheader("📈 RSI - Bot Trading IA")
st.line_chart([random.randint(30, 70) for _ in range(30)])

# Notes
st.info("Les données sont actuellement simulées. Connexion aux flux réels en cours...")
