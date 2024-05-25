import streamlit as st

# Set up the title and subheader
st.title("Cafe Management System")
st.subheader("Welcome to the Cafe Management System")

# Display the menu in the sidebar
st.sidebar.header("Menu")
menu_items = {"Pizza: Rs110": 110, "Veg Burger: Rs49": 49, "Coffee: Rs40": 40, "Pasta: Rs80": 80}
for item, price in menu_items.items():
    st.sidebar.write(f"{item}")

# Initialize order details
order = {}
order_total = 0

# Function to add item to the order
def add_item_to_order(item_name):
    global order_total
    normalized_item_name = next((name for name in menu_items if item_name.lower() in name.lower()), None)
    if normalized_item_name:
        order_total += menu_items[normalized_item_name]
        if normalized_item_name in order:
            order[normalized_item_name] += 1
        else:
            order[normalized_item_name] = 1
        st.success(f"Added {normalized_item_name} to your order. Current total: Rs{order_total}")
    else:
        st.error(f"Ordered item {item_name} is not available.")

# User selects an item to order
st.write("### Place your order")
item_1 = st.text_input("Enter the name of the item you want to order:")

if st.button("Add to Order"):
    add_item_to_order(item_1)

# Calculate the total amount for all items in the order
order_total = sum(menu_items[item] * order[item] for item in order)

# Option to add another item
st.write("### Add another item to your order")
another_order = st.radio("Do you want to add another item?", ("No", "Yes"))

if another_order == "Yes":
    item_2 = st.text_input("Enter the name of the second item you want to order:")
    if st.button("Add Second Item"):
        add_item_to_order(item_2)

        # Recalculate the total amount for all items in the order
        order_total = sum(menu_items[item] * order[item] for item in order)

# Display the order summary
if order:
    st.write("### Order Summary")
    for item, quantity in order.items():
        st.write(f"{item}: {quantity} x Rs{menu_items[item]} = Rs{quantity * menu_items[item]}")
    st.write(f"**Total Amount to Pay: Rs{order_total}**")

# Add a footer
st.sidebar.write("### Thank you for visiting our cafe!")
