from database_setup import get_connection
import uuid
import mysql.connector

# Import data
subjects = [
    ("Математика", 60, 2),
    ("Інформатика", 90, 3),
    ("Економіка", 45, 1)
]

# database connect
conn = get_connection()
try:
    if conn is not None and conn.is_connected():
        cursor = conn.cursor()
        
        insert_subject_query = """
        INSERT INTO Subjects (Id, Name, Hours, Semesters)
        VALUES (%s, %s, %s, %s);
        """
        
        # data insert
        for subject in subjects:
            subject_data = (str(uuid.uuid4()),) + subject 
            cursor.execute(insert_subject_query, subject_data)
        
        conn.commit()
        print("Test data inserted successfully into 'Subjects' table.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")