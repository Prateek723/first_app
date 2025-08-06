import streamlit as st
import hashlib

# Configuration
ACCESS_CODE = "hellothere"  # Change this to your desired access code
# For better security, you can hash the access code
ACCESS_CODE_HASH = hashlib.sha256(ACCESS_CODE.encode()).hexdigest()

def check_access_code(input_code):
    """Check if the provided access code is correct"""
    input_hash = hashlib.sha256(input_code.encode()).hexdigest()
    return input_hash == ACCESS_CODE_HASH

def show_login_page():
    """Display the login page"""
    st.title("🔐 Access Required")
    st.write("Please enter the access code to continue:")
    
    # Create a form for better UX
    with st.form("login_form"):
        access_code_input = st.text_input("Access Code", type="password", placeholder="Enter access code")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if access_code_input:
                if check_access_code(access_code_input):
                    st.session_state.authenticated = True
                    st.success("✅ Access granted! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Invalid access code. Please try again.")
            else:
                st.warning("⚠️ Please enter an access code.")

def show_protected_content():
    """Display the protected content after authentication"""
    # Header with logout option
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🎉 Welcome to the Protected Area!")
    with col2:
        if st.button("Logout", type="secondary"):
            st.session_state.authenticated = False
            st.rerun()
    
    st.write("---")
    
    # Your main application content goes here
    st.header("Your Protected Content")
    st.write("This content is only visible to authenticated users.")
    
    # Example protected content
    st.subheader("Sample Features:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📊 Data Analytics")
        st.write("Access to sensitive data and analytics")
        
        if st.button("View Analytics"):
            st.success("Analytics loaded successfully!")
    
    with col2:
        st.info("⚙️ Admin Panel")
        st.write("Administrative functions and settings")
        
        if st.button("Open Admin Panel"):
            st.success("Admin panel opened!")
    
    # Sample data display
    st.subheader("Sample Protected Data:")
    import pandas as pd
    import numpy as np
    
    # Generate sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=10),
        'Value': np.random.randint(100, 1000, 10),
        'Category': np.random.choice(['A', 'B', 'C'], 10)
    })
    
    st.dataframe(data, use_container_width=True)
    
    # Sample chart
    st.subheader("Sample Chart:")
    st.line_chart(data.set_index('Date')['Value'])

def main():
    """Main application function"""
    # Initialize authentication state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Set page config
    st.set_page_config(
        page_title="Secure App",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Hide Streamlit menu and footer for cleaner look (optional)
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Route to appropriate page based on authentication status
    if st.session_state.authenticated:
        show_protected_content()
    else:
        show_login_page()

if __name__ == "__main__":
    main()