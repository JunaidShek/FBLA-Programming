"""
Menu Page - Food Catalog, Item Customization, Real-Time Stock Tracking, and Global Search.
"""

from pathlib import Path
import random
import streamlit as st
import os
from PIL import Image
import time
st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).parent

st.title("🍽️ Ammi's Chamcha Menu")
st.write("Click on any dish below to customize your preferences and order quantities:")

def get_item_inventory(item_name: str) -> int:
    """Calculates a deterministic pseudo-random stock quantity using item name hash."""
    random.seed(abs(hash(item_name)) % 1000000)
    return random.randint(0, 15)

def load_small_image(image_path, target_size=(150, 150)):
    """Square-crops and resizes menu image assets for clean card layout display."""
    if not os.path.exists(image_path):
        return None
    try:
        img = Image.open(image_path)
        width, height = img.size
        min_dim = min(width, height)
        
        # Center-crop coordinates
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        
        img = img.crop((left, top, right, bottom))
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        return img
    except Exception:
        return None

# Dictionary organizing menu items by category
MENU_DATA = {
    "veg": {
        "title": "Vegetarian Starters", 
        "image": "assets/tiffin.jpg", 
        "is_sweet_or_bev": False,
        "items": [
            ("Masala Vada", 7.99, "South Indian deep fried snack made with lentils, onions and traditional spices."),
            ("Bajjis - Veggies", 7.99, "South Indian vegetable fritters, coated in spiced besan and fried golden, served with chutneys."),
            ("Pakoras - Veggies / Onion", 7.99, "Golden, crispy vegetable fritters coated in a flavorful chickpea flour batter."),
            ("Punugulu", 7.99, "Golden, crispy dumplings with a crunchy exterior and soft, fluffy centers."),
            ("Aloo Bonda", 7.99, "A popular, deep-fried Indian snack featuring spiced mashed potatoes encased in a crispy chickpea flour batter."),
            ("Gobi 65", 12.99, "Spicy cauliflower florets deep-fried in a 65 masala, popular in Chennai."),
            ("Karampodi - Gobi / Paneer", 12.99, "Crispy cauliflower florets or paneer tossed in a bold, house-made Andhra-style spice powder."),
            ("Karuvepaku - Gobi / Paneer", 12.99, "Crispy cauliflower florets or paneer tossed in a bold, aromatic house-made spiced curry leaf powder."),
            ("Manchurian - Veggie / Gobi / Paneer", 12.99, "Batter fried veggie balls, cauliflower, or paneer cooked in sweet and spicy Indo-Chinese sauce."),
            ("Chilli - Gobi / Paneer", 12.99, "Golden, crunchy paneer or cauliflower in a sweet and spicy garlic-soy glaze with fresh spring onions."),
            ("Kovai Kalan", 13.99, "Crispy deep-fried cabbage and mushroom fritters coated in a bold, tangy semi-dry Indo-Chinese sauce."),
            ("Kaima Idly", 11.99, "Crispy fried idli cubes tossed in a spicy sauce - South Indian street-food favorite."),
            ("Kara Paniyaram", 11.99, "Irresistibly crispy, fluffy dumplings bursting with onion, chili, and curry leaf flavors."),
            ("Samosa", 5.99, "Triangular-shaped savory pastry filled with spiced potatoes and peas."),
            ("Street Style Samosa", 5.99, "Triangular-shaped savory pastry filled with spicy onions."),
            ("Samosa Chaat", 8.99, "Crumbled samosas topped with savory chutneys, fresh yogurt, and ground spices.")
        ]
    },
    "nonveg": {
        "title": "Chicken, Mutton & Seafood Starters", 
        "image": "assets/chicken.jpg", 
        "is_sweet_or_bev": False,
        "items": [
            ("Chicken 65", 13.99, "Tender bite-sized chicken pieces marinated in yogurt and fiery spices, deep-fried with crisp curry leaves."),
            ("Chicken Lollipop (4 Pieces)", 13.99, "Frenched chicken wings marinated in aromatic Indo-Chinese spices and fried to golden perfection."),
            ("Karampodi - Chicken / Fish", 14.99, "Tender chicken or fish cubes tossed in a bold, house-made Andhra-style spice powder."),
            ("Karuvepaku - Chicken / Fish", 15.99, "Crispy fried chicken or fish tossed in a bold, aromatic house-made spiced curry leaf powder."),
            ("Chicken Chindhamani", 15.99, "Tamil Nadu special fiery, traditional dish with bite-sized chicken, shallots, and dry red chillies."),
            ("Chicken Pallipalayam", 15.99, "Fiery dry dish from Tamil Nadu made with chicken, shallots, red chilies, and fresh coconut slivers."),
            ("Chilli - Chicken / Fish / Shrimp", 13.99, "Golden, crunchy protein tossed in a sweet and spicy garlic-soy glaze with spring onions."),
            ("Mutton Chukka", 17.99, "Fiery semi-dry South Indian goat meat stir-fry coated in a thick, freshly ground pepper masala."),
            ("Apollo Fish", 15.99, "Tender boneless fish cubes in spiced batter, fried golden-crisp and tossed with zesty yogurt-garlic sauce."),
            ("Nethili Fry", 15.99, "Crispy anchovy fry marinated with regional spice powders and pan-fried to perfection."),
            ("Marina Fish Fry", 15.99, "Crispy pan-fried fish fillet coated in a bold Chennai coastal masala served with lemon and onion rings."),
            ("Muttai Kalakki", 5.99, "Soft, semi-cooked street-style eggs layered with pepper and flavorful meat gravy."),
            ("Prawn Vadai", 10.99, "Crispy golden patties made with minced prawns, lentils, aromatic spices, and fresh herbs."),
            ("Tawa Prawns", 18.99, "Succulent prawns cooked on a hot griddle and tossed with rich aromatic spices.")
        ]
    },
    "biryani": {
        "title": "Long Grain Basmati & Samba Biryanis", 
        "image": "assets/biryani.jpg", 
        "is_sweet_or_bev": False,
        "items": [
            ("Dum Biriyani - Veg", 13.99, "Authentic long-grain Basmati rice layered with seasonal vegetables and slow-cooked on dum."),
            ("Dum Biriyani - Chicken", 15.99, "Classic Hyderabadi layered chicken and fragrant basmati rice slow-cooked on dum with saffron."),
            ("Dum Biriyani - Mutton", 18.99, "Tender goat meat slow-cooked on dum layered with aromatic long-grain basmati rice."),
            ("Dum Biriyani - Fish", 19.99, "Marinated fish fillets cooked on dum layered with seasoned basmati rice and herbs."),
            ("Paneer Biriyani", 14.99, "Authentic long-grain Basmati rice layered with marinated paneer cubes and mild spices."),
            ("Egg Biriyani", 14.99, "Spiced boiled eggs layered with aromatic long-grain Basmati rice and slow-cooked on dum."),
            ("Thalappakatti Chicken Biriyani", 18.99, "Succulent chicken slow-cooked with short-grain Seeraga Samba rice, ghee, and hand-ground spices."),
            ("Thalappakatti Mutton Biriyani", 19.99, "Short-grain Samba rice and rich goat meat infused with traditional Dindigul hill country herbs."),
            ("Ambur Chicken Biriyani", 18.99, "Nawab-style aromatic biryani made with succulent chicken gravy and parboiled Jeera Samba rice."),
            ("Ambur Mutton Biriyani", 19.99, "One-pot Nawab-style biryani with tender mutton cooked along with aromatic Jeera Samba rice."),
            ("Kongu Chicken Biriyani", 18.99, "Signature Coimbatore-style dish with a mild spice profile, creamy texture, and aromatic flavors."),
            ("Kongu Mutton Biriyani", 19.99, "Coimbatore-style goat meat biryani crafted with subtle spices and fragrant rice."),
            ("Vijayawada Paneer Biriyani", 15.99, "Authentic long-grain Basmati rice layered with fiery Vijayawada-style spiced paneer."),
            ("Vijayawada Boneless Chicken Biriyani", 15.99, "Crispy spiced boneless chicken tossed in bold Andhra spices layered with fragrant basmati rice.")
        ]
    },
    "curries": {
        "title": "Traditional Curries & Gravies", 
        "image": "assets/curries.webp", 
        "is_sweet_or_bev": False,
        "items": [
            ("Chana Masala", 12.99, "Tender chickpeas simmered in a rich, tangy tomato-onion gravy with bold, aromatic spices."),
            ("Vegetable Salna", 13.99, "Spicy South Indian street-style watery gravy with vegetables, coconut, and roasted spices."),
            ("Vadacurry", 14.99, "Crumbled cooked lentil dumplings simmered with tempered spices, sweet onions, and tomatoes."),
            ("Paneer Tikka Masala", 14.99, "Smoky grilled paneer bathed in a luscious, creamy tomato-onion gravy with bold spices."),
            ("Paneer Butter Masala", 14.99, "Cubes of soft cottage cheese cooked in smooth buttery tomato and cashew nut sauce."),
            ("Paneer Saag", 14.99, "Tender paneer cubes cooked in a smooth spiced curry of spinach and leafy greens garnished with cream."),
            ("Urundai / Pakoda Kulambu", 15.99, "Tangy South Indian tamarind curry simmered with spiced lentil dumplings."),
            ("Green Veg Curry - Dhaba Style", 14.99, "Mixed vegetables in a smoky, creamy green gravy crafted with cashews and rustic spices."),
            ("Chettinadu Veg Curry", 13.99, "Assorted seasonal vegetables simmered in bold, roasted coconut and Chettinad spice masala."),
            ("Madras Curry - Veg / Paneer", 13.99, "Fresh seasonal vegetables or paneer simmered in a classic Tamil Nadu style bold spice masala."),
            ("Andhra Curry - Veg / Paneer", 13.99, "Vegetables or cottage cheese cooked in a fiery, hot Andhra-style chili gravy."),
            ("Butter Chicken Masala", 15.99, "Shredded tandoori chicken simmered in rich cashew-infused tomato cream sauce."),
            ("Chicken Tikka Masala", 15.99, "Smoky grilled chicken bathed in a luscious, creamy tomato-onion gravy with bold spices."),
            ("Chicken Salna", 14.99, "Spicy South Indian watery gravy with tender bone-in chicken, coconut, and aromatic spices."),
            ("Mutton Salna", 16.99, "Rich South Indian style street gravy crafted with goat meat, coconut, and whole spices."),
            ("Meen Kulambu", 18.99, "Fiery South Indian fish curry with tangy tamarind, cold-pressed sesame oil, and aromatic spices."),
            ("Mutton Paya", 18.99, "Rich gelatinous goat trotters stew slow-cooked overnight with aromatic spices."),
            ("Chicken Ghee Roast", 16.99, "Succulent chicken slow-cooked in rich aromatic ghee and coated in a fiery, tangy masala."),
            ("Chettinadu Chicken Curry", 14.99, "Bone-in chicken simmered in bold, roasted coconut and Chettinad spice masala."),
            ("Madras Curry - Chicken / Mutton", 14.99, "Tender chicken or goat meat simmered in a classic bold Madras spice gravy."),
            ("Andhra Curry - Chicken / Mutton", 14.99, "Chicken or mutton cooked in a fiery, hot Andhra-style green chili and spice gravy.")
        ]
    },
    "tiffins": {
        "title": "South Indian Tiffin Varieties", 
        "image": "assets/otherfood.webp", 
        "is_sweet_or_bev": False,
        "items": [
            ("Medhu Vada", 7.99, "Crisp outside, fluffy inside savory lentil donuts infused with black pepper and ginger."),
            ("Sambar Vada", 9.99, "Crispy deep fried South Indian lentil doughnut soaked in hot aromatic vegetable sambar."),
            ("Dahi Vada", 9.99, "Deep fried lentil dumplings dunked in smooth sweetened yogurt topped with sweet chutney."),
            ("Idly (2 Pieces)", 7.99, "Steamed, pillow-soft savory rice and black lentil cakes served with chutneys and sambar."),
            ("Ghee Podi Idly", 8.99, "Steamed rice cakes tossed in aromatic clarified butter and coated with spicy roasted lentil podi."),
            ("Thattu Idly", 6.99, "A large, extra-soft, plate-sized steamed rice cake topped with a dollop of pure melted ghee."),
            ("Sambar Idly", 8.99, "Fluffy steamed rice cakes submerged in a bowl of rich, aromatic vegetable sambar."),
            ("Karampodi Idly", 11.99, "Bite-sized idli cubes tossed in a bold, house-made Andhra-style spice powder and ghee."),
            ("Karuvepaku Idly", 11.99, "Idli cubes tossed in a bold, aromatic house-made spiced curry leaf powder."),
            ("Plain Dosa", 9.99, "Golden and crispy thin crepe made with fermented rice and black lentil batter."),
            ("Masala Dosa", 10.99, "Classic golden crispy rice crepe wrapping spiced onion-potato mash."),
            ("Mysore Masala Dosa", 11.99, "Crispy golden dosa layered with fiery garlic-chili chutney and savory spiced potato mash."),
            ("Bangalore Special Benna Dosa", 13.99, "Thick, spongy butter dosa crisp on the outside, generously buttered and melting inside."),
            ("Ghee Roast Dosa", 11.99, "Crispy ghee-roasted rice crepe dusted with spicy roasted lentil podi powder."),
            ("Paneer Tikka Dosa", 12.99, "Golden and crispy crepe topped with rich creamy tikka sauce and spiced paneer cubes."),
            ("Rava Dosa Special", 14.99, "Extra-crispy lace-like crepe crafted from thin semolina, cumin seeds, and peppercorns."),
            ("Onion Rava Dosa", 14.99, "Lacy crispy semolina crepe layered with finely chopped onions, green chilies, and herbs."),
            ("Uttappam - Onion / Veggie", 10.99, "Fluffy golden rice griddle pancake loaded with juicy onions, tomatoes, and herbs."),
            ("Egg Dosa", 11.99, "Soft, thick griddle pancake layered with beaten egg, black pepper, and fresh spices."),
            ("Chicken Tikka Dosa", 13.99, "Golden and crispy crepe topped with creamy tikka sauce and tender chicken pieces."),
            ("Madurai Kari Dosa - Chicken", 14.99, "Three-layered street-style dosa with fluffy egg, spiced chicken masala, and onions."),
            ("Madurai Kari Dosa - Mutton", 16.99, "Three-layered dosa layered with fluffy egg, minced mutton masala, and curry leaves."),
            ("Idiyappam", 7.99, "Hand-pressed steamed rice noodle nests served with fresh coconut milk."),
            ("Poori (2 Pieces)", 4.99, "Crisp, golden-brown puffed deep-fried wheat flatbreads served with potato masala."),
            ("Parotta (2 Pieces)", 6.99, "Flaky, golden South Indian layered flatbread with crisp edges and soft buttery pull-apart layers."),
            ("Kothu Parotta - Veg / Egg / Chicken", 13.99, "Shredded parotta fast-fried on a hot griddle with aromatic spices, onions, and rich salna gravy."),
            ("Potalam Parotta - Chicken / Mutton", 16.99, "Shredded parotta tossed in spicy masala with choice of meat, pan-steamed in a banana leaf parcel."),
            ("Naan - Butter / Garlic / Bullet", 2.99, "Warm tandoor-baked flatbread topped with pure butter, minced garlic, or spicy green chillies.")
        ]
    },
    "kids": {
        "title": "Kids Combinations & Platters", 
        "image": "assets/combo.jpg", 
        "is_sweet_or_bev": False,
        "items": [
            ("Mini Ghee Dosa Kid Platter", 6.99, "Small crispy golden dosas served with pure melted butter and mild dips."),
            ("Chocolate Dosa Treat", 7.99, "Sweet thin tawa crepe drizzled with warm hazelnut chocolate spread."),
            ("Kids French Fries Basket", 4.99, "Classic crinkle-cut golden potato sticks lightly salted."),
            ("Fried Rice - Veg / Egg / Chicken / Shrimp", 12.99, "Indo-Chinese style wok-tossed rice with savory soy sauce, crisp veggies, and protein."),
            ("Hakka Noodles - Veg / Egg / Chicken / Shrimp", 12.99, "Indo-Chinese style wok-tossed hakka noodles with fresh vegetables and protein."),
            ("Nutella Dosa", 11.99, "Thin, crispy golden crepe layered with rich Nutella chocolate-hazelnut spread."),
            ("Cheese Dosa", 11.99, "Crispy golden rice crepe filled with melted gooey mozzarella cheese."),
            ("Cheese & Veggie Dosa", 12.99, "Golden crepe loaded with melted cheese and finely chopped fresh vegetables."),
            ("Paniyaram - Dessert Sauces", 13.99, "Crispy, fluffy South Indian rice dumplings served warm with chocolate, strawberry, or butterscotch sauce.")
        ]
    },
    "sweets": {
        "title": "Traditional Homemade Sweets", 
        "image": "assets/sweet.jpg", 
        "is_sweet_or_bev": True,
        "items": [
            ("Gulab Jamun (2 Pieces)", 4.99, "Soft milk-solid dumplings saturated in warm cardamom-scented sugar syrup."),
            ("Rasamalai Milk Cups", 5.99, "Paneer cottage cheese discs submerged in chilled saffron and cardamom cream milk."),
            ("Mango Rasamalai", 6.99, "Rich, creamy saffron milk syrup blended with sweet Alphonso mango pulp and paneer discs."),
            ("Mysore Pak Traditional", 7.99, "Crumbly sweet block made from chickpea flour, sugar, and rich pure ghee."),
            ("Kaju Katli Cashew Slices", 8.99, "Diamond-shaped melt-in-your-mouth confections crafted from premium cashew paste."),
            ("Badam Halwa", 8.99, "Rich, melt-in-your-mouth almond pudding slow-cooked with ghee, saffron, and sugar."),
            ("Rava Kesari", 5.99, "Traditional South Indian semolina sweet pudding infused with saffron, ghee, and cashews."),
            ("Double Ka Meetha", 6.99, "Hyderabadi bread pudding soaked in saffron-cardamom milk and garnished with fried nuts.")
        ]
    },
    "beverages": {
        "title": "Cold & Hot Beverages", 
        "image": "assets/drink.jpg", 
        "is_sweet_or_bev": True,
        "items": [
            ("Madras Filter Coffee", 3.99, "Strong chicory-blend coffee brewed in traditional brass filter with hot milk."),
            ("Masala Chai Hot Tea", 3.99, "Black tea brewed with fresh ginger, cardamom, and whole milk."),
            ("Mango Lassi Yogurt Drink", 4.99, "Velvety chilled blend of Alphonso mango pulp and fresh churned yogurt."),
            ("Rose Milk", 4.99, "Chilled blend of creamy whole milk and aromatic rose syrup."),
            ("Badam Milk", 5.99, "Chilled almond milk infused with aromatic cardamom, saffron, and crushed pistachios."),
            ("Nannari Sharbath", 5.99, "Sweet, tangy sarsaparilla root cooler served with a refreshing burst of zesty lime."),
            ("Nungu Milk Sharbath", 7.99, "Cool, creamy ice apple drink with sweet Nannari syrup and chilled milk."),
            ("Almond Rose Lassi", 5.99, "Creamy almond yogurt drink blended with fragrant rose syrup."),
            ("Sweet Lassi with Saffron", 4.49, "Sweet, creamy yogurt drink flavored with premium saffron strands."),
            ("Madurai Jigarthanda", 7.99, "Tamil Nadu special summer drink with almond gum, Nannari syrup, reduced milk, and ice cream."),
            ("Sharjah Milkshake", 7.99, "Lusciously creamy banana shake made with ripe sweet bananas, milk, and rich malt."),
            ("Masala Chaas", 3.99, "Refreshing probiotic buttermilk drink seasoned with ground whole spices and fresh herbs."),
            ("Thums Up Indian Cola", 3.99, "Strongly carbonated Indian cola featuring a heavy, spicy kick finish."),
            ("Limca Lemon Soda", 3.99, "Popular Indian carbonated lemon-lime soft drink with a fizzy kick."),
            ("Coca-Cola / Diet Coke", 2.99, "Classic refreshing carbonated soft drink."),
            ("Sprite", 2.99, "Crisp, clear lemon-lime flavored carbonated soft drink.")
        ]
    }
}

