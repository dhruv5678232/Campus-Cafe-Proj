import streamlit as st
import plotly.express as px
import pandas as pd

# Mock data with updated 'rise' and 'embers' inventory
restaurants = {
    'rise': {
        'name': 'Rise - Ready to Serve',
        'theme_gradient': 'linear-gradient(135deg, #8B4513, #D2691E)',
        'inventory': [
            {'id': 'rise_tea', 'name': 'Tea [Medium]', 'stock': 47, 'max_stock': 50, 'category': 'drink', 'available': True, 'price': '25.00'},
            {'id': 'rise_chicken_puff', 'name': 'Chicken Puff', 'stock': 18, 'max_stock': 20, 'category': 'pastry', 'available': True, 'price': '55.00'},
            {'id': 'rise_coffee', 'name': 'Coffee', 'stock': 18, 'max_stock': 20, 'category': 'drink', 'available': True, 'price': '40.00'},
            {'id': 'rise_veggie_puff', 'name': 'Veg Puff', 'stock': 22, 'max_stock': 25, 'category': 'pastry', 'available': True, 'price': '40.00'},
            {'id': 'rise_egg_puff', 'name': 'Egg Puff', 'stock': 8, 'max_stock': 10, 'category': 'pastry', 'available': True, 'price': '__'},
            {'id': 'rise_black_forest', 'name': 'Black Forest Pastry', 'stock': 15, 'max_stock': 25, 'category': 'pastry', 'available': True, 'price': '80.00'},
            {'id': 'rise_chocolate_pastry', 'name': 'Chocolate Pastry', 'stock': 10, 'max_stock': 25, 'category': 'pastry', 'available': True, 'price': '80.00'},
            {'id': 'rise_red_velvet', 'name': 'Red Velvet Pastry', 'stock': 12, 'max_stock': 20, 'category': 'pastry', 'available': True, 'price': '80.00'},
            {'id': 'rise_samosa', 'name': 'Samosa Pastry', 'stock': 20, 'max_stock': 40, 'category': 'pastry', 'available': False, 'price': '__'},
            {'id': 'rise_korean_cheese', 'name': 'Korean Cream Cheese Bun', 'stock': 1, 'max_stock': 15, 'category': 'pastry', 'available': True, 'price': '60.00'},
            {'id': 'rise_hashbrown', 'name': 'Hashbrown Omelette', 'stock': 12, 'max_stock': 20, 'category': 'meal', 'available': True, 'price': '__'},
            {'id': 'rise_omlette', 'name': 'Omelette', 'stock': 25, 'max_stock': 30, 'category': 'meal', 'available': True, 'price': '__'},
            {'id': 'rise_chicken_sandwich', 'name': 'Chicken Sandwich', 'stock': 20, 'max_stock': 25, 'category': 'sandwich', 'available': True, 'price': '90.00'},
            {'id': 'rise_paneer_sandwich', 'name': 'Paneer Sandwich', 'stock': 18, 'max_stock': 20, 'category': 'sandwich', 'available': True, 'price': '75.00'},
            {'id': 'rise_spicy_chicken_pizza', 'name': 'Spicy Chicken Pizza', 'stock': 15, 'max_stock': 20, 'category': 'pizza', 'available': True, 'price': '__'},
            {'id': 'rise_paneer_pizza', 'name': 'Paneer Pizza', 'stock': 12, 'max_stock': 15, 'category': 'pizza', 'available': True, 'price': '__'},
            {'id': 'rise_4_cheese_pizza', 'name': '4 Cheese Pizza', 'stock': 10, 'max_stock': 15, 'category': 'pizza', 'available': True, 'price': '__'},
            {'id': 'rise_margerita_pizza', 'name': 'Margerita Pizza', 'stock': 8, 'max_stock': 12, 'category': 'pizza', 'available': True, 'price': '__'},
            {'id': 'rise_market_fresh_pizza', 'name': 'Market Fresh Pizza', 'stock': 5, 'max_stock': 10, 'category': 'pizza', 'available': True, 'price': '__'},
            {'id': 'rise_veg_burger', 'name': 'Veg Burger', 'stock': 15, 'max_stock': 20, 'category': 'burger', 'available': True, 'price': '__'},
            {'id': 'rise_chicken_smash_burger', 'name': 'Chicken Smash Burger', 'stock': 12, 'max_stock': 15, 'category': 'burger', 'available': True, 'price': '__'},
            {'id': 'rise_chicken_fingers', 'name': 'Chicken Fingers', 'stock': 10, 'max_stock': 15, 'category': 'snack', 'available': True, 'price': '__'},
            {'id': 'rise_crispy_corn', 'name': 'Crispy Corn', 'stock': 8, 'max_stock': 12, 'category': 'snack', 'available': True, 'price': '__'},
            {'id': 'rise_french_fries', 'name': 'French Fries', 'stock': 20, 'max_stock': 25, 'category': 'snack', 'available': True, 'price': '__'},
            {'id': 'rise_masala_fries', 'name': 'Masala Fries', 'stock': 15, 'max_stock': 20, 'category': 'snack', 'available': True, 'price': '__'},
        ],
        'sales_data': [
            {'item_id': 'rise_chicken_puff', 'quantity': 75, 'revenue': 375},
            {'item_id': 'rise_coffee', 'quantity': 50, 'revenue': 250},
            {'id': 'rise_veggie_puff', 'quantity': 25, 'revenue': 125},
            {'id': 'rise_egg_puff', 'quantity': 15, 'revenue': 75},
        ],
        'ratings': [
            {'item_id': 'rise_tea', 'rating': 4.2, 'comment': 'Sometimes too sweet, sometimes perfect, inconsistent.', 'timestamp': '2023-01-14'},
            {'item_id': 'rise_chicken_puff', 'rating': 4.6, 'comment': 'Amazing flavor, gets sold quickly.', 'timestamp': '2023-01-14'},
            {'item_id': 'rise_coffee', 'rating': 3.8, 'comment': 'Too bitter today. Please reduce strength.', 'timestamp': '2023-01-14'},
            {'item_id': 'rise_veggie_puff', 'rating': 4.1, 'comment': 'Good filling but pastry could be crispier.', 'timestamp': '2023-01-14'},
            {'item_id': 'rise_samosa', 'rating': 3.9, 'comment': 'Oil was too much today, made me feel heavy.', 'timestamp': '2023-01-14'},
        ],
        'suggestions': [
            {'item_name': 'Mocha Chai', 'description': 'Traditional chai with cardamom and ginger', 'status': 'pending', 'timestamp': '2023-01-15'},
            {'item_name': 'Veggie Burger', 'description': 'Veggie burger with mint chutney', 'status': 'pending', 'timestamp': '2023-01-14'},
            {'item_name': 'Pav Bhaji', 'description': 'Spiced mashed veggies with bread', 'status': 'approved', 'timestamp': '2023-01-14'},
        ],
        'metrics': {
            'today_sales': 24.825,
            'gross_cost': 22.150,
            'gross_profit': 2.675,
            'net_profit': 1.890,
            'items_sold': 127,
            'low_stock_items': 3
        },
        'weekly_revenue': [4500, 4600, 4700, 4650, 4550, 4400, 4000]
    },
    'embers': {
        'name': 'Embers - Ready to Serve',
        'theme_gradient': 'linear-gradient(135deg, #1e3c72, #2a5298)',
        'inventory': [
            {'id': 'embers_chicken_lollipop', 'name': 'Chicken Lollipop', 'stock': 15, 'max_stock': 20, 'category': 'snack', 'available': True, 'price': '__'},
            {'id': 'embers_chilli_paneer', 'name': 'Chilli Paneer', 'stock': 12, 'max_stock': 15, 'category': 'meal', 'available': True, 'price': '__'},
            {'id': 'embers_paneer_tikka_masala', 'name': 'Paneer Tikka Masala', 'stock': 10, 'max_stock': 15, 'category': 'meal', 'available': True, 'price': '__'},
            {'id': 'embers_veg_manchurian', 'name': 'Veg Manchurian', 'stock': 8, 'max_stock': 12, 'category': 'meal', 'available': True, 'price': '__'},
            {'id': 'embers_achari_paneer_tikka', 'name': 'Achari Paneer Tikka', 'stock': 5, 'max_stock': 10, 'category': 'snack', 'available': True, 'price': '__'},
            {'id': 'embers_fish_curry', 'name': 'Fish Curry', 'stock': 10, 'max_stock': 15, 'category': 'meal', 'available': True, 'price': '__'},
        ],
        'sales_data': [
            {'item_id': 'embers_chicken_lollipop', 'quantity': 30, 'revenue': 240},
            {'item_id': 'embers_chilli_paneer', 'quantity': 20, 'revenue': 160},
            {'id': 'embers_paneer_tikka_masala', 'quantity': 15, 'revenue': 120},
            {'id': 'embers_veg_manchurian', 'quantity': 10, 'revenue': 80},
        ],
        'ratings': [
            {'item_id': 'embers_chicken_lollipop', 'rating': 4.5, 'comment': 'Spicy and delicious', 'timestamp': '2023-01-15'},
            {'item_id': 'embers_chilli_paneer', 'rating': 4.3, 'comment': 'Perfect spice level', 'timestamp': '2023-01-15'},
            {'item_id': 'embers_paneer_tikka_masala', 'rating': 4.4, 'comment': 'Rich and creamy', 'timestamp': '2023-01-15'},
            {'item_id': 'embers_veg_manchurian', 'rating': 4.1, 'comment': 'Great texture', 'timestamp': '2023-01-15'},
            {'item_id': 'embers_achari_paneer_tikka', 'rating': 4.2, 'comment': 'Unique tangy flavor', 'timestamp': '2023-01-15'},
            {'item_id': 'embers_fish_curry', 'rating': 4.3, 'comment': 'Well-spiced and fresh', 'timestamp': '2023-01-15'},
        ],
        'suggestions': [
            {'item_name': 'Butter Chicken', 'description': 'Rich creamy chicken curry', 'status': 'pending', 'timestamp': '2023-01-15'},
            {'item_name': 'Paneer Tikka', 'description': 'Grilled paneer with spices', 'status': 'pending', 'timestamp': '2023-01-14'},
            {'item_name': 'Rasmalai', 'description': 'Sweetened cheese balls in milk', 'status': 'approved', 'timestamp': '2023-01-14'},
        ],
        'metrics': {
            'today_sales': 28.750,
            'gross_cost': 25.500,
            'gross_profit': 3.250,
            'net_profit': 2.300,
            'items_sold': 75,
            'low_stock_items': 1
        },
        'weekly_revenue': [3500, 3600, 3700, 3650, 3550, 3400, 3200]
    }
}

