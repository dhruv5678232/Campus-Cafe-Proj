import streamlit as st
import plotly.express as px
import pandas as pd

# Mock data with ensured 'metrics' key for all restaurants
restaurants = {
    'rise': {
        'name': 'Rise - Ready to Serve',
        'theme_gradient': 'linear-gradient(135deg, #8B4513, #D2691E)',
        'inventory': [
            {'id': 'rise_tea', 'name': 'Tea [Medium]', 'stock': 47, 'max_stock': 50, 'category': 'drink', 'available': True},
            {'id': 'rise_chicken_puff', 'name': 'Chicken Puff', 'stock': 18, 'max_stock': 20, 'category': 'pastry', 'available': True},
            {'id': 'rise_coffee', 'name': 'Coffee', 'stock': 18, 'max_stock': 20, 'category': 'drink', 'available': True},
            {'id': 'rise_veggie_puff', 'name': 'Veggie Puff', 'stock': 22, 'max_stock': 25, 'category': 'pastry', 'available': True},
            {'id': 'rise_egg_puff', 'name': 'Egg Puff', 'stock': 8, 'max_stock': 10, 'category': 'pastry', 'available': True},
            {'id': 'rise_black_forest', 'name': 'Black Forest Pastry', 'stock': 15, 'max_stock': 25, 'category': 'pastry', 'available': True},
            {'id': 'rise_chocolate_pastry', 'name': 'Chocolate Pastry', 'stock': 10, 'max_stock': 25, 'category': 'pastry', 'available': True},
            {'id': 'rise_red_velvet', 'name': 'Red Velvet Pastry', 'stock': 12, 'max_stock': 20, 'category': 'pastry', 'available': True},
            {'id': 'rise_samosa', 'name': 'Samosa Pastry', 'stock': 20, 'max_stock': 40, 'category': 'pastry', 'available': False},
            {'id': 'rise_korean_cheese', 'name': 'Korean Cream Cheese Bun', 'stock': 1, 'max_stock': 15, 'category': 'pastry', 'available': True},
            {'id': 'rise_hashbrown', 'name': 'Hashbrown Omelette', 'stock': 12, 'max_stock': 20, 'category': 'meal', 'available': True},
            {'id': 'rise_omlette', 'name': 'Omelette', 'stock': 25, 'max_stock': 30, 'category': 'meal', 'available': True},
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
            {'id': 'embers_tea', 'name': 'Tea [Medium]', 'stock': 45, 'max_stock': 50, 'category': 'drink', 'available': True},
            {'id': 'embers_chicken_biryani', 'name': 'Chicken Biryani', 'stock': 20, 'max_stock': 25, 'category': 'meal', 'available': True},
            {'id': 'embers_coffee', 'name': 'Coffee', 'stock': 15, 'max_stock': 20, 'category': 'drink', 'available': True},
            {'id': 'embers_veg_biryani', 'name': 'Veg Biryani', 'stock': 18, 'max_stock': 20, 'category': 'meal', 'available': True},
            {'id': 'embers_dal_rice', 'name': 'Dal Rice', 'stock': 10, 'max_stock': 15, 'category': 'meal', 'available': True},
            {'id': 'embers_naan', 'name': 'Garlic Naan', 'stock': 12, 'max_stock': 20, 'category': 'snack', 'available': True},
            {'id': 'embers_gulab_jamun', 'name': 'Gulab Jamun', 'stock': 8, 'max_stock': 15, 'category': 'dessert', 'available': True},
            {'id': 'embers_samosa', 'name': 'Vegetable Samosa', 'stock': 25, 'max_stock': 30, 'category': 'snack', 'available': True},
        ],
        'sales_data': [
            {'item_id': 'embers_chicken_biryani', 'quantity': 80, 'revenue': 640},
            {'item_id': 'embers_tea', 'quantity': 60, 'revenue': 180},
            {'id': 'embers_veg_biryani', 'quantity': 30, 'revenue': 240},
            {'id': 'embers_dal_rice', 'quantity': 20, 'revenue': 100},
        ],
        'ratings': [
            {'item_id': 'embers_tea', 'rating': 4.3, 'comment': 'Perfect balance of spices.', 'timestamp': '2023-01-14'},
            {'item_id': 'embers_chicken_biryani', 'rating': 4.7, 'comment': 'Excellent taste and portion.', 'timestamp': '2023-01-14'},
            {'item_id': 'embers_coffee', 'rating': 3.9, 'comment': 'Needs more cream.', 'timestamp': '2023-01-14'},
            {'item_id': 'embers_veg_biryani', 'rating': 4.2, 'comment': 'Great for vegetarians.', 'timestamp': '2023-01-14'},
            {'item_id': 'embers_samosa', 'rating': 4.0, 'comment': 'Crisp but slightly oily.', 'timestamp': '2023-01-14'},
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
            'items_sold': 150,
            'low_stock_items': 2
        },
        'weekly_revenue': [5000, 5100, 5200, 5150, 5050, 4900, 4600]
    }
}