def render_food_card(item_name: str, price: float, description: str, small_img, is_sweet_or_bev: bool = False):
    """Renders menu item cards with live stock tracking, customization popovers, and cart addition logic."""
    if "inventory" not in st.session_state:
        st.session_state.inventory = {}
        
    if item_name not in st.session_state.inventory:
        st.session_state.inventory[item_name] = get_item_inventory(item_name)
        
    stock = st.session_state.inventory[item_name]
    safe_slug = item_name.lower().replace(' ', '_').replace('/', '_').replace('-', '_')
    
    with st.container(border=True):
        card_cols = st.columns([1, 2], gap="small")
        with card_cols[0]:
            if small_img:
                st.image(small_img)
            else:
                st.markdown("No Image Available")
                
        with card_cols[1]:
            st.markdown(f"### {item_name}")
            st.markdown(f"**Price:** `${price:.2f}`")
            st.caption(description)
            
            # Real-time stock enforcement: disable card if out of stock
            if stock <= 0:
                st.error("Not available")
                st.button("Sold Out", key=f"dis_{safe_slug}", disabled=True, use_container_width=True)
            else:
                with st.popover("⚙️ Customize Options", use_container_width=True):
                    st.subheader(f"Configure {item_name}")
                    st.caption(f"Real-time Stock: {stock} left")
                    
                    if is_sweet_or_bev:
                        st.selectbox("Select Sweetness Level:", ["Less Sweet", "Regular Sweetness", "Extra Sweet"], key=f"sweet_{safe_slug}")
                    else:
                        st.selectbox("Select Spice Level:", ["Mild", "Medium", "Spicy", "Tamil Nadu Kick!"], key=f"spice_{safe_slug}")
                    
                    # Semantic input validation: quantity input capped at current stock level
                    st.number_input("Quantity:", min_value=1, max_value=max(1, stock), value=1, step=1, key=f"qty_{safe_slug}")
                
                # Add item to cart and decrement inventory upon confirmation
                if st.button("Add to My Order", key=f"add_{safe_slug}", use_container_width=True, type="primary"):
                    chosen_pref = st.session_state.get(f"sweet_{safe_slug}" if is_sweet_or_bev else f"spice_{safe_slug}")
                    chosen_qty = st.session_state.get(f"qty_{safe_slug}", 1)
                    current_stock = st.session_state.inventory[item_name]
                    
                    if chosen_qty <= current_stock:
                        st.session_state.inventory[item_name] -= chosen_qty
                        st.session_state.cart.append({
                            "name": item_name, "price": price, "qty": int(chosen_qty), "spice": chosen_pref
                        })
                        st.success(f"Added {chosen_qty}x {item_name} to your order!", icon="✅")
                        time.sleep(0.3)
                        st.rerun()
                    else:
                        st.error(f"Only {current_stock} available!")

