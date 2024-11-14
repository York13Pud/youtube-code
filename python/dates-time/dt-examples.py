# --- Import the required libraries / modules:
from datetime import date, datetime, time, timedelta


# --- Get the current date and time:
print(f"Date & Time: {datetime.now()}\n")


# --- Get just the current date:
print(f"Date: {datetime.now().date()}\n")


# --- Get just the current time:
print(f"Time: {datetime.now().time()}\n")


# --- Specify a date that will be shown in the yyyy-mm-dd format:
print(f"Date (yyyy-mm-dd): {date(year=2024, month=11, day=12)}\n")


# --- Specify a time that will be shown in the format hh:mm:ss:
print(f"Time (hh:mm:ss): {time(hour = 12, minute = 30, second = 59)}\n")


# --- Show the difference between two dates:
date_one = date(year=2024, month=11, day=7)
date_two = date(year=2023, month=11, day=6)

print(f"The first time difference is: {date_one - date_two}\n")


# --- Show the difference between two times:
time_one = timedelta(hours = 15, minutes = 52)
time_two = timedelta(hours = 13, minutes = 58)

print(f"The second time difference is: {time_one - time_two}\n")


# --- Show the difference between two dates and times:
date_time_one = datetime(year = 2023, month = 4, day = 22, 
                         hour = 11, minute = 52, second = 25)

date_time_two = datetime(year = 2022, month = 3, day = 22, 
                         hour = 13, minute = 58, second = 57)

print(f"The third time difference is: {date_time_one - date_time_two}\n")


# --- Convert to European and U.S.A based date formats (dd-mm-yyyy / mm-dd-yyyy):
current_date = datetime.now()

print(f"Default Date Format: {current_date.date()}")
print(f"Current Time: {current_date.strftime('%H:%M:%S')}\n")
print(f"U.S.A Date Format: {current_date.strftime('%m/%d/%Y')}")
print(f"U.K Date Format: {current_date.strftime('%d/%m/%Y')}\n")
