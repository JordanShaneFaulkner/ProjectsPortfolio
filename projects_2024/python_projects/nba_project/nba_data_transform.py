import os
import pandas as pd

# Define the path to your Documents folder (adjust the path based on your system)
documents_folder = os.path.expanduser("~/Documents")

# List all files in the folder
files_in_directory = os.listdir(documents_folder)

# Filter out only CSV files that match a particular naming convention (e.g., "data_*.csv")
csv_files = [file for file in files_in_directory if file.endswith(".csv") and (file.startswith("scores") or file.startswith("stats") or file.startswith('projections'))]

dataframes = {}

for csv_file in csv_files:
    file_path = os.path.join(documents_folder, csv_file)
    df_name = os.path.splitext(csv_file)[0] 
    df = pd.read_csv(file_path)
    dataframes[df_name] = df

free_agent_data: pd.DataFrame = dataframes.get('scores_json_FreeAgents', pd.DataFrame())
active_player_data: pd.DataFrame = dataframes.get('scores_json_Players', pd.DataFrame())
stadium_data: pd.DataFrame = dataframes.get('scores_json_Stadiums', pd.DataFrame())
team_data: pd.DataFrame = dataframes.get('scores_json_teams', pd.DataFrame())
team_season_data_2024: pd.DataFrame = dataframes.get('scores_json_TeamSeasonStats_2024', pd.DataFrame())
injured_player_data_2024: pd.DataFrame = dataframes.get('projections_json_InjuredPlayers', pd.DataFrame())
player_season_data_2024: pd.DataFrame = dataframes.get('stats_json_PlayerSeasonStats_2024', pd.DataFrame())


active_player_cols_to_keep = ['PlayerID' ,'Status', 'TeamID', 'Team', 'Jersey',
 'PositionCategory', 'Position', 'FirstName' ,'LastName', 'Height' ,'Weight',
 'College' ,'Salary', 'Experience', 'SportRadarPlayerID','NbaDotComPlayerID']

free_agent_cols_to_keep=['PlayerID', 'Status','PositionCategory', 'Position', 'FirstName', 'LastName', 'Height',
       'Weight', 'BirthDate', 'BirthCity', 'BirthState', 'BirthCountry',
       'HighSchool', 'College', 'Salary','Experience','NbaDotComPlayerID']

stadium_data_cols_to_keep = ['StadiumID', 'Active', 'Name', 'Address', 'City', 'State', 'Zip', 'Country', 'Capacity', 'GeoLat', 'GeoLong']

team_data_cols_to_keep = ['TeamID', 'Key', 'Active', 'City', 'Name', 'LeagueID', 'StadiumID',
'Conference', 'Division', 'PrimaryColor', 'SecondaryColor','TertiaryColor', 'QuaternaryColor','NbaDotComTeamID', 'HeadCoach']

team_season_data_2024_cols_to_keep = ['StatID', 'TeamID', 'SeasonType', 'Season', 'Name', 'Team', 'Wins',
       'Losses', 'OpponentPosition', 'Possessions', 'Updated',
       'Games', 'FantasyPoints', 'Minutes', 'Seconds', 'FieldGoalsMade',
       'FieldGoalsAttempted', 'FieldGoalsPercentage',
       'EffectiveFieldGoalsPercentage', 'TwoPointersMade',
       'TwoPointersAttempted', 'TwoPointersPercentage', 'ThreePointersMade',
       'ThreePointersAttempted', 'ThreePointersPercentage', 'FreeThrowsMade',
       'FreeThrowsAttempted', 'FreeThrowsPercentage', 'OffensiveRebounds',
       'DefensiveRebounds', 'Rebounds', 'OffensiveReboundsPercentage',
       'DefensiveReboundsPercentage', 'TotalReboundsPercentage', 'Assists',
       'Steals', 'BlockedShots', 'Turnovers', 'PersonalFouls', 'Points',
       'TrueShootingAttempts', 'TrueShootingPercentage',
       'PlayerEfficiencyRating', 'AssistsPercentage', 'StealsPercentage',
       'BlocksPercentage', 'TurnOversPercentage', 'UsageRatePercentage',
       'PlusMinus', 'DoubleDoubles', 'TripleDoubles',
       'FantasyPointsFantasyDraft', 'IsClosed', 'LineupConfirmed',
       'LineupStatus', 'OpponentStat']

injured_player_data_cols_to_keep = ['PlayerID', 'Status', 'TeamID', 'Team', 'Jersey',
       'PositionCategory', 'Position', 'FirstName', 'LastName', 'Height',
       'Weight', 'BirthDate', 'BirthCity', 'BirthState', 'BirthCountry',
       'HighSchool', 'College', 'Salary', 'Experience',
       'SportRadarPlayerID', 'StatsPlayerID', 'InjuryStatus', 'InjuryBodyPart', 'InjuryStartDate',
       'InjuryNotes','DepthChartPosition','DepthChartOrder', 'NbaDotComPlayerID']

player_season_data_2024_cols_to_keep = ['StatID', 'TeamID', 'PlayerID', 'SeasonType', 'Season', 'Name', 'Team',
       'Position', 'Started', 'GlobalTeamID', 'Updated', 'Games',
       'FantasyPoints', 'Minutes', 'Seconds', 'FieldGoalsMade',
       'FieldGoalsAttempted', 'FieldGoalsPercentage',
       'EffectiveFieldGoalsPercentage', 'TwoPointersMade',
       'TwoPointersAttempted', 'TwoPointersPercentage', 'ThreePointersMade',
       'ThreePointersAttempted', 'ThreePointersPercentage', 'FreeThrowsMade',
       'FreeThrowsAttempted', 'FreeThrowsPercentage', 'OffensiveRebounds',
       'DefensiveRebounds', 'Rebounds', 'OffensiveReboundsPercentage',
       'DefensiveReboundsPercentage', 'TotalReboundsPercentage', 'Assists',
       'Steals', 'BlockedShots', 'Turnovers', 'PersonalFouls', 'Points',
       'TrueShootingAttempts', 'TrueShootingPercentage',
       'PlayerEfficiencyRating', 'AssistsPercentage', 'StealsPercentage',
       'BlocksPercentage', 'TurnOversPercentage', 'UsageRatePercentage',
       'FantasyPointsFanDuel', 'FantasyPointsDraftKings', 'FantasyPointsYahoo',
       'PlusMinus', 'DoubleDoubles', 'TripleDoubles',
       'FantasyPointsFantasyDraft', 'IsClosed', 'LineupConfirmed',
       'LineupStatus']

active_player_data = active_player_data[active_player_cols_to_keep]
free_agent_data = free_agent_data[free_agent_cols_to_keep]
injured_player_data_2024 = injured_player_data_2024[injured_player_data_cols_to_keep]
stadium_data = stadium_data[stadium_data_cols_to_keep]
team_season_data_2024 = team_season_data_2024[team_season_data_2024_cols_to_keep]
team_data = team_data[team_data_cols_to_keep]
player_season_data_2024 = player_season_data_2024[player_season_data_2024_cols_to_keep]
active_player_data.loc[active_player_data['PlayerID'] == 20003210, 'Experience'] = 1

#Verification
print(active_player_data.isna().any())
print(free_agent_data.isna().any())
print(injured_player_data_2024.isna().any())
print(active_player_data.duplicated().sum())
print(injured_player_data_2024.duplicated().sum())
print(free_agent_data.duplicated().sum())
print(stadium_data.duplicated().sum())
print(team_data.duplicated().sum())
print(team_season_data_2024.duplicated().sum())