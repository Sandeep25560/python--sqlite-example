import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    grade REAL
)''')
def insert_student(name, grade):
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    connection.commit()

insert_student('Sandeep', 85.5)
insert_student('Anudeep', 92.3)

def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print("Students after insertion:")
fetch_students()

def update_student_grade(student_id, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    connection.commit()

update_student_grade(2, 95.0)

print("\nStudents after updating grade:")
fetch_students()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()

delete_student(1)

print("\nStudents after deleting Alice:")
fetch_students()
try:
    cursor.execute("SELECT * FROM Employees")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
connection.close()
