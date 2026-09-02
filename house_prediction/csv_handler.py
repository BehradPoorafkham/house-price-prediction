import mysql.connector
import csv
from house_prediction.decorators import logging_csv
from house_prediction.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

@logging_csv
def create_csv():
    cnx = mysql.connector.connect(user = DB_USER, password = DB_PASSWORD,
                                  host = DB_HOST,
                                  database = DB_NAME)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM ads")
    rows = cursor.fetchall()
    header = (
        "token", 
        "category", 
        "last_modified_at",
        "city", 
        "title", 
        "price", 
        "size", 
        "year", 
        "has_parking", 
        "has_elevator", 
        "rooms", 
        "floor"
    )
    with open(
        r"C:\Users\nima rayaneh novin\Desktop\python_work\House_price_prediction_system\data\ads.csv", 
        mode="w", 
        newline="", 
        encoding="utf-8-sig"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    cnx.close()