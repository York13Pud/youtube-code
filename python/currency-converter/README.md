# Python Currency Converter GUI App

## Introduction

This project is a currency converter GUI application that uses customTKinter, along with some aspects of TKinter to create a cross-platform currency converter GUI application.

If you would like to see a video of how to deploy this, along with an explanation of the code, here is a link to a video on YouTube that goes over it.

[![YouTube Video](https://img.youtube.com/vi/9iNjPkpeELQ/0.jpg)](https://www.youtube.com/watch?v=9iNjPkpeELQ)

## Instructions

### Python Requirements

To deploy the application, you will need to have Python installed on your system. The version I developed the app with was 3.12. You will also need to ensure that TKinter is installed as well.

For macOS, if you installed Python using homebrew, you will need to install TKinter using the following command (Change `3.12` to match the version of Python you are running.):

``` bash
brew install python-tk@3.12
```

If you installed Python using the installer from [python.org](https://www.python.org/), TKinter is usually installed as part of that. This applies to both macOS and Windows.

### Download the Repository

Open a terminal and download this repository to a location on your system by running the below command:

``` shell
git clone https://github.com/York13Pud/youtube-code.git
```

Once you have downloaded the repository, you will need to `cd` into the folder called currency-converter (you may need to add more to the path depending upon where you saved it):

``` bash
cd youtube-code/python/currency-converter
```

### Setting Up a Virtual Environment

Create a new virtual environment by running:

For macOS:

``` bash
python3 -m venv venv
```

For Windows:

``` powershell
py -m venv env/my_env
```

Next, activate the virtual environment:

For macOS

``` shell
source ./venv/bin/activate
```

For Windows (ensure that you are able to execute PowerShell scripts before running this):

``` powershell
.\my_env\Scripts\activate
```

### Install Required Packages

To install the required packages, run:

For macOS and Windows:

``` shell
pip install -r requirements.txt
```

### API key

This application will require an API key from [freecurrencyapi.com](https://freecurrencyapi.com/). You can sign up for an account and obtain an API key from there (not sponsored).

The API key will need to be saved in a `.env` file that is stored in `modules/env`. You will need to create this file as it is not included in the repository. The environment variable name will need to be called `API_KEY`. For example:

`modules/env/.env`

``` bash
API_KEY="change-me"
```

### Run the App

You are now ready to run the application. To run it, simply run:

For macOS:

``` shell
python main.py
```

For Windows:

``` powershell
py main.py
```

The application should now appear.

## Using the App

The application is very simple to use. You input an amount you want to convert and then specify the currency to convert from and then to.

You then click on Convert and the converted value will appear above the button.

Here is a short video demo of the app:

[![Demo](https://img.youtube.com/vi/GvcJWR80ijk/0.jpg)](https://www.youtube.com/watch?v=GvcJWR80ijk)
