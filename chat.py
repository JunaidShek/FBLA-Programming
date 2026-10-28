"""
Help Desk Page - Knowledge-Base Virtual Assistant Chatbot with User Feedback Collection.
"""

import streamlit as st
st.set_page_config(layout="wide")

st.title("🙋‍♂️ Help Desk")
st.write("Interact with our virtual order agent using the help buttons below:")

# Structured knowledge base dictionary for support queries
SUPPORT_FLOWS = {
    "MENU_HELP": {
        "bot": "What menu customization or dietary question can I answer for you?",
        "options": ["🌱 Allergen / Veg Policy", "🌶️ Customizing Spice", "⏳ Dosa Wait Times"]
    },
    "🌱 Allergen / Veg Policy": {
        "bot": "All items under our Vegetarian tab are prepared on dedicated meat-free cooking surfaces. Please notify staff via order notes for severe allergies.",
        "options": ["🔄 Back to Help Options"]
    },
    "🌶️ Customizing Spice": {
        "bot": "You can select your preferred spice profile by expanding any food item card directly on our Menu page before adding it to your cart.",
        "options": ["🔄 Back to Help Options"]
    },
    "⏳ Dosa Wait Times": {
        "bot": "Specialty Tiffin items like Rava Dosa are made fresh to order and carry a minimum 15-minute kitchen preparation buffer.",
        "options": ["🔄 Back to Help Options"]
    },
    "ORDER_HELP": {
        "bot": "What part of the checkout or fulfillment process can I help you with?",
        "options": ["📍 Setting Delivery Mode", "💳 Card Validation Errors", "🛒 Clear / Modify Cart"]
    },
    "📍 Setting Delivery Mode": {
        "bot": "During final checkout, you can toggle between Home Delivery (routes to your account address) or In-Store Pickup at our Frederick, MD storefront.",
        "options": ["🔄 Back to Help Options"]
    },
    "💳 Card Validation Errors": {
        "bot": "Our gateway strictly validates inputs. Ensure your card number is 15-16 numeric digits, expiration matches MM/YY, and CVV is 3 digits.",
        "options": ["🔄 Back to Help Options"],
        "show_email_notice": True
    },
    "🛒 Clear / Modify Cart": {
        "bot": "Navigate to the View Cart page in the sidebar to remove items or update quantities.",
        "options": ["🔄 Back to Help Options"],
        "show_email_notice": True
    }
}

# Initialize chatbot conversation state
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [{"role": "assistant", "content": "Hello! Choose an option below to browse common questions or troubleshoot issues:"}]

if "chat_step" not in st.session_state:
    st.session_state.chat_step = "START"

# Render conversation container and thumb feedback logging
chat_container = st.container(height=380, border=True)
with chat_container:
    for msg_idx, msg in enumerate(st.session_state.chat_messages):
        with st.chat_message(msg["role"]): 
            st.write(msg["content"])
            if msg["role"] == "assistant":
                thumb_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                fb_key = f"fb_msg_{msg_idx}_{st.session_state.chat_step.lower().replace(' ', '_')[:3]}"
                selected_thumb = st.feedback("thumbs", key=fb_key)
                if selected_thumb is not None:
                    st.caption(f"Feedback logged: {thumb_mapping[selected_thumb]}")

# Display direct email redirect notice for complex technical topics
if st.session_state.chat_step in SUPPORT_FLOWS and SUPPORT_FLOWS[st.session_state.chat_step].get("show_email_notice"):
    st.warning("⚠️ Complex technical issue detected. Need further help?")
    if st.button("📩 Click here to Email Support Directly", type="primary"):
        st.switch_page("help.py")

# Determine active button options based on chat flow state
current_buttons = []
if st.session_state.chat_step == "START":
    current_buttons = ["📋 Menu & Dietary Help", "🛒 Ordering & Checkout Help"]
elif st.session_state.chat_step in ["MENU_HELP", "ORDER_HELP"]:
    current_buttons = SUPPORT_FLOWS[st.session_state.chat_step]["options"] + ["🔄 Back to Help Options"]
else:
    current_buttons = SUPPORT_FLOWS[st.session_state.chat_step]["options"]

st.write("---")
cols = st.columns(len(current_buttons))

# Render action buttons and handle user state transitions
for idx, action in enumerate(current_buttons):
    with cols[idx]:
        if st.button(action, key=f"help_action_{idx}", use_container_width=True):
            st.session_state.chat_messages.append({"role": "user", "content": action})
            if action == "🔄 Back to Help Options":
                st.session_state.chat_step = "START"
                st.session_state.chat_messages.append({"role": "assistant", "content": "How else can I assist you with your order today?"})
            elif action == "📋 Menu & Dietary Help":
                st.session_state.chat_step = "MENU_HELP"
                st.session_state.chat_messages.append({"role": "assistant", "content": SUPPORT_FLOWS["MENU_HELP"]["bot"]})
            elif action == "🛒 Ordering & Checkout Help":
                st.session_state.chat_step = "ORDER_HELP"
                st.session_state.chat_messages.append({"role": "assistant", "content": SUPPORT_FLOWS["ORDER_HELP"]["bot"]})
            else:
                st.session_state.chat_step = action
                st.session_state.chat_messages.append({"role": "assistant", "content": SUPPORT_FLOWS[action]["bot"]})
            st.rerun()