# Streamlit app
st.set_page_config(page_title="Restaurant Management Dashboard", layout="wide")

if 'active_view' not in st.session_state:
    st.session_state.active_view = 'admin'
if 'active_restaurant' not in st.session_state:
    st.session_state.active_restaurant = 'rise'
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Sidebar
with st.sidebar:
    st.title("Dashboard Controls")
    selected_rest = st.selectbox("Select Restaurant", ['rise', 'embers'], index=0 if st.session_state.active_restaurant == 'rise' else 1)
    if selected_rest != st.session_state.active_restaurant:
        st.session_state.active_restaurant = selected_rest
    selected_view = st.selectbox("Select View", ['Admin View', 'Student View'], index=0 if st.session_state.active_view == 'admin' else 1)
    if selected_view == 'Admin View' and st.session_state.active_view != 'admin':
        st.session_state.active_view = 'admin'
    elif selected_view == 'Student View' and st.session_state.active_view != 'student':
        st.session_state.active_view = 'student'

# Apply theme
theme_gradient = restaurants[st.session_state.active_restaurant]['theme_gradient']
st.markdown(f"""
<style>
    .main {{
        background: {theme_gradient};
        background-attachment: fixed;
    }}
    .stApp {{
        background: {theme_gradient};
    }}
    .stButton>button {{
        background-color: #f0e6d2;
        color: black;
    }}
    .stMetric>label {{
        color: #4a2c0e;
    }}
    .css-1aumxhk {{
        background-color: #f0e6d2;
    }}
</style>
""", unsafe_allow_html=True)

