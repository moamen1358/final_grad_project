import sqlite3

# def initialize_database():
#     # Connect to SQLite database (or create it if it doesn't exist)
#     conn = sqlite3.connect('attendance_system.db')
#     cursor = conn.cursor()

#     # Create the students table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
#     ''')

#     # Create the attendance_log table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS attendance_log (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         timestamp DATETIME NOT NULL
#     )
#     ''')

#     # Create the presidents_embeds table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS presidents_embeds (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         facial_features TEXT NOT NULL
#     )
#     ''')

#     # Commit the changes and close the connection
#     conn.commit()
#     cursor.close()
#     conn.close()

# initialize_database()


# import sqlite3
# import csv
# import json

# def import_students():
#     conn = sqlite3.connect('attendance_system.db')
#     cursor = conn.cursor()

#     with open('/home/invisa/Desktop/my_grad_streamlit/students.csv', 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             cursor.execute('''
#             INSERT INTO students (name)
#             VALUES (?)
#             ''', (row[0],))

#     conn.commit()
#     cursor.close()
#     conn.close()

# def import_attendance_log():
#     conn = sqlite3.connect('attendance_system.db')
#     cursor = conn.cursor()

#     with open('/home/invisa/Desktop/my_grad_streamlit/attendance_log.csv', 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             cursor.execute('''
#             INSERT INTO attendance_log (name, timestamp)
#             VALUES (?, ?)
#             ''', (row[0], row[1]))

#     conn.commit()
#     cursor.close()
#     conn.close()

# def import_presidents_embeds():
#     conn = sqlite3.connect('attendance_system.db')
#     cursor = conn.cursor()

#     with open('/home/invisa/Desktop/my_grad_streamlit/data_frames/presidents_embeds_moamen.csv', 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             name = row[0]
#             facial_features = json.loads(row[1])
#             cursor.execute('''
#             INSERT INTO presidents_embeds (name, facial_features)
#             VALUES (?, ?)
#             ''', (name, json.dumps(facial_features)))

#     conn.commit()
#     cursor.close()
#     conn.close()

# if __name__ == "__main__":
#     import_students()
#     import_attendance_log()
#     import_presidents_embeds()

# Function to get a connection to the SQLite database
def get_db_connection():
    return sqlite3.connect('attendance_system.db')

conn = get_db_connection()
cursor = conn.cursor()
query = "SELECT name FROM presidents_embeds "# WHERE name = ?
cursor.execute(query)#, ('akall',)
# count = cursor.fetchone()[0]
# print(count)
print(cursor.fetchall())
print(query)