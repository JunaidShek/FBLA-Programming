"""
App Settings Page - Controls Light/Dark Mode Theme and Background Audio Playback.
"""

import streamlit as st
st.set_page_config(layout="wide")

st.title("⚙️ App Preferences & Settings")
st.write("Manage your display theme and background audio settings below:")

# Initialize theme and audio toggle states if not already set
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "music_muted" not in st.session_state:
    st.session_state.music_muted = False

with st.container(border=True):
    st.subheader("Theme Settings")
    
    # Toggle Dark Mode theme preference
    dark_toggle = st.toggle("Enable Dark Mode Theme", value=st.session_state.dark_mode)
    if dark_toggle != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_toggle
        st.rerun()  # Instant refresh to apply styling changes
        
    if st.session_state.dark_mode:
        st.info("Dark Mode is currently **Active**.")
    else:
        st.success("Light Mode is currently **Active**.")

with st.container(border=True):
    st.subheader("Audio Controls")
    
    # Toggle background music mute setting
    music_toggle = st.toggle("Mute Background Music", value=st.session_state.music_muted)
    if music_toggle != st.session_state.music_muted:
        st.session_state.music_muted = music_toggle
        st.rerun()  # Instant rerun to update audio playback state
        
    if st.session_state.music_muted:
        st.warning("🔇 Background music is currently **Muted**.")
    else:
        st.success("🔊 Background music is currently **Playing**.")