import mysql.connector
from datetime import datetime
from house_prediction.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from house_prediction.decorators import timer, logging_database, logging_ads, logging_data

@timer
@logging_database
def create_database():
    try:
        cnx = mysql.connector.connect(user = DB_USER, password = DB_PASSWORD,
                            host = DB_HOST,
                            database = DB_NAME)
        cursor = cnx.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ads(
            token VARCHAR(20) PRIMARY KEY,
            category VARCHAR(50),
            last_modified_at DATETIME,
            city VARCHAR(50),
            title VARCHAR(255),
            price BIGINT,
            size INT,
            year SMALLINT,
            has_parking BOOLEAN,
            has_elevator BOOLEAN,
            rooms VARCHAR(10),
            floor TINYINT
        )
        """)
        cnx.commit()
    finally:
        cnx.close()

@logging_ads
def generate_ads(data):
    for ad in data["posts"]:

        fields = ad.get("real_estate_fields") or {}
        price = ad.get("price") or {}
        last_modified = datetime.fromisoformat(
            ad.get("last_modified_at").replace("Z",
        "+00:00")
        )
        yield (
            ad.get("token"),
            ad.get("category"),
            last_modified,
            ad.get("city"),
            ad.get("title"),
            int(price.get("value")),
            fields.get("size"),
            fields.get("year"),
            fields.get("has_parking"),
            fields.get("has_elevator"),
            fields.get("rooms"),
            fields.get("floor")
        )

@timer
@logging_data
def insert_data(data):
    try:
        cnx = mysql.connector.connect(user = DB_USER, password = DB_PASSWORD,
                                host = DB_HOST,
                                database = DB_NAME)
        cursor = cnx.cursor()
        cursor.executemany("INSERT INTO ads (token, category, last_modified_at, city, title, price, size, year, has_parking, has_elevator, rooms, floor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", generate_ads(data))
        cnx.commit()
    finally:
        cnx.close()