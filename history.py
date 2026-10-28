"""
Order History Page - Displays Past Completed Orders, Itemized Receipts, and Order Status Badges.
"""

import streamlit as st
st.set_page_config(layout="wide")

st.title("📦 Your Order History & Tracking")
st.write("Review your past completed orders, itemized receipts, and fulfillment status below:")

# Display empty state if no past orders exist
if "order_history" not in st.session_state or not st.session_state.order_history:
    st.info("Your order history is currently empty! Complete a checkout to view past records here.")
    if st.button("Browse Food Menu"):
        st.switch_page("menu.py")
else:
    # Render past completed orders in reverse chronological order
    for idx, order in enumerate(reversed(st.session_state.order_history)):
        with st.container(border=True):
            col_info, col_price = st.columns([2, 1])
            with col_info:
                st.markdown(f"### Order #{len(st.session_state.order_history) - idx}")
                st.caption(f"🕒 Placed on: {order['timestamp']}")
                st.markdown(f"**Fulfillment Mode:** {order['mode']}")
            with col_price:
                st.markdown(f"**Total Charged:** `${order['total']:.2f}`")
                if idx == 0:
                    st.success("Status: Kitchen Preparing")
                else:
                    st.info("Status: Completed")
            
            # Expander for detailed item breakdown
            with st.expander("View Itemized Receipt Breakdown"):
                for item in order["items"]:
                    st.text(f"• ({item['qty']}x) {item['name']} [{item['spice']}] -> ${item['price'] * item['qty']:.2f}")
                st.write("---")
                st.write(f"Subtotal: `${order['subtotal']:.2f}` | Tax: `${order['tax']:.2f}` | Tip: `${order['tip']:.2f}`")