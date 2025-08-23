# build a cli scraper that fetches SJS roster from NHL JSON API
# parses it into a list of player dicts
# saves CSV + JSON
# prints a short summary in the terminal


# fields to extract
# fullName
# position
# jerseyNumber
# height/weight
# birthDate
# nationality
# player id or person.id

# functions
# fetchRoster() - requests the sharks roster JSON and returns a list of player dicts
# saveJSON(data, filename) and saveCSV(data, filename) - persist data
# displaySummary(data) - prints n players saved, shows first 5 fields
# main() - ties it together and provides short menu | 1) Fetch and save roster 2) View saved roster 3) Exit

import requests
from bs4 import BeautifulSoup


# fetch and parse the page
def fetchRoster():
    response = requests.get('https://api-web.nhle.com/v1/roster/SJS/current')

    print(response.status_code, response.headers.get("content-type"))
    # 200 application/json

    print(response.json().keys())            # see top-level keys
    # dict_keys(['forwards', 'defensemen', 'goalies'])

    # store Fs, Ds, and Gs inside their own arrays.
    roster = response.json().get("forwards", []) + response.json().get("defensemen", []) + response.json().get("goalies", [])

    print(len(roster), roster[0])        # inspect one player entry
    # 49 {'id': 8481585, 'headshot': 'https://assets.nhle.com/mugs/nhl/20252026/SJS/8481585.png', 'firstName': {'default': 'Egor'}, 'lastName': {'default': 'Afanasyev'}, 'sweaterNumber': 11, 'positionCode': 'L', 'shootsCatches': 'L', 'heightInInches': 76, 'weightInPounds': 211, 
    # 'heightInCentimeters': 193, 'weightInKilograms': 96, 'birthDate': '2001-01-23', 'birthCity': {'default': 'Tver'}, 'birthCountry': 'RUS'} 

    return roster