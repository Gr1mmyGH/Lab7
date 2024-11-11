import mysql.connector

# Method of db connect
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="university_user",
            password="university_password",
            database="university_db"
        )
        
        if conn.is_connected():
            print("Connected to the database successfully.")
            return conn
        else:
            print("Problem with database connection.")
            return None

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

# Table create
try:
    conn = get_connection() # connect to db
    if conn is not None and conn.is_connected():
        
        cursor = conn.cursor()

        create_students_table_query = """
        CREATE TABLE IF NOT EXISTS Students (
            Id CHAR(36) PRIMARY KEY,
            LastName VARCHAR(50) NOT NULL,
            Name VARCHAR(50) NOT NULL,
            Surname VARCHAR(50),
            Address VARCHAR(100),
            Telephone VARCHAR(15),
            Level VARCHAR(20),
            Department VARCHAR(50),
            GroupName VARCHAR(50),
            Headman BOOLEAN
        );
        """
        
        cursor.execute(create_students_table_query)
        conn.commit()  
        print("Table 'Students' created successfully.")
        
        create_subjects_table_query = """
        CREATE TABLE IF NOT EXISTS Subjects (
            Id CHAR(36) PRIMARY KEY,
            Name VARCHAR(50) NOT NULL,
            Hours INT,
            Semesters INT
        );
        """
        
        cursor.execute(create_subjects_table_query)
        conn.commit()
        print("Table 'Subjects' created successfully.")
        
        create_exams_table_query = """
        CREATE TABLE IF NOT EXISTS Exams (
            Id CHAR(36) PRIMARY KEY,
            Date DATE NOT NULL,
            Student CHAR(36),
            Subject CHAR(36),
            Grade INT CHECK (Grade IN (2, 3, 4, 5)),
            FOREIGN KEY (Student) REFERENCES Students(Id) ON DELETE CASCADE,
            FOREIGN KEY (Subject) REFERENCES Subjects(Id) ON DELETE CASCADE
        );
        """
        
        cursor.execute(create_exams_table_query)
        conn.commit()
        print("Table 'Exams' created successfully.")
    
    else:
        print("Could not establish database connection to create tables.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")