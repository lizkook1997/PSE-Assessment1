from db.db_config import get_connection

class Car:
    def __init__(self, make, model, year, mileage, min_days, max_days):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.min_days = min_days
        self.max_days = max_days

    def add(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO cars (make, model, year, mileage, min_days, max_days, available)
                VALUES (%s, %s, %s, %s, %s, %s, TRUE)
            """, (self.make, self.model, self.year, self.mileage, self.min_days, self.max_days))
            conn.commit()
            cur.close()
            conn.close()
            print("Car added successfully!")
        except Exception as e:
            print(f"Failed to add car: {e}")

    @staticmethod
    def list_available():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM cars WHERE available = TRUE")
            cars = cur.fetchall()
            cur.close()
            conn.close()
            return cars
        except Exception as e:
            print(f"Failed to fetch cars: {e}")
            return []
