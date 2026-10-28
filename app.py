"""
Main Application Entry Point - Ammi's Chamcha Digital Ordering System
Handles page routing, global theme configurations, background audio, and store status tracking.
"""

import streamlit as st
import base64
from datetime import datetime, time

# Page setup configuration (Must be executed as the first Streamlit command)

st.set_page_config(layout="wide", page_title="Ammi's Chamcha - Digital Ordering System")

st.logo("assets/logo.png", size="large")

# Initialize global session state variables for audio and dark mode preferences
if "music_muted" not in st.session_state:
    st.session_state.music_muted = False

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def autoplay_audio(file_path: str):
    """Encodes and plays background audio using inline HTML5 unless muted by the user."""
    if st.session_state.music_muted:
        return
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
    except Exception:
        pass  # Gracefully ignore if audio file is missing

# Execute background audio playback check
autoplay_audio("assets/bgmusic.mp3")

# Apply dynamic CSS themes based on active Light or Dark Mode preference
if st.session_state.dark_mode:
    bg_gradient = "linear-gradient(135deg, #0B0E14 0%, #2A1A1E 100%)"
    sidebar_bg = "linear-gradient(180deg, #151821 0%, #241B20 100%)"
    
    # Enforce white text contrast in Dark Mode
    dark_mode_text_css = """
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, 
    .stApp p, .stApp span, .stApp label, .stApp markdown, 
    [data-testid="stMarkdownContainer"] p, [data-testid="stWidgetLabel"] label,
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }
    """
else:
    bg_gradient = "linear-gradient(135deg, #FFFDFB 0%, #F8D8C0 100%)"
    sidebar_bg = "linear-gradient(180deg, #FFFFFF 0%, #ECC5A8 100%)"
    dark_mode_text_css = ""

# Inject custom CSS styling
active_bg_color = '#3e404b' if st.session_state.dark_mode else '#E28B75'
active_text_color = '#FFFFFF' if not st.session_state.dark_mode else 'inherit'

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {bg_gradient} !important;
        background-attachment: fixed !important;
    }}
    {dark_mode_text_css}
    [data-testid="stSidebar"] {{
        background: {sidebar_bg} !important;
        border-right: 1px solid rgba(0, 0, 0, 0.15);
    }}
    [data-testid="stSidebarNav"] ul {{ padding: 10px; }}
    [data-testid="stSidebarNav"] li {{
        border-radius: 12px !important;
        margin-bottom: 6px;
        transition: all 0.3s ease;
    }}
    [data-testid="stSidebarNav"] li a {{
        border-radius: 12px !important;
        padding: 8px 12px !important;
    }}
    [data-testid="stSidebarNav"] li:has(a[aria-current="page"]) {{
        background-color: {active_bg_color} !important;
        color: {active_text_color} !important;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize global shared session state containers
if "cart" not in st.session_state:
    st.session_state.cart = []

if "account_data" not in st.session_state:
    st.session_state.account_data = {
        "email": "customer@example.com",
        "password": "••••••••••••",
        "address": "5010 Buckeystown Pike, Frederick, MD 21704"
    }

if "order_summary" not in st.session_state:
    st.session_state.order_summary = None

# Sidebar Store Operating Hours Widget with real-time break logic
with st.sidebar:
    now = datetime.now().time()
    lunch_start, lunch_end = time(11, 30), time(15, 0)
    dinner_start, dinner_end = time(17, 0), time(22, 0)
    
    sub_text = ""
    if lunch_start <= now <= lunch_end:
        status, delta_text, sub_text, color = "OPEN", "Open until 3:00 PM (Lunch)", "Opens again at 5:00 PM", "normal"
    elif dinner_start <= now <= dinner_end:
        status, delta_text, color = "OPEN", "Open until 10:00 PM (Dinner)", "normal"
    elif now < lunch_start:
        status, delta_text, color = "CLOSED", "Opens at 11:30 AM for Lunch", "inverse"
    elif lunch_end < now < dinner_start:
        status, delta_text, sub_text, color = "CLOSED", "Closed for afternoon break", "Reopens at 5:00 PM", "inverse"
    else:
        status, delta_text, sub_text, color = "CLOSED", "Closed for the night", "Opens tomorrow at 11:30 AM", "inverse"
        
    st.metric(label="Store Status", value=status, delta=delta_text, delta_color=color)
    
    if sub_text:
        st.caption(sub_text)
        
    st.markdown("---")

# Multi-page directory navigation mapping
pages = {
    "Welcome": [
        st.Page("home.py", title="Restaurant Home")
    ],
    "Our Restaurant Menu": [
        st.Page("menu.py", title="Menu")
    ],
    "Your Orders": [
        st.Page("cart.py", title="View Cart"),
        st.Page("buy.py", title="Checkout"),
        st.Page("history.py", title="Order History")
    ],
    "Support Desk": [
        st.Page("chat.py", title="Help Desk"),
        st.Page("help.py", title="Email Support")
    ],
    "User Preferences": [
        st.Page("settings.py", title="App Settings"),
        st.Page("account.py", title="Manage My Account")
    ]
}

pg = st.navigation(pages)
pg.run()