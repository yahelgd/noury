import numpy as np
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour Nour ❤️", page_icon="✨", layout="centered")

# Style pour une interface élégante et centrée
st.markdown("""
    <style>
    .main { background-color: #fff9fb; }
    .stButton>button { border-radius: 30px; border: 1px solid #ff4b4b; background-color: white; }
    .stButton>button:hover { background-color: #ff4b4b; color: white; }
    .poeme { 
        font-style: italic; 
        text-align: center; 
        font-size: 1.4rem; 
        color: #444;
        line-height: 1.6;
        padding: 20px;
    }
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_index=True)

# Initialisation des sessions
if 'connecte' not in st.session_state:
    st.session_state['connecte'] = False
if 'diapo_index' not in st.session_state:
    st.session_state['diapo_index'] = 0

# --- Structure des 3 Diapos ---
diapos = [
    {
        "image": "photo1.jpg",
        "legende": """Nour, tu es la femme de ma vie. <br>
        Tu es la lumière qui m'éclaire des ténèbres. <br>
        Chaque moment avec toi me console des souffrances de ma vie."""
    },
    {
        "image": "photo2.jpg",
        "legende": """Nour, pour moi tu es un cadeau et une bénédiction de Dieu. <br>
        Jamais je ne me lasserai de ta présence car tu es une partie de moi <br>
        et tu es ma seule source de bonheur."""
    },
    {
        "image": "photo3.jpg",
        "legende": """Je te serai loyal jusqu'à mon dernier souffle et je ferai <br>
        tout ce qui est en mon possible pour te protéger, te chérir et te conseiller. <br>
        Tu es la prunelle de mes yeux, ma muse et ma confidente."""
    }
]

# --- LOGIN (AUTHENTIFICATION) ---
if not st.session_state['connecte']:
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>🔐 Accès réservé</h2>", unsafe_allow_index=True)
    st.write("")

    # Champ centré
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        reponse = st.text_input("C'est quoi le prénom de mon colloc ?", placeholder="Tape ici...")
        valider = st.button("Valider l'accès", use_container_width=True)

    if valider:
        if reponse.strip().lower() == "youssef":
            st.session_state['connecte'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("Ce n'est pas la bonne réponse... ❌")

# --- ESPACE NOUR ---
else:
    st.markdown("<h1 style='text-align: center;'>Bonjour Nour ❤️</h1>", unsafe_allow_index=True)

    index = st.session_state['diapo_index']
    current = diapos[index]

    # Affichage de l'image (sans titre)
    try:
        st.image(current["image"], use_container_width=True)
    except:
        st.info(f"📸 (Place ton fichier '{current['image']}' ici)")

    # Texte poétique (HTML pour gérer les retours à la ligne <br>)
    st.markdown(f'<p class="poeme">"{current["legende"]}"</p>', unsafe_allow_index=True)

    st.write("---")

    # Navigation simplifiée
    c1, c2, c3 = st.columns([2, 1, 2])
    with c1:
        if st.button("⬅️ Précédent", disabled=(index == 0), use_container_width=True):
            st.session_state['diapo_index'] -= 1
            st.rerun()
    with c2:
        st.markdown(f"<p style='text-align:center; padding-top:10px;'>{index + 1}/3</p>", unsafe_allow_index=True)
    with c3:
        if st.button("Suivant ➡️", disabled=(index == len(diapos) - 1), use_container_width=True):
            st.session_state['diapo_index'] += 1
            st.rerun()

    # Sidebar discrète pour quitter
    if st.sidebar.button("Déconnexion"):
        st.session_state['connecte'] = False
        st.session_state['diapo_index'] = 0
        st.rerun()

