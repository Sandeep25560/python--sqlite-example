import sqlite3

def connect_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    return conn, cursor

def fetch_user_by_name(cursor, name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    return cursor.fetchall()

def main():
    conn, cursor = connect_db()
    
    name = input("Enter the name to search for: ")

    users = fetch_user_by_name(cursor, name)
    
    if users:
        print(f"Users with the name '{name}':")
        for user in users:
            print(user)
    else:
        print(f"No users found with the name '{name}'.")

    conn.close()

if __name__ == "__main__":
    main()