# Header Metrics with updated currency format (only for Admin View)
current_restaurant = restaurants.get(st.session_state.active_restaurant, {})
metrics = current_restaurant.get('metrics', {'today_sales': 0, 'gross_cost': 0, 'gross_profit': 0, 'net_profit': 0, 'items_sold': 0, 'low_stock_items': 0})
if st.session_state.active_view == 'admin':
    st.title(current_restaurant.get('name', 'Restaurant Dashboard'))
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Today's Sales", f"₹{int(metrics['today_sales'] * 1000):,}")
    col2.metric("Gross Cost", f"₹{int(metrics['gross_cost'] * 1000):,}")
    col3.metric("Gross Profit", f"₹{int(metrics['gross_profit'] * 1000):,}")
    col4.metric("Net Profit", f"₹{int(metrics['net_profit'] * 1000):,}")
    col5.metric("Items Sold", f"{metrics['items_sold']:,}")
    col6, col7 = st.columns([3, 2])
    col6.metric("Low Stock Items", f"{metrics['low_stock_items']:,}")

# Main Content
if st.session_state.active_view == 'admin':
    col1, col2, col3 = st.columns([2, 3, 2])
    
    with col1:
        st.subheader("Inventory Overview")
        df_inv = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        if not df_inv.empty:
            # Filter out new items (those with IDs containing sandwich, pizza, burger, etc.)
            df_inv_original = df_inv[~df_inv['id'].str.contains('sandwich|pizza|burger|chicken_fingers|crispy_corn|french_fries|masala_fries')]
            # Convert stock and max_stock to numeric, coercing errors to NaN
            df_inv_original['stock'] = pd.to_numeric(df_inv_original['stock'], errors='coerce')
            df_inv_original['max_stock'] = pd.to_numeric(df_inv_original['max_stock'], errors='coerce')
            df_inv_original['stock_pct'] = (df_inv_original['stock'] / df_inv_original['max_stock'] * 100).round(1)
            for _, row in df_inv_original.iterrows():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.metric(label=row['name'], value=f"{int(row['stock'])}/{int(row['max_stock'])}")
                    st.caption(f"Category: {row['category']} | Available: {'Yes' if row['available'] else 'No'} | Price: ₹{row['price']}")
                    st.toggle("Availability", value=row['available'], key=f"toggle_{row['id']}")
                with col2:
                    if st.button("+", key=f"stock_add_{row['id']}"):
                        for item in restaurants[st.session_state.active_restaurant]['inventory']:
                            if item['id'] == row['id']:
                                item['stock'] += 1
                                st.rerun()
        else:
            st.warning("No inventory data available.")
    
    with col2:
        st.subheader("Sales Analytics")
        df_sales = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('sales_data', []))
        df_inv_data = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        if not df_sales.empty and not df_inv_data.empty:
            df_sales = df_sales.merge(df_inv_data[['id', 'name']], left_on='item_id', right_on='id', how='left')
            df_sales = df_sales[['name', 'quantity', 'revenue']].head(4)
            fig_bar = px.bar(df_sales, x='name', y='quantity', title='Top 4 Selling Items',
                             color='revenue', color_continuous_scale='Viridis')
            st.plotly_chart(fig_bar, use_container_width=True)
            
            weekly_revenue = restaurants.get(st.session_state.active_restaurant, {}).get('weekly_revenue', [])
            if weekly_revenue:
                days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                fig_line = px.line(x=days, y=weekly_revenue,
                                   title='Weekly Revenue Trend (₹)', markers=True)
                st.plotly_chart(fig_line, use_container_width=True)
            
            # New grid display for recently added items with availability toggle
            st.subheader("New Menu Items")
            new_items = df_inv_data[df_inv_data['id'].str.contains('sandwich|pizza|burger|chicken_fingers|crispy_corn|french_fries|masala_fries')]
            if not new_items.empty:
                num_cols = 3
                cols = st.columns(num_cols)
                for idx, (_, row) in enumerate(new_items.iterrows()):
                    with cols[idx % num_cols]:
                        with st.container():
                            st.write(f"**{row['name']}**")
                            st.metric("Stock", f"{int(row['stock'])}/{int(row['max_stock'])}")
                            st.caption(f"Category: {row['category']} | Price: ₹{row['price']}")
                            st.toggle("Availability", value=row['available'], key=f"new_toggle_{row['id']}")
            else:
                st.info("No new items to display.")
    
    with col3:
        st.subheader("Stock Levels")
        df_inv = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        if not df_inv.empty:
            # Convert stock and max_stock to numeric, coercing errors to NaN
            df_inv['stock'] = pd.to_numeric(df_inv['stock'], errors='coerce')
            df_inv['max_stock'] = pd.to_numeric(df_inv['max_stock'], errors='coerce')
            # Group by category and use item name for lines
            fig_stock = px.line(df_inv, x='category', y='stock', color='name', title='Stock Levels by Category',
                                markers=True)
            st.plotly_chart(fig_stock, use_container_width=True)
    
    with col3:
        st.subheader("Item Ratings & Reviews")
        df_ratings = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('ratings', []))
        if not df_ratings.empty:
            for _, row in df_ratings.iterrows():
                st.metric(label=row['name'] if 'name' in row else row['item_id'], value=f"{row['rating']} ⭐")
                st.write(row['comment'])
                st.caption(f"Reviewed on: {row['timestamp']}")
        else:
            st.warning("No ratings data available.")
    
    # Suggestions Panel
    st.subheader("Student Suggestions")
    df_sugg = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('suggestions', []))
    if not df_sugg.empty:
        for _, row in df_sugg.iterrows():
            with st.container():
                st.write(f"**{row['item_name']}** - {row['description']}")
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.caption(f"Status: {row['status'].capitalize()} | Submitted on: {row['timestamp']}")
                with col2:
                    if row['status'] == 'pending':
                        if st.button("Approve", key=f"approve_{row['item_name']}"):
                            row['status'] = 'approved'
                            st.rerun()
                with col3:
                    if row['status'] == 'pending':
                        if st.button("Reject", key=f"reject_{row['item_name']}"):
                            row['status'] = 'rejected'
                            st.rerun()
    else:
        st.info("No suggestions available.")

