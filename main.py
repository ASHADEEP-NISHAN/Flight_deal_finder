#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

notification=NotificationManager()
data_manager = DataManager()
flight_search=FlightSearch()

sheet_data = data_manager.get_destination_data()
if sheet_data[0]["iataCode"]=="":
    for row in sheet_data:
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    data_manager.destinaton_data=sheet_data
    data_manager.update_destination_codes()

tomorrow=datetime.now()+timedelta(days=1)
six_month=datetime.now()+timedelta(days=(6*30))
for destination in sheet_data:
    flight=flight_search.check_Flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month
    )
    if flight==None:
        continue
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customers_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message=f"low price alert ! only ${flight.price}to fly from {flight.origin_city}-"
        f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}"
        f", from {flight.out_date} to {flight.return_date}."
        if flight.stop_over>0:
            message+= f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        # notification.send_sms(message=message)
        notification.send_emails(emails,message=message)
