import streamlit as st
import home
import report
import registration_form
import real_time_prediction
from real_time_prediction import create_or_add_to_collection

def show_app():
    CHROMA_STORE_PATH = "./store"
    st.title("Face Recognition App")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", [
        "Home", 
        "Real-Time Prediction", 
        "Registration Form", 
        "Report"
    ])

    if page == "Home":
        home.show_home()
    elif page == "Real-Time Prediction":
        real_time_prediction.show_real_time_prediction()
    elif page == "Registration Form":
        registration_form.show_registration_form()
    elif page == "Report":
        report.show_report()

    # ChromaDB integration
    create_or_add_to_collection("face_recognition", path_to_chroma=CHROMA_STORE_PATH)

    # Exit button
    st.sidebar.markdown("---")
    if st.sidebar.button("Exit", key="exit_button"):
        st.session_state.logged_in = False
        del st.query_params["logged_in"]
        st.rerun()

if __name__ == "__main__":
    # This block only runs when app.py is executed directly
    st.set_page_config(layout="wide")
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        show_app()
    else:
        import login
        login.main()