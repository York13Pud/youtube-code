# Python Terminal Output Colour

## Introduction

This contains a couple of examples of how you can define some arguments that can be passed to a Python program when it is run at the command line.

If you would like to see a video of how to deploy this, along with an explanation of the code, here is a link to a video on YouTube that goes over it.

[![YouTube Video](https://img.youtube.com/vi/I-CtWle6-pI/0.jpg)](https://youtube.com/shorts/I-CtWle6-pI)

## Instructions

### Python Requirements

The minimum version of Python you should have installed to run these examples is 3.10. I was using 3.12 at the time of making the examples.

### Download the Repository

Open a terminal and download this repository to a location on your system by running the below command:

``` shell
git clone https://github.com/York13Pud/youtube-code.git
```

Once you have downloaded the repository, you will need to `cd` into the folder `command-line-switches` (you may need to add more to the path depending upon where you saved it):

``` bash
cd youtube-code/python/command-line-switches
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

### Running the Example Files

You are now ready to run any of the examples. There are two files that you can run. Replace *filename* with `example_1/show_name.py`, or `example_2/csv_to_excel.py`:

For macOS:

``` shell
python filename
```

For Windows:

``` powershell
py filename
```

The examples in that file should now appear. You can modify them as you see fit.