def render_menu_grid(items, image_path, is_sweet_or_bev=False, category_key="menu"):
    """Arranges menu items into a 2-column paginated grid layout."""
    small_img = load_small_image(image_path)
    current_items = items
    if len(items) > 8:
        items_per_page = 8
        total_pages = (len(items) + items_per_page - 1) // items_per_page
        page = st.pagination(num_pages=total_pages, key=f"pagination_{category_key}")
        start_idx = (int(page) - 1) * items_per_page
        end_idx = start_idx + items_per_page
        current_items = items[start_idx:end_idx]

    for i in range(0, len(current_items), 2):
        cols = st.columns(2, gap="small")
        with cols[0]:
            render_food_card(current_items[i][0], current_items[i][1], current_items[i][2], small_img, is_sweet_or_bev)
        if i+1 < len(current_items):
            with cols[1]:
                render_food_card(current_items[i+1][0], current_items[i+1][1], current_items[i+1][2], small_img, is_sweet_or_bev)

# Global real-time search bar
search_query = st.text_input("🔍 Search menu items or filter by keyword:", placeholder="Type a dish name, ingredient (e.g., paneer, chicken, dosa), or dietary keyword...")

if search_query:
    st.subheader(f"Search Results for: '{search_query}'")
    matching_items = []
    
    # Filter items across all menu categories based on search query
    for cat_key, cat_data in MENU_DATA.items():
        for item in cat_data["items"]:
            if search_query.lower() in item[0].lower() or search_query.lower() in item[2].lower():
                matching_items.append((item, cat_data["image"], cat_data["is_sweet_or_bev"]))
    
    if not matching_items:
        st.info("No matching dishes found. Try a different search term!")
    else:
        for i in range(0, len(matching_items), 2):
            cols = st.columns(2, gap="small")
            with cols[0]:
                it, img_path, is_sb = matching_items[i]
                render_food_card(it[0], it[1], it[2], load_small_image(img_path), is_sb)
            if i+1 < len(matching_items):
                with cols[1]:
                    it, img_path, is_sb = matching_items[i+1]
                    render_food_card(it[0], it[1], it[2], load_small_image(img_path), is_sb)
