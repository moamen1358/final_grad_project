import streamlit as st
import sqlite3
import app

# Must be the absolute first Streamlit command
# st.set_page_config(layout="wide")

def create_connection():
    conn = sqlite3.connect('attendance_system.db')
    return conn

def check_credentials(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def show_login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.query_params["logged_in"] = "True"
            st.rerun()
        else:
            st.error("Invalid username or password")

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Check query params
    if "logged_in" in st.query_params and st.query_params["logged_in"] == "True":
        st.session_state.logged_in = True

    if st.session_state.logged_in:
        app.show_app()  # Call app without reinitializing page config
    else:
        show_login()

if __name__ == "__main__":
    main()