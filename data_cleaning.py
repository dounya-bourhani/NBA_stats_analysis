import os
import re
import pandas as pd

# ----- Data exportation - Basketball Reference -----

# Define the path to the data folder
data_folder = 'data'

# List all CSV files in the data folder
csv_files = [f for f in os.listdir(data_folder) if f.startswith('stats')]

# Read and concatenate all CSV files
dataframes = [pd.read_csv(os.path.join(data_folder, file)) for file in csv_files]
stats_dataframe = pd.concat(dataframes, ignore_index=True)

stats_dataframe.rename(columns={'Unnamed: 5': 'LOC', 'Unnamed: 7':'RES'}, inplace=True)

# ------- Adding the defensive rating column -------

# List all CSV files in the data folder that start with 'RD'
rd_csv_files = [f for f in os.listdir(data_folder) if f.startswith('RD')]

# Read and concatenate all CSV files
rd_dataframes = [pd.read_csv(os.path.join(data_folder, file), usecols=['Date', 'DRtg']) for file in rd_csv_files]

# Concatenate the dataframes
rd_stats_dataframe = pd.concat(rd_dataframes, ignore_index=True)

# Convert the Date column to a datetime format
stats_dataframe['Date'] = pd.to_datetime(stats_dataframe['Date'])
rd_stats_dataframe['Date'] = pd.to_datetime(rd_stats_dataframe['Date'])

#  Merge the dataframes on the 'Date' column
stats_dataframe = pd.merge(stats_dataframe, rd_stats_dataframe, on='Date', how='left')

# ------- Data preprocessing - Missing values -------

# Treat the missing values in the LOC column
# Replace "@" with "away"
stats_dataframe['LOC'] = stats_dataframe['LOC'].replace('@', 'away')
# Replace NaN values with "home"
stats_dataframe['LOC'] = stats_dataframe['LOC'].fillna('home')

# Treat the missing values in all the game stats and the defensive rating columns for when he didn't play
# Define the conditions
conditions = ['Inactive', 'Did Not Play', 'Did Not Dress', 'Not With Team']
# Replace NaN values with -1 for rows where GS matches the conditions
stats_dataframe.loc[stats_dataframe['GS'].isin(conditions)] = stats_dataframe.loc[stats_dataframe['GS'].isin(conditions)].infer_objects(copy=False).fillna(-1)

# Treat the missing values in the 3P% column. In this cases, the player did play, but didn't attempt any 3-point shots, free throws or field goals.
stats_dataframe['3P%'] = stats_dataframe['3P%'].fillna(0)
stats_dataframe['FT%'] = stats_dataframe['FT%'].fillna(0)
stats_dataframe['FG%'] = stats_dataframe['FG%'].fillna(0)

# Treat the missing value in the +/- column, which was maybe a mistake or an error.
stats_dataframe['+/-'] = stats_dataframe['+/-'].fillna('4')

# ------- Data preprocessing - Other preprocessing -------

# Age column (from 31-128 to 31)
# Remove everything after the hyphen and convert the column to int
stats_dataframe['Age'] = stats_dataframe['Age'].apply(lambda x: int(x.split('-')[0]))

# RES column (from W (+2) to 2)
# Extract the number in parentheses in the colonne RES
stats_dataframe['RES'] = stats_dataframe['RES'].str.extract(r'\(([-+]?\d+)\)').astype(int)

# Convert the MP column to seconds
def convert_minutes_to_seconds(mp):
    if isinstance(mp, str):
        parts = mp.split(':')
        return int(parts[0]) * 60 + int(parts[1])
    return mp

stats_dataframe['MP'] = stats_dataframe['MP'].apply(convert_minutes_to_seconds)

# Define a function to get the efficiency
def get_efficiency(row):
    return row['PTS'] + row['TRB'] + row['AST'] + row['BLK'] + row['STL'] - (row['FGA'] - row['FG']) - (row['FTA'] - row['FT']) - row['TOV']

stats_dataframe['EFF'] = stats_dataframe.apply(get_efficiency, axis=1)

# Define a function to get the seasons
def get_season(date):
    last_year = str(date.year-1)
    current_year = str(date.year)
    next_year = str(date.year+1)
    if (date >= pd.to_datetime("09-01-" + current_year) and date <= pd.to_datetime("12-31-" + current_year)):
        return current_year + '-' + next_year
    elif (date >= pd.to_datetime("01-01-" + current_year) and date <= pd.to_datetime("08-31-" + current_year)):
        return last_year + '-' + current_year
    
# Apply the function to Date to create new column SEASON
stats_dataframe['SEASON'] = stats_dataframe['Date'].apply(get_season)   

# Defensive rating column
conditions = ['Inactive', 'Did Not Play', 'Did Not Dress', 'Not With Team']
stats_dataframe['DRtg'] = stats_dataframe['DRtg'].replace(conditions, -1)

# Perfect! Now we don't have any missing values anymore. We preprocessed all our data. We can move on to the exploration phase.

# Export the dataframe to a CSV file
stats_dataframe.to_csv('data/Rudy_Gobert_entire_stats.csv')
