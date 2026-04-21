import streamlit as st

# --- CONFIGURATION DE LA PAGE (Ligne 8 corrigée) ---
st.set_page_config(page_title="Pour Nour ❤️", page_icon="✨", layout="centered")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #fff9fb; }
    .stButton>button { border-radius: 30px; border: 1px solid #ff4b4b; background-color: white; color: #ff4b4b; font-weight: bold; }
    .stButton>button:hover { background-color: #ff4b4b; color: white; }
    .poeme { 
        font-style: italic; 
        text-align: center; 
        font-size: 1.4rem; 
        color: #444;
        line-height: 1.6;
        padding: 20px;
    }
    /* Centrer l'image */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_index=True)

# Initialisation des variables de session
if 'connecte' not in st.session_state:
    st.session_state['connecte'] = False
if 'diapo_index' not in st.session_state:
    st.session_state['diapo_index'] = 0

# --- STRUCTURE DES 3 DIAPOS ---
diapos = [
    {
        "image": "photo1.jpg", 
        "legende": "Nour, tu es la femme de ma vie. <br>Tu es la lumière qui m'éclaire des ténèbres. <br>Chaque moment avec toi me console des souffrances de ma vie."
    },
    {
        "image": "photo2.jpg",
        "legende": "Nour, pour moi tu es un cadeau et une bénédiction de Dieu. <br>Jamais je ne me lasserai de ta présence car tu es une partie de moi <br>et tu es ma seule source de bonheur."
    },
    {
        "image": "photo3.jpg",
        "legende": "Je te serai loyal jusqu'à mon dernier souffle et je ferai <br>tout ce qui est en mon possible pour te protéger, te chérir et te conseiller. <br>Tu es la prunelle de mes yeux, ma muse et ma confidente."
    }
]

# --- ECRAN D'ACCÈS (AUTHENTIFICATION) ---
if not st.session_state['connecte']:
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>🔐 Accès réservé</h2>", unsafe_allow_index=True)
    st.write("")
    
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        reponse = st.text_input("C'est quoi le prénom de mon colloc ?", placeholder="Ton texte ici...")
        valider = st.button("Valider l'accès", use_container_width=True)

    if valider:
        if reponse.strip().lower() == "youssef":
            st.session_state['connecte'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("Mauvaise réponse... Réessaie mon cœur. ❌")

# --- ESPACE NOUR (UNE FOIS CONNECTÉ) ---
else:
    st.markdown("<h1 style='text-align: center;'>Bonjour Nour ❤️</h1>", unsafe_allow_index=True)
    
    index = st.session_state['diapo_index']
    current = diapos[index]
    
    # Affichage de la photo
    try:
        # Note : use_container_width remplace use_column_width dans les versions récentes
        st.image(current["image"], use_container_width=True)
    except:
        st.info(f"📸 (L'image '{current['image']}' doit être dans le dossier sur GitHub)")
    
    # Texte poétique
    st.markdown(f'<p class="poeme">"{current["legende"]}"</p>', unsafe_allow_index=True)
    
    st.write("---")
    
    # Navigation entre les diapos
    c1, c2, c3 = st.columns([2, 1, 2])
    with c1:
        if st.button("⬅️ Précédent", disabled=(index == 0), use_container_width=True):
            st.session_state['diapo_index'] -= 1
            st.rerun()
    with c2:
        st.markdown(f"<p style='text-align:center; font-weight:bold;'>{index + 1} / 3</p>", unsafe_allow_index=True)
    with c3:
        if st.button("Suivant ➡️", disabled=(index == len(diapos) - 1), use_container_width=True):
            st.session_state['diapo_index'] += 1
            st.rerun()

    # Petit bouton discret en bas pour se déconnecter
    st.write("")
    if st.sidebar.button("Se déconnecter"):
        st.session_state['connecte'] = False
        st.session_state['diapo_index'] = 0
        st.rerun()

