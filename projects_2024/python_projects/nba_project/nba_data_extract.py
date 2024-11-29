import pandas as pd 
import requests 
import os 

#CONSTANTS
API_KEY="c69dfab489284f9f8a08efaf40339074" #API Key
BASE = "https://api.sportsdata.io/v3/nba/" #Base URL for NBA API Get Request 

def get_data(endpoint):
    try:
        request = requests.get(f"{BASE}{endpoint}?key={API_KEY}")
        if request.status_code == 200:
            print(f"Request successful: code {request.status_code}.")
            return request.json()
        else:
            print(f"Request Unsuccessful.Error {request.status_code} Reason: {request.reason}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while fetching data: {e}")

def get_multiple_endpoints_and_save(endpoints):
    os.makedirs("c:\\Users\\jfaulkne\\Documents", exist_ok=True)
    for endpoint in endpoints:
        data = get_data(endpoint)
        if data:
            df = pd.DataFrame(data)
            file_name = f"c:\\Users\\jfaulkne\\Documents/{endpoint.replace('/', '_')}.csv"
            df.to_csv(file_name, index=False)
            print(f"Data from {endpoint} saved to {file_name}")
        else:
            print(f"No data returned for {endpoint}")

nba_endpoints = ["scores/json/Players","scores/json/FreeAgents","projections/json/InjuredPlayers","stats/json/PlayerSeasonStats/2024","scores/json/teams","scores/json/Stadiums","scores/json/TeamSeasonStats/2024"]

get_multiple_endpoints_and_save(nba_endpoints)
