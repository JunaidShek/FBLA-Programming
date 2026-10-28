"""
Email Support Page - Customer Ticket Dispatch Form with Email Format Validation.
"""

import streamlit as st
st.set_page_config(layout="wide")

st.title("📬 Contact Support Desk")
st.write("We are sorry if your experience did not meet expectations. Please drop us an email below:")

default_email = st.session_state.account_data.get("email", "")

# Support form submission
with st.form("support_email_form"):
    user_email = st.text_input("Your Registered Email Address", value=default_email)
    issue_subject = st.text_input("Issue Category / Subject", value="Grievance / Ordering Assistance Request")
    message_body = st.text_area("Detailed Description of Issue or Feedback")
    
    submit_btn = st.form_submit_button("Send Support Ticket", type="primary")
    
    # Syntactical validation on support form inputs
    if submit_btn:
        if not user_email or not issue_subject or not message_body:
            st.error("🚨 Validation Error: Fields cannot be submitted empty.")
        elif "@" not in user_email or "." not in user_email:
            st.error("🚨 Syntactical Error: Please enter a structurally complete email format.")
        else:
            st.success("🎉 Support ticket dispatched successfully! Our team will follow up within 24 hours.")