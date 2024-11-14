# --- Import the required libraries / modules:
from datetime import datetime
from zoneinfo import available_timezones, ZoneInfo


# --- NOTE: Pytz is deprecated from Python 3.9 onwards. Use zoneinfo instead

# --- Show all of the available timezones:
# print(available_timezones())


# --- Set the format for the date, time and timezone to be shown:
datetime_format = '%d/%m/%Y, %H:%M:%S %Z (%z)'


# --- Get the local time (U.K in my case)
local_date_time = datetime.now()


# --- Display the local date, time and timezone:
print(f"Local Time: {local_date_time.strftime(datetime_format)}\n")


# --- Fix the issue of the timezone not being shown:
local_date_time = datetime.now(tz = ZoneInfo("Europe/London")) # not adding tz does not show timezone for uk
local_date_time = datetime.now().astimezone() # This method gets the current system tz instead of hard coding as above


# --- List all of the timezones to use:
locations = [
    {
        "location": "Paris",
        "timezone": "Europe/Paris"
    },
    {
        "location": "Washington D.C",
        "timezone": "US/Eastern"
    },
    {
        "location": "Canberra",
        "timezone": "Australia/Canberra"
    }
]


# --- Display the local date, time and timezone:
print(f"Local Time: {local_date_time.strftime(datetime_format)}\n")


# --- Display the date, time and timezone from the list:
for location in locations:
    print(f"{location['location']} Time: {local_date_time.astimezone(tz = ZoneInfo(location['timezone'])).strftime(datetime_format)}")
