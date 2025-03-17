# --- Import the required libraries / modules:
from decimal import *
from tkinter import messagebox

import freecurrencyapi
import os
import re


def check_value_is_numeric(value: str) -> bool | object:
    """_summary_
    This function takes a string value and attempts to convert it to a Decimal value.

    Args:
        value (str): The value that needs to be converted from a string to a Decimal.

    Returns:
        bool | object: If the value can be converted, it will return it as an object (Decimal). If not, it will return a bool.
    """
    
    # --- Check if the value is a string:
    if not isinstance(value, str):
        return False

    # --- Check if the value has a value:
    if not value:
        return False

    # --- Check for mathematical symbols
    if re.search(r'[+\-*/]', value):
        return False

    # --- Attempt to convert the value to a decimal number:
    try:
        convert_value = float(value)
    
    except ValueError:
        return False
    
    # --- Check if the value is over 0:
    if convert_value <= 0:
        return False
    
    # --- Return the converted value if all checks pass:
    return Decimal(convert_value).quantize(Decimal('.0001'), rounding=ROUND_DOWN)


def get_exchange_rate(from_currency: str, to_currency: str) -> object:
    """_summary_
    This function will get the current exchange rate for 1 of the from_currency and how much it will be in the to_currency.
    
    Args:
        from_currency (str): the currency to convert from.
        to_currency (str): The currency to convert to.

    Raises:
        Exception: Raise an exception if either currency is not valid.

    Returns:
        object: Returns a Decimal object with the value of the converted currency.
    """
    
    client = freecurrencyapi.Client(api_key = os.getenv("API_KEY"))
    
    try:
        result = client.latest(base_currency = from_currency, currencies = [to_currency])
    except:
        messagebox.showerror("Error", "Please check the currencies list as one of the symbols was not recognised. Also, check to see if the API key is entered correctly.")
        raise Exception
        
    return Decimal(result["data"][to_currency]).quantize(Decimal('.0001'), rounding=ROUND_DOWN)


def convert_currency(from_currency: str, to_currency: str, value: object) -> object:
    """_summary_
    This function will convert a value from one currency to another and return the converted value.
    
    Args:
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.
        value (float, optional): The value to convert from.

    Returns:
        object: The converted value as a Decimal.
    """
    
    from_currency_code = from_currency.split(sep = " ")[0]
    to_currency_code = to_currency.split(sep = " ")[0]
    
    exchange_rate = get_exchange_rate(from_currency = from_currency_code, to_currency = to_currency_code)
    
    return Decimal(value * exchange_rate).quantize(Decimal('.0001'), rounding=ROUND_DOWN)
    