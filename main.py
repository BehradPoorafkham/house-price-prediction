from house_prediction.API import call_API
from house_prediction.database import create_database, generate_ads, insert_data
from house_prediction.csv_handler import create_csv

def main():
    data = call_API()
    create_database()
    generate_ads(data)
    insert_data(data)
    create_csv()

size = int(input("متراژ خانه: "))
rooms = int(input("تعداد اتاق: "))
year = int(input("سال ساخت: "))
floor = int(input("طبقه: "))
has_parking = input("پارکینگ دارد؟ (yes/no): ")
has_elevator = input("آسانسور دارد؟ (yes/no): ")
parking = 1 if has_parking == "yes" else 0
elevator = 1 if has_elevator == "yes" else 0

house = [[
    size,
    rooms,
    year,
    floor,
    parking,
    elevator
]]