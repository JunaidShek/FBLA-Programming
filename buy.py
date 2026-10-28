"""
Checkout Page - Fulfillment Toggles, Promo Code Discounts, Gratuity Selector,
Syntactical & Semantic Payment Validation, and Receipt Generation.
"""

import streamlit as st
import time
st.set_page_config(layout="wide")

st.title("💳 Secure Final Checkout")

# Redirect guard: prevents accessing checkout with an empty cart
if not st.session_state.cart or not st.session_state.order_summary:
    st.warning("Please add items to your cart and Enter from Cart page to access checkout.")
    st.stop()

summary = st.session_state.order_summary

# Fulfillment mode selector
st.subheader("1. Delivery Mode")
mode = st.radio("Choose fulfillment type:", ["🏠 Home Delivery", "🥡 In-Store Pickup"])

if mode == "🏠 Home Delivery":
    st.info(f"📍 Delivering directly to your profile address:\n**{st.session_state.account_data['address']}**")
else:
    st.info("📍 Restaurant Pickup Address: **5010 Buckeystown Pike STE 132, Frederick, MD 21704**")

# Promo code discount evaluation
st.subheader("2. Promo Code & Discounts")
promo_input = st.text_input("Enter Promo Code (Try WELCOME10 or FREEDELIVERY):", placeholder="Enter code here")

discount_amount = 0.0
promo_applied = False
if promo_input:
    cleaned_code = promo_input.strip().upper()
    if cleaned_code == "WELCOME10":
        discount_amount = summary["subtotal"] * 0.10
        promo_applied = True
        st.success("🎉 Promo code WELCOME10 applied: 10% off your subtotal!")
    elif cleaned_code == "FREEDELIVERY":
        discount_amount = 5.00
        promo_applied = True
        st.success("🎉 Promo code FREEDELIVERY applied: $5.00 discount!")
    else:
        st.error("❌ Invalid promo code. Please check and try again.")

adjusted_subtotal = max(0.0, summary["subtotal"] - discount_amount)

# Tip calculation logic
st.subheader("3. Add Gratuity / Tip")
tip_option = st.radio("Select Tip Percentage:", ["15%", "18%", "20%", "Custom", "No Tip"], horizontal=True)

tip_amount = 0.0
if tip_option == "15%":
    tip_amount = adjusted_subtotal * 0.15
elif tip_option == "18%":
    tip_amount = adjusted_subtotal * 0.18
elif tip_option == "20%":
    tip_amount = adjusted_subtotal * 0.20
elif tip_option == "Custom":
    tip_amount = st.number_input("Enter custom tip amount ($):", min_value=0.0, value=5.0, step=1.0)

# Payment input fields
st.subheader("4. Secure Payment Gateway")
cc_number = st.text_input("Credit Card Number", max_chars=19)
col_e, col_c = st.columns(2)
with col_e: 
    cc_expiry = st.text_input("Expiration Date (MM/YY)", max_chars=5)
with col_c: 
    cc_cvv = st.text_input("CVV", type="password", max_chars=3)

# Final financial report breakdown
st.subheader("5. Final Itemized Order Report")
with st.container(border=True):
    for item in summary["items"]:
        sub_cost = item["price"] * item["qty"]
        st.text(f"✔️ ({item['qty']}x) {item['name']:<35} [{item['spice']}] -> ${sub_cost:.2f}")
    st.write("---")
    tax = adjusted_subtotal * 0.06
    grand_total = adjusted_subtotal + tax + tip_amount
    st.write(f"Original Subtotal: ${summary['subtotal']:.2f}")
    if promo_applied:
        st.write(f"Promo Discount: -${discount_amount:.2f}")
        st.write(f"Adjusted Subtotal: ${adjusted_subtotal:.2f}")
    st.write(f"State Sales Tax (6%): ${tax:.2f}")
    if tip_amount > 0:
        st.write(f"Gratuity / Tip: ${tip_amount:.2f}")
    st.markdown(f"### **Total Charged: ${grand_total:.2f}**")

def validate_semantic_expiry(expiry_str: str) -> bool:
    """
    Semantic Check: Verifies expiration month is 01-12 and checks that the date
    represents a valid future date relative to October 2026.
    """
    try:
        if len(expiry_str) != 5 or expiry_str[2] != '/':
            return False
        parts = expiry_str.split('/')
        month = int(parts[0])
        year = int("20" + parts[1])
        if not (1 <= month <= 12):
            return False
        current_year, current_month = 2026, 10
        if year < current_year or (year == current_year and month < current_month):
            return False
        return True
    except ValueError:
        return False

# Payment submission & validation handler
if st.button("Authorize and Process Payment", type="primary", use_container_width=True):
    clean_cc = cc_number.replace(" ", "")
    
    # Syntactical and Semantic Input Validation Checks
    if not clean_cc or not cc_expiry or not cc_cvv:
        st.error("🚨 Validation Error: Please fill in all credit card input fields.")
    elif not clean_cc.isdigit() or len(clean_cc) < 15 or len(clean_cc) > 16:
        st.error("🚨 Syntactical Error: Credit card sequence must be a valid numeric sequence of 15 to 16 digits.")
    elif len(cc_expiry) < 5 or "/" not in cc_expiry:
        st.error("🚨 Syntactical Error: Expiration date must strictly match MM/YY rules.")
    elif not validate_semantic_expiry(cc_expiry):
        st.error("🚨 Semantic Error: Credit card expiration date must be between 01 and 12 and set to a valid future date.")
    elif not cc_cvv.isdigit() or len(cc_cvv) != 3:
        st.error("🚨 Syntactical Error: CVV code must consist of exactly 3 integers.")
    else:
        with st.spinner("Processing Secure Payment...", show_time=True):
            time.sleep(2)
        st.success("🎉 Order processed and sent securely to the kitchen team!")
        
        # Save order into persistent session state order history log
        if "order_history" not in st.session_state:
            st.session_state.order_history = []
            
        completed_order = {
            "items": summary["items"].copy(),
            "subtotal": adjusted_subtotal,
            "tax": tax,
            "tip": tip_amount,
            "total": grand_total,
            "mode": mode,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.order_history.append(completed_order)
        
        # Construct itemized text receipt string
        receipt_text = f"""=== AMMI'S CHAMCHA - OFFICIAL RECEIPT ===
Date/Time: {completed_order['timestamp']}
Fulfillment Mode: {mode}
--------------------------------------------------
"""
        for item in summary["items"]:
            receipt_text += f"({item['qty']}x) {item['name']} [{item['spice']}] - ${item['price'] * item['qty']:.2f}\n"
        receipt_text += f"--------------------------------------------------\n"
        if promo_applied:
            receipt_text += f"Discount Applied: -${discount_amount:.2f}\n"
        receipt_text += f"Subtotal: ${adjusted_subtotal:.2f}\n"
        receipt_text += f"State Tax (6%): ${tax:.2f}\n"
        receipt_text += f"Tip / Gratuity: ${tip_amount:.2f}\n"
        receipt_text += f"TOTAL CHARGED: ${grand_total:.2f}\n"
        receipt_text += f"==================================================\n"
        receipt_text += f"Thank you for ordering with Ammi's Chamcha!\n"
        
        # Provide receipt file download button
        st.download_button(
            label="📥 Download Itemized Order Receipt (.txt)",
            data=receipt_text,
            file_name=f"ammischamcha_receipt_{int(time.time())}.txt",
            mime="text/plain",
            type="primary"
        )
        
        # Reset shopping cart state upon successful checkout
        st.session_state.cart = []
        st.session_state.order_summary = None