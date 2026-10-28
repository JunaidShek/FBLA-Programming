"""
Cart Page - Cart Item Listing, Quantity Summaries, Item Removals, and Subtotal Calculations.
"""

import streamlit as st

st.title("🛒 Your Selected Dishes")
st.set_page_config(layout="wide")

# Check for empty cart state and offer menu redirect
if not st.session_state.cart:
    st.info("Your shopping cart is currently empty! Head back to the Menu page to add items.")
    if st.button("Browse Food Menu Now"):
        st.switch_page("menu.py")
else:
    st.write("Review your selections below before proceeding to checkout:")
    
    total_bill = 0.0
    
    # Iterate through cart items, compute item totals, and render item cards
    for idx, item in enumerate(st.session_state.cart):
        item_cost = item["price"] * item["qty"]
        total_bill += item_cost
        
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 1.5, 1])
            with c1:
                st.markdown(f"🍲 **{item['name']}**")
                st.caption(f"🌶️ Option/Spice: {item['spice']} | 🔢 Qty: {item['qty']}")
            with c2:
                st.markdown(f"`${item['price']:.2f} ea` \n\n **Total: ${item_cost:.2f}**")
            with c3:
                # Remove selected item from session state cart
                if st.button("🗑️ Remove", key=f"del_{idx}_{item['name'].lower()[:3]}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()

    st.write("---")
    
    # Render financial subtotal summary and checkout navigation button
    col_meta, col_actions = st.columns(2)
    with col_meta:
        st.markdown(f"### **Subtotal Price: ${total_bill:.2f}**")
        st.caption("Fulfillment selections, delivery modes, and 6% sales tax are calculated at checkout.")

    with col_actions:
        st.write("")
        if st.button("Proceed to Checkout Securely ➡️", use_container_width=True, type="primary"):
            st.session_state.order_summary = {
                "items": st.session_state.cart.copy(),
                "subtotal": total_bill
            }
            st.switch_page("buy.py")