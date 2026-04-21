import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Pour toi", page_icon="✨", layout="centered")

# --- STYLE PERSONNALISÉ (ÉPURÉ, TEXTE GÉANT, PETITES PHOTOS) ---
st.markdown("""
    <style>
    .main { background-color: #fff9fb; }
    .stButton>button { 
        border-radius: 30px; 
        border: 1px solid #ff4b4b; 
        background-color: white; 
        color: #ff4b4b; 
        font-weight: bold; 
        width: 100%;
    }
    .stButton>button:hover { 
        background-color: #ff4b4b; color: white; 
    }
    .poeme { 
        font-style: italic; 
        text-align: center; 
        font-size: 2rem; /* Texte encore plus grand */
        font-weight: bold;
        color: #333;
        line-height: 1.5;
        padding: 30px 10px;
    }
    /* Centrer et réduire la taille de l'image à 50% */
    [data-testid="stImage"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 50%; /* Image plus petite pour laisser place au texte */
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialisation des variables de session
if 'connecte' not in st.session_state:
    st.session_state['connecte'] = False
if 'diapo_index' not in st.session_state:
    st.session_state['diapo_index'] = 0

# --- STRUCTURE DES 3 DIAPOS ---
diapos = [
    {
        "image": "photo1.JPG", 
        "legende": "Nour, tu es la femme de ma vie. <br>Tu es la lumière qui m'éclaire des ténèbres. <br>Chaque moment avec toi me console des souffrances de ma vie."
    },
    {
        "image": "photo2.JPG",
        "legende": "Nour, pour moi tu es un cadeau et une bénédiction de Dieu. <br>Jamais je ne me lasserai de ta présence car tu es une partie de moi <br>et tu es ma seule source de bonheur."
    },
    {
        "image": "photo3.JPG",
        "legende": "Je te serai loyal jusqu'à mon dernier souffle et je ferai <br>tout ce qui est en mon possible pour te protéger, te chérir et te conseiller. <br>Tu es la prunelle de mes yeux, ma muse et ma confidente."
    }
]

# --- ECRAN D'ACCÈS ---
if not st.session_state['connecte']:
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>🔐 Accès réservé</h2>", unsafe_allow_html=True)
    
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        reponse = st.text_input("C'est quoi le prénom de mon colloc ?", placeholder="...")
        valider = st.button("Valider")

    if valider:
        if reponse.strip().lower() == "youssef":
            st.session_state['connecte'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("Réessaie... ❌")

# --- ESPACE SANS SALUTATIONS ---
else:
    index = st.session_state['diapo_index']
    current = diapos[index]
    
    # Affichage de la photo (plus petite)
    try:
        st.image(current["image"])
    except:
        st.info(f"📸 Image '{current['image']}' manquante")
    
    # Texte poétique (Très grand et bien visible)
    st.markdown(f'<p class="poeme">"{current["legende"]}"</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    # Navigation
    c1, c2, c3 = st.columns([2, 1, 2])
    with c1:
        if st.button("⬅️", disabled=(index == 0)):
            st.session_state['diapo_index'] -= 1
            st.rerun()
    with c2:
        st.markdown(f"<p style='text-align:center; font-weight:bold; margin-top:10px;'>{index + 1}/3</p>", unsafe_allow_html=True)
    with c3:
        if st.button("➡️", disabled=(index == len(diapos) - 1)):
            st.session_state['diapo_index'] += 1
            st.rerun()

    if st.sidebar.button("Déconnexion"):
        st.session_state['connecte'] = False
        st.session_state