else:
    # Render tabbed categories when search query is empty
    tab_veg, tab_nonveg, tab_biryani, tab_curries, tab_tiffins, tab_kids, tab_sweets, tab_beverages = st.tabs([
        "Vegetarian", "Non-Vegetarian", "Biryani", "Curries & Sides", "Tiffins", "Kids & Combos", "Sweets", "Beverages"
    ])

    with tab_veg:
        render_menu_grid(MENU_DATA["veg"]["items"], MENU_DATA["veg"]["image"], MENU_DATA["veg"]["is_sweet_or_bev"], category_key="veg")
    with tab_nonveg:
        render_menu_grid(MENU_DATA["nonveg"]["items"], MENU_DATA["nonveg"]["image"], MENU_DATA["nonveg"]["is_sweet_or_bev"], category_key="nonveg")
    with tab_biryani:
        render_menu_grid(MENU_DATA["biryani"]["items"], MENU_DATA["biryani"]["image"], MENU_DATA["biryani"]["is_sweet_or_bev"], category_key="biryani")
    with tab_curries:
        render_menu_grid(MENU_DATA["curries"]["items"], MENU_DATA["curries"]["image"], MENU_DATA["curries"]["is_sweet_or_bev"], category_key="curries")
    with tab_tiffins:
        render_menu_grid(MENU_DATA["tiffins"]["items"], MENU_DATA["tiffins"]["image"], MENU_DATA["tiffins"]["is_sweet_or_bev"], category_key="tiffins")
    with tab_kids:
        render_menu_grid(MENU_DATA["kids"]["items"], MENU_DATA["kids"]["image"], MENU_DATA["kids"]["is_sweet_or_bev"], category_key="kids")
    with tab_sweets:
        render_menu_grid(MENU_DATA["sweets"]["items"], MENU_DATA["sweets"]["image"], MENU_DATA["sweets"]["is_sweet_or_bev"], category_key="sweets")
    with tab_beverages:
        render_menu_grid(MENU_DATA["beverages"]["items"], MENU_DATA["beverages"]["image"], MENU_DATA["beverages"]["is_sweet_or_bev"], category_key="beverages")