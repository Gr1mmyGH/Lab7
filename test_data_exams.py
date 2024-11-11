from database_setup import get_connection
import uuid
import random
from datetime import datetime, timedelta
import mysql.connector

# Database connect
conn = get_connection()

try:
    if conn is not None and conn.is_connected():
        cursor = conn.cursor()
        
        # Get students
        cursor.execute("SELECT Id FROM Students")
        student_ids = [row[0] for row in cursor.fetchall()]
        
        # Get subjects
        cursor.execute("SELECT Id FROM Subjects")
        subject_ids = [row[0] for row in cursor.fetchall()]

        insert_exam_query = """
        INSERT INTO Exams (Id, Date, Student, Subject, Grade)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        # Data generate worker
        for student_id in student_ids:
            for subject_id in subject_ids:
                exam_id = str(uuid.uuid4())  # Генерация уникального ID экзамена
                exam_date = datetime.now() - timedelta(days=random.randint(30, 365))  # Случайная дата экзамена
                grade = random.randint(2, 5)  # Случайная оценка от 2 до 5
                
              # prepare
                exam_data = (exam_id, exam_date.strftime('%Y-%m-%d'), student_id, subject_id, grade)
                
                # import data
                cursor.execute(insert_exam_query, exam_data)
        

        conn.commit()
        print("Test data inserted successfully into 'Exams' table.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")