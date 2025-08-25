# build a cli scraper that fetches SJS roster from NHL JSON API
# parses it into a list of player dicts
# saves CSV + JSON
# prints a short summary in the terminal


# functions
# fetchRoster() - requests the sharks roster JSON and returns a list of player dicts
# saveJSON(data, filename) and saveCSV(data, filename) - persist data
# displaySummary(data) - prints n players saved, shows first 5 fields
# main() - ties it together and provides short menu | 1) Fetch and save roster 2) View saved roster 3) Exit

import requests
from bs4 import BeautifulSoup

def main():
    data = fetchRoster()
    displaySummary(data)
    choice = input("What would you like to do?" \
    " (1) Fetch and save roster (2) View saved roster (3) Exit")
    if choice == "1":
        format = input("Would you like to fetch the roster in (1) JSON or (2) CSV?")
        if format == "1":
            saveJSON(data, "roster.json")
        elif format == "2":
            saveCSV(data, "roster.csv")
    elif choice == "2":
        viewSavedRoster(data)
    elif choice == "3":
        exit()

# fetch and parse the page
def fetchRoster():
    response = requests.get('https://api-web.nhle.com/v1/roster/SJS/current')
    data = response.json()

    roster = data.get("forwards", []) + data.get("defensemen", []) + data.get("goalies", [])
    parsedRoster = [parsePlayers(player) for player in roster]

    return parsedRoster

def parsePlayers(player):
    return {
        "id": player["id"],
        "fullName": f"{player['firstName']['default']} {player['lastName']['default']}",
        "position": player.get("positionCode"), # we use get here in case field is optional or missing
        "jerseyNumber": player.get("jerseyNumber"),
        "height": f"{player.get('heightInInches')} in / {player.get('heightInCentimeters')} cm",
        "weight": f"{player.get('weightInPounds')} lbs / {player.get('weightInKilograms')} kg",
        "birthDate": player.get("birthDate"),
        "nationality": player.get("birthCountry"),
    }

def displaySummary(data):
    print("Welcome to Kevin's San Jose Sharks Scraper")
    print("Go Sharks!")
    print(f"Found {len(data)} players:")
    for player in data[:5]:  # show first 5 players
        print(f" - {player['fullName']} ({player['position']})")

def viewSavedRoster(data):
    print("Viewing saved roster:")
    for player in data:
        print(f" - {player['fullName']} ({player['position']})")

def saveJSON(data, filename):
    pass

def saveCSV(data, filename):
    pass

def menu():
    pass

if __name__ == "__main__":
    main()