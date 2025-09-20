import sqlite3

DB_PATH = "courses.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def add_course(title, duration, fee):
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO COURSES (title, duration, fee) VALUES (?, ?, ?)",
                (title, duration, fee)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")

def get_courses():
    try:
        with get_connection() as conn:
            cursor = conn.execute("SELECT id, title, duration, fee FROM COURSES")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving courses: {e}")
        return []

def get_course(course_id):
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, title, duration, fee FROM COURSES WHERE id = ?",
                (course_id,)
            )
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error retrieving course: {e}")
        return None

def update_course(course_id, title, duration, fee):
    try:
        with get_connection() as conn:
            conn.execute(
                "UPDATE COURSES SET title = ?, duration = ?, fee = ? WHERE id = ?",
                (title, duration, fee, course_id)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating course: {e}")

def delete_course(course_id):
    try:
        with get_connection() as conn:
            conn.execute(
                "DELETE FROM COURSES WHERE id = ?",
                (course_id,)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting course: {e}")

def create_table():
    try:
        with get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS COURSES (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    fee REAL NOT NULL
                )
                """
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        create_table()
    except Exception as e:
        print(f"Error creating table: {e}")
    # add_course("Python Basics", 30, 199.99)
    # print(get_courses())
    # update_course(1, "Advanced Python", 40, 249.99)
    # delete_course(1)
