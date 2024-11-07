import streamlit as st
from datetime import date
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_user, create_product, create_manufacturer, create_sales_purchase

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Streamlit app to handle user input and interact with the database
def main():
    print("starging")
    st.sidebar.image("static\image\logo.png", width=60)
    st.sidebar.title("Product Lifecycle Management System")    
    # Create sidebar with buttons (not a dropdown)
    st.sidebar.title("Navigation")
    user_button = st.sidebar.button("User")
    product_button = st.sidebar.button("Product")
    manufacturing_button = st.sidebar.button("Manufacturing")
    sales_purchase_button = st.sidebar.button("Sales and Purchase")

    # Show corresponding form based on the button clicked
    if user_button:
        user_form()
    elif product_button:
        product_form()
    elif manufacturing_button:
        manufacturing_form()
    elif sales_purchase_button:
        sales_purchase_form()

# Form for creating users
def user_form():
    st.header("User Information")
    with st.form("user_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
        mobile_no = st.text_input("Mobile No")
        email = st.text_input("Email")
        user_type = st.selectbox("User Type", ['supplier', 'customer', 'employee'])
        submit_button = st.form_submit_button(label="Submit")
        st.write(submit_button)
        
        if submit_button:
            st.write("Submit button clicked!")
            with next(get_db()) as db:
                print("user form")
                user = create_user(db, first_name, last_name, gender, mobile_no, email, user_type)
                st.success(f"User {user.first_name} {user.last_name} created successfully!")

# Form for creating products
def product_form():
    st.header("Product Information")
    with st.form("product_form"):
        product_name = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=0)
        unit = st.text_input("Unit")
        price = st.number_input("Price", min_value=0.0)
        expiration_date = st.date_input("Expiration Date", min_value=date.today())
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            with next(get_db()) as db:
                product = create_product(db, product_name, quantity, unit, price, expiration_date)
                st.success(f"Product {product.name} created successfully!")

# Form for creating manufacturing information
def manufacturing_form():
    st.header("Manufacturing Information")
    with st.form("manufacturing_form"):
        batch_number = st.text_input("Batch Number")
        bom = st.text_input("Bill of Materials (BOM)")
        manufacturing_date = st.date_input("Manufacturing Date", min_value=date.today())
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            with next(get_db()) as db:
                manufacturer = create_manufacturer(db, batch_number, bom, manufacturing_date)
                st.success(f"Manufacturing info for batch {manufacturer.batch_number} created successfully!")

# Form for creating sales and purchase information
def sales_purchase_form():
    st.header("Sales and Purchase Information")
    with st.form("sales_purchase_form"):
        transaction_type = st.selectbox("Transaction Type", ["Sale", "Purchase"])
        product_name = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=0)
        unit = st.text_input("Unit")
        supplier_name = st.text_input("Supplier Name")
        price = st.number_input("Price", min_value=0.0)
        transaction_date = st.date_input("Transaction Date", min_value=date.today())
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            with next(get_db()) as db:
                sales_purchase = create_sales_purchase(db, transaction_type, product_name, quantity, unit, supplier_name, price, transaction_date)
                st.success(f"{transaction_type} for {sales_purchase.product.name} created successfully!")

if __name__ == "__main__":
    main()
