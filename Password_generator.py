import streamlit as st
import string
import random
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- 1. DATABASE SETUP ---
try:
    DB_URL = st.secrets["DB_URL"]
    if DB_URL.startswith("postgres://"):
        DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)
    
    engine = create_engine(DB_URL)
    Base = declarative_base()
except Exception as e:
    st.error("Could not find Database Secret. Please check Streamlit Settings.")
    st.stop()

class PasswordVault(Base):
    __tablename__ = 'user_passwords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    website = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# --- 2. PASSWORD GENERATION LOGIC ---
def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        pwd = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.isupper() for c in pwd) and 
            any(c.isdigit() for c in pwd) and 
            any(c in string.punctuation for c in pwd)):
            return pwd

# --- 3. STREAMLIT UI ---
def main():
    st.set_page_config(page_title="Strongest Password Manager", page_icon="🛡️")
    st.title("🛡️ Strongest Password Manager")
    st.markdown("🔒 *Powered by Aiven PostgreSQL & SQLAlchemy*")

    # Tabs for navigation
    tab1, tab2 = st.tabs(["✨ Generate & Save", "🔍 Retrieve"])

    with tab1:
        st.subheader("Generate New Credentials")
        
        # Create two columns: one for the slider and one for the button
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Slider moved from sidebar to main area
            pwd_length = st.slider("Select Password Length", 8, 32, 16)
        
        with col2:
            # Button placed next to the slider
            st.write("##") # Adds a little vertical alignment space
            gen_button = st.button("Generate")

        if gen_button:
            new_pw = generate_secure_password(pwd_length)
            st.session_state['generated_pw'] = new_pw
            st.success("New secure password generated!")
            st.code(new_pw, language="text")

        if 'generated_pw' in st.session_state:
            st.divider()
            st.write("### 💾 Save to Vault")
            site = st.text_input("Website or App Name (e.g., Facebook)").lower()
            user = st.text_input("Username or Email")
            
            if st.button("Confirm & Save to Cloud"):
                if site and user:
                    try:
                        new_entry = PasswordVault(
                            website=site, 
                            username=user, 
                            password=st.session_state['generated_pw']
                        )
                        session.add(new_entry)
                        session.commit()
                        st.balloons()
                        st.success(f"Successfully saved credentials for {site}!")
                        del st.session_state['generated_pw']
                    except Exception as e:
                        session.rollback()
                        st.error(f"Database Error: {e}")
                else:
                    st.warning("Please fill in both fields.")

    with tab2:
        st.subheader("Search your Vault")
        search_target = st.text_input("Enter Website Name to Search").lower()
        
        if st.button("Retrieve Password"):
            if search_target:
                result = session.query(PasswordVault).filter_by(website=search_target).first()
                if result:
                    st.info(f"**Credentials for {search_target.capitalize()}:**")
                    st.write(f"**Username:** {result.username}")
                    st.write(f"**Password:**")
                    st.code(result.password, language="text")
                else:
                    st.error(f"No entry found for '{search_target}'.")
            else:
                st.warning("Please enter a website name.")

if __name__ == "__main__":
    main()
