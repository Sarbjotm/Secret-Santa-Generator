# Secret Santa

Secret Santa assigns gifters to giftees, and notifys them by email whose Secret Santa they will be. 

## Installation

After cloning the repo, create a config.py file that has your gmail email address and password in the following format: 

```python
EMAIL_ADDRESS = ""
PASSWORD = ""

```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SMTPLIB

```bash
pip install smtplib
```

## Set Up Gmail

Log into your gmail account from a browser and navigate to [My Account](https://myaccount.google.com/security) and scroll down until you see "Allow less secure apps" and turn this setting on. 

*NOTE THIS DOES MAKE YOUR GMAIL LESS SECURE SO EITHER USE A NON PRIMARY EMAIL OR REMEMBER TO TURN OFF THE SETTIG WHEN YOU'RE DONE*

## Running
After installing [pip](https://pip.pypa.io/en/stable/) and setting up your gmail account place your CSV file titled "namesandemails.csv" into the directory. Ensure the file format for namesandemails is 
```bash
NAME1,EMAIL1
NAME2,EMAIL2
```
Now in terminal enter 
```bash
python3 santa.py
```
or 
```bash
python santa.py
```
depending on your operating system and if you have more then one python version installed.
