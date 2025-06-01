import psycopg2
from db.db_config import get_connection

class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def register(self):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                        (self.name, self.email, self.password, self.role))
            conn.commit()
            print("Registration successful.")
        except Exception as e:
            print("Registration failed:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def login(email, password):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT id, role FROM users WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
            if user:
                return user  # (user_id, role)
            else:
                return None
        except Exception as e:
            print("Login error:", e)
            return None
        finally:
            cur.close()
            conn.close()
