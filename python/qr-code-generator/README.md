# Python QR Code Generator Using CustomTKinter

## Introduction

This project is a simple QR Code GUI application that uses customTKinter, along with some aspects of TKinter to create a cross-platform desktop application.

If you would like to see a video of how to deploy this, along with an explanation of the code, here is a link to a video on YouTube that goes over it.

[![YouTube Video](https://img.youtube.com/vi/GvcJWR80ijk/0.jpg)](https://www.youtube.com/watch?v=GvcJWR80ijk)

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

Once you have downloaded the repository, you will need to `cd` into the folder called qr-code-generator (you may need to add more to the path depending upon where you saved it):

``` bash
cd youtube-code/python/qr-code-generator
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

Using the application is very simple. There is a text box on the top-left that you can use to enter a URL or any text that you want to put into the QR code. There are then three sliders, each determine specific size metrics of the QR code.

After that, there are two colour pickers, one for the foreground and another for the background colour of the QR code.

Finally, there are two buttons at the bottom. The *Preview* button will generate the QR code based on what has been specified in the settings above and then show it where the preview image is.

The *Save* button will then prompt you for a filename and location to save the QR code image to.
