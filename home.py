import streamlit as st

# Force the layout to span the entire width of the browser window
st.set_page_config(layout="wide")

# Trigger welcoming animation
st.balloons()

# --- HERO SECTION: Logo & Brand Catchphrase ---
# Adjusted column weights so the right column takes up more structural space
hero_col1, hero_col2 = st.columns([1, 2.5], gap="large")

with hero_col1:
    st.image("assets/logo.png", use_container_width=True)

with hero_col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Welcome. Taste the goodness. Rooted in tradition. Forever.")
    st.markdown(
        """
        Every bite tells a story. At **Ammi's Chamcha**, we believe food carries memory—the joy of a festival, 
        the warmth of family. Rooted in the culinary heritage of Tamil Nadu, our dishes are 
        crafted with pure ghee, aromatic spices, and recipes passed down through generations.
        """
    )
    
st.write("---")

# --- STORY & GALLERY SECTION ---
story_col, img_grid_col = st.columns(2, gap="large")

with story_col:
    st.markdown("### Our Heritage")
    st.markdown(
        """
        From rich curries to comforting classics, sweets and snacks made with the same love as 
        those cherished in South Indian kitchens, every plate reflects our devotion to tradition 
        reimagined for today. 
        """
    )
    st.markdown(
        """
        We bring the cherished flavors of Tamil Nadu to Maryland, so that every dish feels like a 
        piece of South India, served with heart. Ammi's Chamcha is self-service, so linger. Explore. 
        Rediscover a flavor you've missed, or fall in love with something new.
        """
    )
    sub_col1, sub_col2 = st.columns(2, gap="small")
    with sub_col1:
        st.image("assets/combo.jpg", use_container_width=True)
    with sub_col2:
        st.image("assets/biryani.jpg", width=200)
with img_grid_col:
    sub_col1, sub_col2 = st.columns(2, gap="small")
    with sub_col1:
        st.image("assets/scroll1.jpg", use_container_width=True)
        st.image("assets/chicken.jpg", use_container_width=True)
    with sub_col2:
        st.image("assets/chicken.jpg", use_container_width=True)
        st.image("assets/sweet.jpg", use_container_width=True)

st.write("---")

# --- CUSTOMER FEEDBACK SECTION ---
st.header("What Our Customers Say")
with st.container(border=True):
    st.markdown(
        '"I just wanted to let you know that the Sweets, and the food are amazing! '
        'Everybody absolutely loved the food."'
    )
    st.caption("⭐⭐⭐⭐⭐ — Verified Customer Review")
    
    st.markdown(
        '"awesome puran poli! thank you! my mom said it reminded her of the ones she ate growing up in mumbai"'
    )
    st.caption("⭐⭐⭐⭐⭐ — Verified Customer Review")
    
    st.markdown(
        '"Thank you very much for the ladoos and chaklis! They were very delicious! The ladoos were indeed divine! The chaklis were very crispy and the color was excellent! I heard already very good comments."'
    )
    st.caption("⭐⭐⭐⭐⭐ — Verified Customer Review")

st.write("---")

# --- STORE SCHEDULE SECTION ---
st.header("Opening Hours")
col_hours1, col_hours2 = st.columns(2)

with col_hours1:
    with st.container(border=True):
        st.subheader("🍱 Lunch Hours")
        st.write("**Tuesday:** Closed 🛑")
        st.write("**Wednesday - Monday:** 11:00 AM - 03:00 PM ☀️")

with col_hours2:
    with st.container(border=True):
        st.subheader("🌙 Dinner Hours")
        st.write("**Tuesday:** Closed 🛑")
        st.write("**Wednesday - Monday:** 05:00 PM - 09:00 PM 🌙")
