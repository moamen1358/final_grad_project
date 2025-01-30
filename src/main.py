# import streamlit as st
# import home
# import report
# import registration_form
# import real_time_prediction
# from chromadb import PersistentClient


# # Set page configuration
# st.set_page_config(layout="wide")

# # Streamlit app
# st.title("Face Recognition App")

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Real-Time Prediction", "Registration Form", "Report"])

# # Display the selected page
# if page == "Home":
#     home.show_home()

# elif page == "Real-Time Prediction":
#     real_time_prediction.show_real_time_prediction()

# elif page == "Registration Form":
#     registration_form.show_registration_form()

# elif page == "Report":
#     report.show_report()  # Call the function to show the report page

import streamlit as st
import home
import report
import registration_form
import real_time_prediction
from real_time_prediction import create_or_add_to_collection
from chromadb import PersistentClient

# Constants
CHROMA_STORE_PATH = "./store"

# Set page configuration
# st.set_page_config(layout="wide")

# Streamlit app
st.title("Face Recognition App")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Real-Time Prediction", "Registration Form", "Report"])

# Display the selected page
if page == "Home":
    home.show_home()

elif page == "Real-Time Prediction":
    real_time_prediction.show_real_time_prediction()

elif page == "Registration Form":
    registration_form.show_registration_form()

elif page == "Report":
    report.show_report()  # Call the function to show the report page

# Load embeddings to ChromaDB
create_or_add_to_collection("face_recognition", path_to_chroma=CHROMA_STORE_PATH)