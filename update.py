import sqlite3

def connect_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    return conn, cursor

def update_user_age(cursor, user_id, new_age):
    
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))

def main():
    conn, cursor = connect_db()
    
    try:
        user_id = int(input("Enter the user ID to update: "))
        new_age = int(input("Enter the new age: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        conn.close()
        return

    update_user_age(cursor, user_id, new_age)
    
    conn.commit()
    print(f"User with ID {user_id} updated to age {new_age}.")

    conn.close()

if __name__ == "__main__":
    main()
