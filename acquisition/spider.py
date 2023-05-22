#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
from time import sleep
import requests
import mariadb
import sys

# Functions
def main():
    # Source = SteamSpy API, Method = GET, Tag = Indie
    # url = 'https://steamspy.com/api.php?request=tag&tag=Indie'

    url = 'https://steamspy.com/api.php?request=appdetails&appid=730'

    # Number of attempts to get the data
    attempts = 10

    # Check the response of the get function
    response_get_data = get_dat(url, attempts)

    # We finish the spider if we do not have data
    if response_get_data == None:
        return

    # If we have data, we assign it to the data variable
    data = response_get_data


def get_dat(url: str, attempts = 5):
    response = requests.get(url)
    status_code = response.status_code

    for attempt in range(attempts):
        if status_code == 200:
            data = response.json()
            return data

        else:
            sleep(90)
            response = requests.get(url)
            status_code = response.status_code
    
    return

if __name__ == '__main__':
    main()
