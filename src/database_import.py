import streamlit as st
import sqlite3
import pandas as pd

# Function to create database and tables
def initialize_database():
    conn = sqlite3.connect('attendance_system.db')
    cursor = conn.cursor()

    # Create the students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create the attendance_log table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        timestamp DATETIME NOT NULL
    )
    ''')

    # Create the presidents_embeds table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS presidents_embeds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        facial_features TEXT NOT NULL
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

# Function to retrieve and display the database structure
def display_database_structure():
    try:
        conn = sqlite3.connect('attendance_system.db')
        cursor = conn.cursor()

        # Retrieve the database name
        database_name = 'attendance_system.db'

        # Retrieve the tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        st.write(f"**Database: {database_name}**")
        for table in tables:
            table_name = table[0]
            st.write(f"  - **Table: {table_name}**")
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            for column in columns:
                st.write(f"    - {column[1]} ({column[2]})")

        cursor.close()
        conn.close()
    except sqlite3.Error as err:
        st.error(f"Error: {err}")

# Streamlit app for database import
def show_database_import_page():
    st.title("SQLite Database and CSV Import")

    # Display the database structure
    st.write("## Database Structure")
    display_database_structure()

    # Create database and table
    if st.button("Create Database and Tables"):
        initialize_database()
        st.success("Database and tables created successfully")

# Call the function to show the database import page
show_database_import_page()