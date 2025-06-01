# from db.db_config import connect
from datetime import datetime
from db.db_config import get_connection

class Booking:
    def __init__(self, user_id, car_id, start_date, end_date):
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date

    def book(self):
        try:
            conn = get_connection()
            cur = conn.cursor()

            fmt = "%Y-%m-%d"
            days = (datetime.strptime(self.end_date, fmt) - datetime.strptime(self.start_date, fmt)).days
            cur.execute("SELECT min_days, max_days FROM cars WHERE id = %s", (self.car_id,))
            car = cur.fetchone()

            if not car or days < car[0] or days > car[1]:
                print("Invalid booking period.")
                return

            rate_per_day = 100
            total_amount = days * rate_per_day

            cur.execute("""
                INSERT INTO bookings (user_id, car_id, start_date, end_date, total_amount, status)
                VALUES (%s, %s, %s, %s, %s, 'pending')
            """, (self.user_id, self.car_id, self.start_date, self.end_date, total_amount))

            conn.commit()
            cur.close()
            conn.close()
            print("✅ Booking placed successfully! Awaiting admin approval.")
        except Exception as e:
            print(f"Booking failed: {e}")

    @staticmethod
    def list_pending_bookings():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT b.id, u.name, c.make, c.model, b.start_date, b.end_date, b.total_amount
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status = 'pending'
        """)
        bookings = cur.fetchall()
        cur.close()
        conn.close()
        return bookings

    @staticmethod
    def update_booking_status(booking_id, new_status):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE bookings SET status = %s WHERE id = %s", (new_status, booking_id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def list_approved_bookings_by_user(user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT c.make, c.model, b.start_date, b.end_date, b.total_amount
            FROM bookings b
            JOIN cars c ON b.car_id = c.id
            WHERE b.user_id = %s AND b.status = 'approved'
        """, (user_id,))
        bookings = cur.fetchall()
        cur.close()
        conn.close()
        return bookings
