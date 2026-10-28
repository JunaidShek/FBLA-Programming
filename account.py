"""
Account Page - User Profile, Credentials, and Shipping Address Management.
"""

import streamlit as st
st.set_page_config(layout="wide")

st.title("👤 My Account Profile Settings")
st.write("Review and update your personal credentials and preferred shipping below:")

# Form for updating user account details
with st.form("account_update_form"):
    user_email = st.text_input("Account Email Address", value=st.session_state.account_data["email"])
    user_password = st.text_input("Account Access Password", value=st.session_state.account_data["password"], type="password")
    user_address = st.text_area("Default Delivery / Shipping Address Location", value=st.session_state.account_data["address"])
    
    submit_changes = st.form_submit_button("Save Profile Changes", type="primary")
    
    # Save updated user profile data into global session state with syntax validation
    if submit_changes:
        if not user_email or not user_address:
            st.error("Email and Delivery Address values cannot be blank.")
        elif "@" not in user_email or "." not in user_email:
            st.error("Syntactical Error: Please enter a valid email format.")
        else:
            st.session_state.account_data["email"] = user_email
            st.session_state.account_data["password"] = user_password
            st.session_state.account_data["address"] = user_address
            st.success("⚙️ Profile settings updated successfully!")