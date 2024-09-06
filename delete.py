import sqlite3

def connect_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    return conn, cursor

def delete_user(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

def main():
    conn, cursor = connect_db()
    
    try:
        user_id = int(input("Enter the user ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        conn.close()
        return

    delete_user(cursor, user_id)
    
    conn.commit()
    print(f"User with ID {user_id} deleted successfully.")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
      print(row) 
      conn.close()

if __name__ == "__main__":
    main()