# Streamlit app
st.set_page_config(page_title="Restaurant Management Dashboard", layout="wide")

if 'active_view' not in st.session_state:
    st.session_state.active_view = 'admin'
if 'active_restaurant' not in st.session_state:
    st.session_state.active_restaurant = 'rise'

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
    .stProgress>span {{
        background-color: #8B4513;
    }}
    .css-1aumxhk {{
        background-color: #f0e6d2;
    }}
</style>
""", unsafe_allow_html=True)

# Header Metrics with fallback
current_restaurant = restaurants.get(st.session_state.active_restaurant, {})
metrics = current_restaurant.get('metrics', {'today_sales': 0, 'gross_cost': 0, 'gross_profit': 0, 'net_profit': 0, 'items_sold': 0, 'low_stock_items': 0})
st.title(current_restaurant.get('name', 'Restaurant Dashboard'))
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Today's Sales", f"₹{metrics['today_sales']:,}", f"₹{24.825 if st.session_state.active_restaurant == 'rise' else 28.750:,} before expenses")
col2.metric("Gross Cost", f"₹{metrics['gross_cost']:,}", f"₹{22.150 if st.session_state.active_restaurant == 'rise' else 25.500:,}")
col3.metric("Gross Profit", f"₹{metrics['gross_profit']:,}", f"₹{2.675 if st.session_state.active_restaurant == 'rise' else 3.250:,}")
col4.metric("Net Profit", f"₹{metrics['net_profit']:,}", f"₹{1.890 if st.session_state.active_restaurant == 'rise' else 2.300:,}")
col5.metric("Items Sold", f"{metrics['items_sold']:,}", f"+{127 if st.session_state.active_restaurant == 'rise' else 150} today")
col6, col7 = st.columns([3, 2])
col6.metric("Low Stock Items", f"{metrics['low_stock_items']:,}", f"{3 if st.session_state.active_restaurant == 'rise' else 2} new")

# Main Content
if st.session_state.active_view == 'admin':
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Inventory Overview")
        df_inv = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('inventory', []))
        if not df_inv.empty:
            df_inv['stock_pct'] = (df_inv['stock'] / df_inv['max_stock'] * 100).round(1)
            for _, row in df_inv.iterrows():
                color = 'normal' if row['stock_pct'] > 30 else 'inverse'
                st.metric(label=row['name'], value=f"{row['stock']}/{row['max_stock']}", delta=f"{row['stock_pct']}%", delta_color=color)
                st.progress(row['stock_pct'] / 100)
                st.caption(f"Category: {row['category']} | Available: {'Yes' if row['available'] else 'No'}")
                st.toggle("Availability", value=row['available'], key=f"toggle_{row['id']}")
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
        else:
            st.info("No sales data available.")
    
    with col3:
        st.subheader("Item Ratings & Reviews")
        df_ratings = pd.DataFrame(restaurants.get(st.session_state.active_restaurant, {}).get('ratings', []))
        if not df_ratings.empty:
            for _, row in df_ratings.iterrows():
                st.metric(label=row['name'] if 'name' in row else row['item_id'], value=f"{row['rating']} ⭐", delta=f"{len(df_ratings[df_ratings['item_id'] == row['item_id']])} reviews")
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
                            st.experimental_rerun()
                with col3:
                    if row['status'] == 'pending':
                        if st.button("Reject", key=f"reject_{row['item_name']}"):
                            row['status'] = 'rejected'
                            st.experimental_rerun()
    else:
        st.info("No suggestions available.")

elif st.session_state.active_view == 'student':
    # Student Dashboard
    tab1, tab2, tab3 = st.tabs(["Top Items", "Rate an Item", "Suggest New Item"])
    
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
                new_rating = {'item_id': selected_item_id, 'rating': rating, 'comment': comment, 'timestamp': '2025-09-16'}
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
                        'timestamp': '2025-09-16'
                    }
                    if 'suggestions' not in st.session_state:
                        st.session_state.suggestions = restaurants[st.session_state.active_restaurant].get('suggestions', []).copy()
                    st.session_state.suggestions.append(new_suggestion)
                    st.success("Your suggestion has been submitted! We'll review it soon.")
                else:
                    st.error("Please provide at least an item name and description.")
