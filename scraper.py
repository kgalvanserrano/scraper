import requests
from bs4 import BeautifulSoup


# fetch and parse the page
response = requests.get('https://api-web.nhle.com/v1/roster/SJS/current')
soup = BeautifulSoup(response.text, 'html.parser') # converts html into searchable object, html.parser is the built-in parser

print(response.status_code, response.headers.get("content-type"))
# 200 application/json
print(response.json().keys())            # see top-level keys
# dict_keys(['forwards', 'defensemen', 'goalies'])
roster = response.json().get("forwards", []) + response.json().get("defensemen", []) + response.json().get("goalies", [])

print(len(roster), roster[0])        # inspect one player entry

# 49 {'id': 8481585, 'headshot': 'https://assets.nhle.com/mugs/nhl/20252026/SJS/8481585.png', 'firstName': {'default': 'Egor'}, 'lastName': {'default': 'Afanasyev'}, 'sweaterNumber': 11, 'positionCode': 'L', 'shootsCatches': 'L', 'heightInInches': 76, 'weightInPounds': 211, 
# 'heightInCentimeters': 193, 'weightInKilograms': 96, 'birthDate': '2001-01-23', 'birthCity': {'default': 'Tver'}, 'birthCountry': 'RUS'} 