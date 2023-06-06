#!/usr/bin/python3
# -*- coding: utf-8 -*-
<<<<<<< Updated upstream
=======

# Libraries
from cleaner import cleaner_data
from time import sleep
import db_config
import datetime
import requests
import mariadb
import json
import sys
from random import random
# Functions
# Spider main function 
def main(url: str):
    # DB connector settings
    # References https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
    # For this part of the code

    #Connect to MariaDB
    try:
        conn = mariadb.connect(
            user = db_config.setting['user'],
            password = db_config.setting['password'],
            host = db_config.setting['host'],
            port = db_config.setting['port'],
            database = db_config.setting['database']
        )

    except mariadb.Error as e:
        sys.exit(1)

    # Get the cursor
    cur = conn.cursor()

    # End part of code

    # Number of attempts to get the data
    attempts = 10

    # Check the response of the get function
    response_get_data = get_data(url, attempts)

    # We finish the spider if we do not have data
    if response_get_data == None:
        return

    # If we have data, we assign it to the data variable
    steam_data = response_get_data

    # We get the current day
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Iterate on the data and
    # make the insertions in the database
    for key, value in steam_data.items():
        appid = value["appid"] #Get the appid
        realvalue = requests.get("https://steamspy.com/api.php?request=appdetails&appid="+str(appid)) #Get response from API
        sql_instruction = cleaner_data(realvalue.text, date) #Create SQL
        sleep(1+random()) #Sleep to not exceed API Time limit

        # References https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
        # For this part of the code

        # Insert the information
        try:
            cur.execute(sql_instruction)

        except mariadb.Error as e:
            continue

        # End part of code
    
    # Commited the insertions on the db
    conn.commit()

    # Finishing the spider
    # Close Connection
    conn.close()
    return

# Function to get data from the API
def get_data(url: str, attempts = 5):
    response = requests.get(url)
    status_code = response.status_code

    for attempt in range(attempts):

        # References https://oxylabs.io/blog/python-requests
        # For this part of the code
        if status_code == 200:
            data = response.json()
            return data

        else:
            sleep(90)
            response = requests.get(url)
            status_code = response.status_code

        # End part of code
    
    return

if __name__ == '__main__':
    # Source = SteamSpy API, Method = GET, Tag = Indie
    # url = 'https://steamspy.com/api.php?request=tag&tag=Indie'
    url = 'https://steamspy.com/api.php?request=tag&tag=Hardware'

    main(url)
>>>>>>> Stashed changes
