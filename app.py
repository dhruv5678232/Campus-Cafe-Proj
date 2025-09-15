import streamlit as st
import plotly.express as px
import pandas as pd

# Mock data based on screenshot
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
        'inventory': [],
        'sales_data': [],
        'ratings': [],
        'suggestions': [],
        'metrics': {},
        'weekly_revenue': []
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

# Header Metrics
st.title(restaurants[st.session_state.active_restaurant]['name'])
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Today's Sales", f"₹{restaurants[st.session_state.active_restaurant]['metrics']['today_sales']:,}", "₹24,825 before expenses")
col2.metric("Gross Cost", f"₹{restaurants[st.session_state.active_restaurant]['metrics']['gross_cost']:,}", "₹22,150")
col3.metric("Gross Profit", f"₹{restaurants[st.session_state.active_restaurant]['metrics']['gross_profit']:,}", "₹2,675")
col4.metric("Net Profit", f"₹{restaurants[st.session_state.active_restaurant]['metrics']['net_profit']:,}", "₹1,890")
col5.metric("Items Sold", f"{restaurants[st.session_state.active_restaurant]['metrics']['items_sold']:,}", "+127 today")
col6, col7 = st.columns([3, 2])
col6.metric("Low Stock Items", f"{restaurants[st.session_state.active_restaurant]['metrics']['low_stock_items']:,}", "3 new")

# Main Content
if st.session_state.active_view == 'admin':
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Inventory Overview")
        df_inv = pd.DataFrame(restaurants[st.session_state.active_restaurant]['inventory'])
        df_inv['stock_pct'] = (df_inv['stock'] / df_inv['max_stock'] * 100).round(1)
        
        for _, row in df_inv.iterrows():
            color = 'normal' if row['stock_pct'] > 30 else 'inverse'
            st.metric(label=row['name'], value=f"{row['stock']}/{row['max_stock']}", delta=f"{row['stock_pct']}%", delta_color=color)
            st.progress(row['stock_pct'] / 100)
            st.caption(f"Category: {row['category']} | Available: {'Yes' if row['available'] else 'No'}")
            st.toggle("Availability", value=row['available'], key=f"toggle_{row['id']}")
    
    with col2:
        st.subheader("Sales Analytics")
        df_sales = pd.DataFrame(restaurants[st.session_state.active_restaurant]['sales_data'])
        df_sales = df_sales.merge(pd.DataFrame(restaurants[st.session_state.active_restaurant]['inventory'])[['id', 'name']], left_on='item_id', right_on='id', how='left')
        df_sales = df_sales[['name', 'quantity', 'revenue']].head(4)
        
        if not df_sales.empty:
            fig_bar = px.bar(df_sales, x='name', y='quantity', title='Top 4 Selling Items',
                             color='revenue', color_continuous_scale='Viridis')
            st.plotly_chart(fig_bar, use_container_width=True)
            
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            fig_line = px.line(x=days, y=restaurants[st.session_state.active_restaurant]['weekly_revenue'],
                               title='Weekly Revenue Trend (₹)', markers=True)
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.info("No sales data available.")
    
    with col3:
        st.subheader("Item Ratings & Reviews")
        df_ratings = pd.DataFrame(restaurants[st.session_state.active_restaurant]['ratings'])
        for _, row in df_ratings.iterrows():
            st.metric(label=row['name'] if 'name' in row else row['item_id'], value=f"{row['rating']} ⭐", delta=f"{len(df_ratings[df_ratings['item_id'] == row['item_id']])} reviews")
            st.write(row['comment'])
            st.caption(f"Reviewed on: {row['timestamp']}")
    
    # Suggestions Panel
    st.subheader("Student Suggestions")
    df_sugg = pd.DataFrame(restaurants[st.session_state.active_restaurant]['suggestions'])
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

elif st.session_state.active_view == 'student':
    # Student Dashboard
    tab1, tab2, tab3 = st.tabs(["Top Items", "Rate an Item", "Suggest New Item"])
    
    with tab1:
        st.subheader("Top Items")
        df_inv = pd.DataFrame(restaurants[st.session_state.active_restaurant]['inventory'])
        df_ratings = pd.DataFrame(restaurants[st.session_state.active_restaurant]['ratings'])
        df_top = df_ratings.groupby('item_id').agg({'rating': 'mean', 'comment': 'count'}).reset_index()
        df_top = df_top.merge(df_inv[['id', 'name']], left_on='item_id', right_on='id', how='left')
        df_top = df_top.sort_values('rating', ascending=False).head(10)
        
        if not df_top.empty:
            fig = px.bar(df_top, x='name', y='rating', title='Top Rated Items',
                         color='comment', hover_data=['comment'])
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df_top, use_container_width=True)
        else:
            st.info("No items available.")
    
    with tab2:
        st.subheader("Rate an Item")
        df_items = pd.DataFrame(restaurants[st.session_state.active_restaurant]['inventory'])
        item_names = df_items[df_items['available']]['name'].tolist()
        
        if item_names:
            item_name = st.selectbox("Select an Item to Rate", item_names)
            selected_item_id = df_items[df_items['name'] == item_name]['id'].iloc[0]
            
            rating = st.slider("Your Rating", 1, 5, 3, help="1-5 stars")
            comment = st.text_area("Comments (optional)", placeholder="Tell us about your experience...")
            
            if st.button("Submit Rating", type="primary"):
                new_rating = {'item_id': selected_item_id, 'rating': rating, 'comment': comment, 'timestamp': '2023-01-16'}
                if 'ratings' not in st.session_state:
                    st.session_state.ratings = restaurants[st.session_state.active_restaurant]['ratings'].copy()
                st.session_state.ratings.append(new_rating)
                st.success("Thank you for your rating! It has been submitted.")
        else:
            st.warning("No available items to rate.")
    
    with tab3:
        st.subheader("Suggest a New Item")
        with st.form("suggestion_form", clear_on_submit=True):
            item_name = st.text_input("Item Name", placeholder="e.g., Vegan Burger")
            category = st.selectbox("Category", ['drink', 'snack', 'pastry', 'meal'])
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
                        'timestamp': '2023-01-16'
                    }
                    if 'suggestions' not in st.session_state:
                        st.session_state.suggestions = restaurants[st.session_state.active_restaurant]['suggestions'].copy()
                    st.session_state.suggestions.append(new_suggestion)
                    st.success("Your suggestion has been submitted! We'll review it soon.")
                else:
                    st.error("Please provide at least an item name and description.")
