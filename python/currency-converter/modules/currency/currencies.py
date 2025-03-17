# --- Import the required libraries / modules:
import freecurrencyapi # https://freecurrencyapi.com/docs/latest
import os

def currencies_description(data: dict) -> list:
    """_summary_
    This function takes a dictionary of currencies, formats them and puts them into a list.

    Args:
        data (dict): A dictionary containing the data from the API.

    Returns:
        list: A list of strings with each currency formatted as 'code - name(symbol)'.
    """
    currency_list = list((f'{x["code"]} - {x["name"]} ({x["symbol"]})') for x in data["data"].values())
    
    return currency_list


def get_currencies() -> list:
    """_summary_
    This function gets the current available currencies from freecurrencyapi.
    
    Raises:
        Exception: Raise an error if the currencies cannot be retrieved.

    Returns:
        list: A list of dictionaries for all of the available currencies.
    """
    
    client = freecurrencyapi.Client(api_key = os.getenv("API_KEY"))
    
    currencies = client.currencies()

    if type(currencies) is not dict:
        raise Exception("There was an error getting the list of currencies")
    
    currencies_list = currencies_description(data = currencies)
    
    return currencies_list