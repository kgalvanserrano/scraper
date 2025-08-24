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

def main():
    fetchRoster()


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

if __name__ == "__main__":
    main()