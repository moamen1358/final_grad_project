# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import sqlite3
# import io

# # Set the page layout to wide
# st.set_page_config(layout="wide")

# # Function to get a connection to the SQLite database
# def get_db_connection():
#     return sqlite3.connect('attendance_system.db')

# # Function to get attendance data from the database
# def get_attendance_data():
#     conn = get_db_connection()
#     query = "SELECT name, timestamp FROM attendance_log"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Function to get list of registered students from the database
# def get_registered_students():
#     conn = get_db_connection()
#     query = "SELECT name FROM students"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df['name'].tolist()

# # Function to add a person to the database
# def add_person(name):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = "SELECT COUNT(*) FROM attendance_log WHERE name = ?"
#     cursor.execute(query, (name,))
#     count = cursor.fetchone()[0]
#     if count == 0:
#         query = "INSERT INTO attendance_log (name, timestamp) VALUES (?, ?)"
#         cursor.execute(query, (name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
#         conn.commit()
#     else:
#         raise ValueError(f"Person '{name}' already exists in the attendance log.")
#     cursor.close()
#     conn.close()

# # Function to delete attendance log from the database
# def delete_attendance_log(name):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = "DELETE FROM attendance_log WHERE name = ?"
#     cursor.execute(query, (name,))
#     if cursor.rowcount == 0:
#         raise ValueError(f"Person '{name}' does not exist in the attendance log.")
#     conn.commit()
#     cursor.close()
#     conn.close()

# def show_report():
#     st.header("Report")
#     st.write("Display reports or logs here.")

#     # Display attendance data
#     df = get_attendance_data()
#     attendance_placeholder = st.empty()
#     attendance_placeholder.dataframe(df, width=1500)  # Set the width to make it wider

#     # Export to Excel
#     buffer = io.BytesIO()
#     with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
#         df.to_excel(writer, index=False, sheet_name='Attendance')
#     st.download_button(
#         label="Download attendance as Excel",
#         data=buffer,
#         file_name='attendance.xlsx',
#         mime='application/vnd.ms-excel'
#     )

#     # Add a person
#     st.subheader("Add a Person")
#     student_names = get_registered_students()
#     add_name = st.selectbox("Select a name to add", student_names)
#     if st.button("Add"):
#         if add_name:
#             try:
#                 add_person(add_name)
#                 st.success(f"Successfully added {add_name}")
#                 # Update the display report log
#                 df = get_attendance_data()
#                 attendance_placeholder.dataframe(df, width=1500)  # Update the width to make it wider
#             except ValueError as e:
#                 st.error(e)
#             except Exception as e:
#                 st.error(f"Error adding {add_name}: {e}")
#         else:
#             st.error("Please select a name")

#     # Delete attendance log
#     st.subheader("Delete Attendance Log")
#     attendance_df = get_attendance_data()
#     attendance_names = attendance_df['name'].unique().tolist()
#     delete_name = st.selectbox("Select a name to delete attendance log", attendance_names)
#     if st.button("Delete Attendance Log"):
#         if delete_name:
#             try:
#                 delete_attendance_log(delete_name)
#                 st.success(f"Successfully deleted attendance log for {delete_name}")
#                 # Update the display report log
#                 df = get_attendance_data()
#                 attendance_placeholder.dataframe(df, width=1500)  # Update the width to make it wider
#             except ValueError as e:
#                 st.error(e)
#             except Exception as e:
#                 st.error(f"Error deleting attendance log: {e}")
#         else:
#             st.error("Please select a name")

import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import io
from real_time_prediction import create_or_add_to_collection
# Constants
DATABASE_PATH = 'attendance_system.db'
CHROMA_STORE_PATH = "./store"


# Set the page layout to wide
st.set_page_config(layout="wide")

# Function to get a connection to the SQLite database
def get_db_connection():
    return sqlite3.connect(DATABASE_PATH)

# Function to get attendance data from the database
def get_attendance_data():
    conn = get_db_connection()
    query = "SELECT name, timestamp FROM attendance_log"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to get list of registered students from the database
def get_registered_students():
    conn = get_db_connection()
    query = "SELECT name FROM students"
    df = pd.read_sql(query, conn)
    conn.close()
    return df['name'].tolist()

# Function to add a person to the database
def add_person(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM attendance_log WHERE name = ?"
    cursor.execute(query, (name,))
    count = cursor.fetchone()[0]
    if count == 0:
        query = "INSERT INTO attendance_log (name, timestamp) VALUES (?, ?)"
        cursor.execute(query, (name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        create_or_add_to_collection("face_recognition", path_to_chroma=CHROMA_STORE_PATH)
    else:
        raise ValueError(f"Person '{name}' already exists in the attendance log.")
    cursor.close()
    conn.close()

# Function to delete attendance log from the database
def delete_attendance_log(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM attendance_log WHERE name = ?"
    cursor.execute(query, (name,))
    if cursor.rowcount == 0:
        raise ValueError(f"Person '{name}' does not exist in the attendance log.")
    conn.commit()
    cursor.close()
    conn.close()

def show_report():
    st.header("Report")
    st.write("Display reports or logs here.")

    # Display attendance data
    df = get_attendance_data()
    attendance_placeholder = st.empty()
    attendance_placeholder.dataframe(df, width=1500)  # Set the width to make it wider

    # Export to Excel
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Attendance')
    st.download_button(
        label="Download attendance as Excel",
        data=buffer,
        file_name='attendance.xlsx',
        mime='application/vnd.ms-excel'
    )

    # Add a person
    st.subheader("Add a Person")
    student_names = get_registered_students()
    add_name = st.selectbox("Select a name to add", student_names)
    if st.button("Add"):
        if add_name:
            try:
                add_person(add_name)
                st.success(f"Successfully added {add_name}")
                # Update the display report log
                df = get_attendance_data()
                attendance_placeholder.dataframe(df, width=1500)  # Update the width to make it wider
            except ValueError as e:
                st.error(e)
            except Exception as e:
                st.error(f"Error adding {add_name}: {e}")
        else:
            st.error("Please select a name")

    # Delete attendance log
    st.subheader("Delete Attendance Log")
    attendance_df = get_attendance_data()
    attendance_names = attendance_df['name'].unique().tolist()
    delete_name = st.selectbox("Select a name to delete attendance log", attendance_names)
    if st.button("Delete Attendance Log"):
        if delete_name:
            try:
                delete_attendance_log(delete_name)
                st.success(f"Successfully deleted attendance log for {delete_name}")
                # Update the display report log
                df = get_attendance_data()
                attendance_placeholder.dataframe(df, width=1500)  # Update the width to make it wider
            except ValueError as e:
                st.error(e)
            except Exception as e:
                st.error(f"Error deleting attendance log: {e}")
        else:
            st.error("Please select a name")