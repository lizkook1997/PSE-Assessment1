import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="car_rental_system",
        user="postgres",
        password="Postgredb@sql"
    )



