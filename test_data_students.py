import uuid
from database_setup import get_connection
import mysql.connector

# Import data
students = [
    ("Іваненко", "Іван", "Іванович", "Київ", "0987654321", 1, "інформаційних технологій", "Група 1", True),
    ("Петренко", "Петро", "Петрович", "Харків", "0981234567", 2, "економіки", "Група 2", False),
    ("Сидоренко", "Сидір", "Сидорович", "Одеса", "0982345678", 3, "аграрного менеджменту", "Група 3", False),
    ("Коваленко", "Ольга", "Михайлівна", "Львів", "0983456789", 1, "інформаційних технологій", "Група 1", False),
    ("Григоренко", "Ганна", "Григорівна", "Дніпро", "0984567890", 4, "економіки", "Група 2", True),
    ("Мельник", "Ірина", "Іванівна", "Полтава", "0985678901", 2, "аграрного менеджменту", "Група 3", False),
    ("Ткаченко", "Юрій", "Васильович", "Запоріжжя", "0986789012", 3, "інформаційних технологій", "Група 1", False),
    ("Онищенко", "Марина", "Сергіївна", "Суми", "0987890123", 4, "економіки", "Група 2", False),
    ("Лисенко", "Максим", "Олександрович", "Черкаси", "0988901234", 1, "аграрного менеджменту", "Група 3", False),
    ("Зеленський", "Богдан", "Петрович", "Рівне", "0989012345", 2, "інформаційних технологій", "Група 1", False),
    ("Шевченко", "Катерина", "Миколаївна", "Тернопіль", "0980123456", 3, "економіки", "Група 2", False)
]

# Database connection
conn = get_connection()
try:
    if conn is not None and conn.is_connected():
        cursor = conn.cursor()
        
        
        insert_student_query = """
        INSERT INTO Students (Id, LastName, Name, Surname, Address, Telephone, Level, Department, GroupName, Headman)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
       
        for student in students:
            student_data = (str(uuid.uuid4()),) + student 
            cursor.execute(insert_student_query, student_data)
        
        
        conn.commit()
        print("Test data inserted successfully into 'Students' table.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")