elif st.session_state.active_view == 'student':
    # Student Dashboard (no stats or title metrics)
    tab1, tab2, tab3, tab4 = st.tabs(["Top Items", "Rate an Item", "Suggest New Item", "Order Now"])
    
    with tab1:
        st.subheader("Top Items")
        df_inv = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        df_ratings = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('ratings', []))
        if not df_ratings.empty and not df_inv.empty:
            df_top = df_ratings.groupby('item_id').agg({'rating': 'mean', 'comment': 'count'}).reset_index()
            df_top = df_top.merge(df_inv[['id', 'name']], left_on='item_id', right_on='id', how='left')
            df_top = df_top.sort_values('rating', ascending=False).head(10)
            fig = px.bar(df_top, x='name', y='rating', title='Top Rated Items',
                         color='comment', hover_data=['comment'])
            # Set custom y-axis ticks for 0.25, 0.5, 0.75, 1, etc. up to 5
            fig.update_layout(yaxis=dict(tickmode='array', tickvals=[0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5], ticktext=['0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2', '2.25', '2.5', '2.75', '3', '3.25', '3.5', '3.75', '4', '4.25', '4.5', '4.75', '5']))
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df_top, use_container_width=True)
        else:
            st.info("No items available.")
    
    with tab2:
        st.subheader("Rate an Item")
        df_items = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        item_names = df_items[df_items['available']]['name'].tolist()
        
        if item_names:
            item_name = st.selectbox("Select an Item to Rate", item_names)
            selected_item_id = df_items[df_items['name'] == item_name]['id'].iloc[0]
            
            rating = st.slider("Your Rating", 1, 5, 3, help="1-5 stars")
            comment = st.text_area("Comments (optional)", placeholder="Tell us about your experience...")
            
            if st.button("Submit Rating", type="primary"):
                new_rating = {'item_id': selected_item_id, 'rating': rating, 'comment': comment, 'timestamp': '2025-09-17'}
                if 'ratings' not in st.session_state:
                    st.session_state.ratings = restaurants[st.session_state.active_restaurant].get('ratings', []).copy()
                st.session_state.ratings.append(new_rating)
                st.success("Thank you for your rating! It has been submitted.")
        else:
            st.warning("No available items to rate.")
    
    with tab3:
        st.subheader("Suggest a New Item")
        with st.form("suggestion_form", clear_on_submit=True):
            item_name = st.text_input("Item Name", placeholder="e.g., Butter Chicken")
            category = st.selectbox("Category", ['drink', 'snack', 'meal', 'dessert'])
            description = st.text_area("Description", placeholder="Describe the item...", max_chars=500)
            dietary = st.multiselect("Dietary Preferences", ['vegetarian', 'vegan', 'gluten-free'], help="Select all that apply")
            dietary_str = ", ".join(dietary) if dietary else ""
            
            submitted = st.form_submit_button("Submit Suggestion", type="primary")
            
            if submitted:
                if item_name and description:
                    new_suggestion = {
                        'item_name': item_name,
                        'description': description,
                        'category': category,
                        'dietary_info': dietary_str,
                        'status': 'pending',
                        'timestamp': '2025-09-17'
                    }
                    if 'suggestions' not in st.session_state:
                        st.session_state.suggestions = restaurants[st.session_state.active_restaurant].get('suggestions', []).copy()
                    st.session_state.suggestions.append(new_suggestion)
                    st.success("Your suggestion has been submitted! We'll review it soon.")
                else:
                    st.error("Please provide at least an item name and description.")
    
    with tab4:
        st.subheader("Order Now")
        df_inv = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        
        # Drinks
        st.subheader("Drinks")
        drinks = df_inv[df_inv['category'] == 'drink'].sort_values('name')
        for _, row in drinks.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{row['name']} - ₹{row['price']}")
            with col2:
                if st.button("+", key=f"add_drink_{row['id']}"):
                    if not row['available']:
                        st.error("Out of stock, please try ordering again later")
                    else:
                        if row['id'] not in st.session_state.cart:
                            st.session_state.cart[row['id']] = {'name': row['name'], 'price': float(row['price']) if row['price'] != '__' else 0.0, 'quantity': 0}
                        st.session_state.cart[row['id']]['quantity'] += 1
                        st.rerun()
        
        # Pastries
        st.subheader("Pastries")
        pastries = df_inv[df_inv['category'] == 'pastry'].sort_values('name')
        for _, row in pastries.iterrows():
            if 'samosa' not in row['name'].lower() and 'puff' not in row['name'].lower():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"{row['name']} - ₹{row['price']}")
                with col2:
                    if st.button("+", key=f"add_pastry_{row['id']}"):
                        if not row['available']:
                            st.error("Out of stock, please try ordering again later")
                        else:
                            if row['id'] not in st.session_state.cart:
                                st.session_state.cart[row['id']] = {'name': row['name'], 'price': float(row['price']) if row['price'] != '__' else 0.0, 'quantity': 0}
                            st.session_state.cart[row['id']]['quantity'] += 1
                            st.rerun()
        
        # Samosas and Puffs
        st.subheader("Samosas and Puffs")
        samosas_puffs = df_inv[df_inv['category'] == 'pastry'].sort_values('name')
        for _, row in samosas_puffs.iterrows():
            if 'samosa' in row['name'].lower() or 'puff' in row['name'].lower():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"{row['name']} - ₹{row['price']}")
                with col2:
                    if st.button("+", key=f"add_samosa_puff_{row['id']}"):
                        if not row['available']:
                            st.error("Out of stock, please try ordering again later")
                        else:
                            if row['id'] not in st.session_state.cart:
                                st.session_state.cart[row['id']] = {'name': row['name'], 'price': float(row['price']) if row['price'] != '__' else 0.0, 'quantity': 0}
                            st.session_state.cart[row['id']]['quantity'] += 1
                            st.rerun()
        
        # Burgers
        st.subheader("Burgers")
        burgers = df_inv[df_inv['category'] == 'burger'].sort_values('name')
        for _, row in burgers.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{row['name']} - ₹{row['price']}")
            with col2:
                if st.button("+", key=f"add_burger_{row['id']}"):
                    if not row['available']:
                        st.error("Out of stock, please try ordering again later")
                    else:
                        if row['id'] not in st.session_state.cart:
                            st.session_state.cart[row['id']] = {'name': row['name'], 'price': float(row['price']) if row['price'] != '__' else 0.0, 'quantity': 0}
                        st.session_state.cart[row['id']]['quantity'] += 1
                        st.rerun()
        
        # Pizzas
        st.subheader("Pizzas")
        pizzas = df_inv[df_inv['category'] == 'pizza'].sort_values('name')
        for _, row in pizzas.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{row['name']} - ₹{row['price']}")
            with col2:
                if st.button("+", key=f"add_pizza_{row['id']}"):
                    if not row['available']:
                        st.error("Out of stock, please try ordering again later")
                    else:
                        if row['id'] not in st.session_state.cart:
                            st.session_state.cart[row['id']] = {'name': row['name'], 'price': float(row['price']) if row['price'] != '__' else 0.0, 'quantity': 0}
                        st.session_state.cart[row['id']]['quantity'] += 1
                        st.rerun()
        
        # Cart Summary with Minus Button
        if st.session_state.cart:
            total_items = sum(item['quantity'] for item in st.session_state.cart.values())
            total_price = sum(item['quantity'] * item['price'] for item in st.session_state.cart.values())
            col1, col2 = st.columns([4, 1])
            with col1:
                st.button(f"Cart: {total_items} Items ₹{total_price:.2f}")
            with col2:
                if st.button("-", key="remove_from_cart"):
                    for item_id in list(st.session_state.cart.keys()):
                        if st.session_state.cart[item_id]['quantity'] > 0:
                            st.session_state.cart[item_id]['quantity'] -= 1
                            if st.session_state.cart[item_id]['quantity'] == 0:
                                del st.session_state.cart[item_id]
                            st.rerun()
                            break
        
        # Order Confirmation
        if st.session_state.cart and st.button("Confirm Order", type="primary"):
            for item_id, item in st.session_state.cart.items():
                if item['quantity'] > 0:
                    # Update inventory stock
                    for inv_item in restaurants[st.session_state.active_restaurant]['inventory']:
                        if inv_item['id'] == item_id:
                            inv_item['stock'] -= item['quantity']
                            if inv_item['stock'] <= 0:
                                inv_item['available'] = False
                            break
                    # Update sales data
                    sale_found = False
                    for sale in restaurants[st.session_state.active_restaurant]['sales_data']:
                        if sale['item_id'] == item_id:
                            sale['quantity'] += item['quantity']
                            sale['revenue'] += item['quantity'] * item['price']
                            sale_found = True
                            break
                    if not sale_found and item['price'] != 0.0:
                        restaurants[st.session_state.active_restaurant]['sales_data'].append({
                            'item_id': item_id,
                            'quantity': item['quantity'],
                            'revenue': item['quantity'] * item['price']
                        })
                    # Update metrics
                    metrics['today_sales'] += item['quantity'] * item['price'] / 1000
                    metrics['items_sold'] += item['quantity']
                    low_stock_threshold = 5
                    metrics['low_stock_items'] = sum(1 for i in restaurants[st.session_state.active_restaurant]['inventory'] if i['stock'] <= low_stock_threshold and i['available'])
            st.session_state.cart = {}
            st.success("Order confirmed! Thank you for your purchase.")
            st.rerun()
