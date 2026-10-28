# Ammi's Chamcha — Digital Ordering System

> **FBLA Competitive Event:** Introduction to Programming  
> **Topic:** Local Business Digital Ordering System  
> **Platform:** Python & Streamlit  

---

## What Our Project Does

Our project is a digital ordering app made for **Ammi's Chamcha**, a local South Indian restaurant in Frederick, MD! We built this app using Python and Streamlit so customers can easily order food online from home or on their phones.

When designing the app, we made sure it includes everything a real restaurant app needs:
- Browsing through 8 food categories with photos and descriptions.
- A search bar so customers can quickly find specific dishes.
- Customizing how spicy or sweet you want your food.
- Real-time stock counts so people can't order food that's sold out.
- Promo codes and tip options.
- Checking credit card numbers and expiration dates to stop bad entries.
- An order history page and downloadable text receipts.
- A virtual chatbot and email support form to help customers with questions.

---

## Project Structure & What Each File Does

We split our code into several Python files to keep things neat and easy to manage. Here is what each file does:

| File Name | What It Does |
| :--- | :--- |
| **`app.py`** | **The Main Hub:** This is the starting file. It handles page navigation, global settings (like cart data), Light/Dark mode styling, background music, and shows if the restaurant is currently open or closed based on the time of day. |
| **`home.py`** | **Home Page:** The welcoming page with food stories, customer reviews, and restaurant operating hours. |
| **`menu.py`** | **The Menu:** Displays all our dishes across 8 tabbed categories. It includes a live search bar, customization popups for spice levels, and keeps track of food inventory. |
| **`cart.py`** | **Shopping Cart:** Lets users review what they picked, change quantities, remove items, and view the price subtotal before going to checkout. |
| **`buy.py`** | **Checkout Page:** Where users pick delivery or pickup, enter promo codes, choose a tip, fill in their credit card info with error checks, and download an official text receipt. |
| **`history.py`** | **Order History:** Saves completed orders so users can look back at what they ordered, check order status, and view past receipts. |
| **`chat.py`** | **Help Chatbot:** An interactive Q&A assistant that answers common questions about dietary policies, wait times, and ordering help. |
| **`help.py`** | **Email Support:** A simple form for customers to send a support ticket if they need extra help. |
| **`settings.py`** | **App Settings:** Lets users turn on Dark Mode or mute the background music whenever they want. |
| **`account.py`** | **User Account:** Saves the user's email, password, and delivery address so they don't have to re-type it during checkout. |

---

## Python Libraries We Used

We used a few super helpful Python libraries to make this app look and work great:

- **Streamlit (`streamlit`)**: The main framework we used to build the web pages, buttons, forms, and layout.
- **Pillow (`PIL`)**: Used to automatically crop and resize food images so they all fit nicely inside cards on the menu.
- **Pathlib & OS (`pathlib`, `os`)**: Helped us find files and folders reliably on any computer.
- **Random (`random`)**: Used to create realistic stock inventory numbers for each menu dish.
- **Time (`time`)**: Used to get exact timestamps for orders, create unique receipt filenames, and simulate payment loading spinners.
- **Base64 (`base64`)**: Allowed us to play background music right inside Streamlit.

---

## How We Check User Inputs (Input Validation)

To make sure our app doesn't crash when someone types in wrong information, we added two levels of input checks:

1. **Syntax Checks (Formatting):**
   - **Credit Card Number:** Strips out spaces and checks if the entry is purely numbers with 15 to 16 digits.
   - **Expiration Date:** Checks that the user types the date in the `MM/YY` format with 5 characters.
   - **CVV Code:** Checks that it is exactly 3 numeric digits.
   - **Emails:** Makes sure email fields are not empty and contain `@` and `.` characters.

2. **Semantic Checks (Real-World Logic):**
   - **Future Expiration Dates:** The app parses the month and year of the credit card. It checks that the month is between `01` and `12` and verifies that the card won't expire in the past.
   - **Stock Inventory Caps:** Users can't add more food items than what is currently in stock. If an item hits 0, it shows "Sold Out" and disables the button.

---

## Image & Resource Credits

We made sure to give full credit for all external images and audio used in our project:

- **Food Images:**
  - `assets/biryani.jpg`: South Indian / Kerala Biryani dish photo via *Wikimedia Commons (Wiki Loves Food)*.
  - `assets/chicken.jpg`: Chicken 65 appetizer photo via *Spice Life Indian Fare / My Kitchen Diaries*.
  - `assets/combo.jpg`: South Indian Tiffin Platter photo via *Sattvic Recipe / Grubhub*.
  - `assets/curries.webp`: Butter Chicken in copper handi bowl photo via *My Delhi Premium Indian Eatery*.
  - `assets/drink.jpg`: Fresh Mango Lassi photo via *The Cookie Rookie / Coconuts & Kettlebells*.
  - `assets/otherfood.webp`: Indian feast spread with Naan & Tandoori Chicken photo via *HeritageOne*.
  - `assets/scroll1.jpg`: Traditional South Indian Ela Sadya (Banana Leaf Meal) photo via *Indulge Express / Au Revoir*.
  - `assets/sweet.jpg`: Warm Gulab Jamun photo via *Bharat Mirchandani (Flickr) / HHWT*.
- **Background Music:**
  - Ambient storefront soundtrack via YouTube: [Ammi's Chamcha Storefront Ambient Soundtrack](https://www.youtube.com/watch?v=6OcZYlRRaTc&list=PLKDccW9WtMV8yY9aKhURsBv4hI5kG5Dxl&index=1).

---
*Created for the Future Business Leaders of America (FBLA) High School Competitive Events Program.*