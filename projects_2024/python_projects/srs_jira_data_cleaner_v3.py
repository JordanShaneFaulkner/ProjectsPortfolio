import pandas as pd 
import numpy as np
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog

def open_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer dialog for selecting a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        # Read the selected CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    else:
        print("No file selected.")
        return None

if __name__ == "__main__":
    df = open_csv_file()
    if df is not None:
        # User can interact with the DataFrame here
        print(df.head())  # Display the first few rows of the DataFrame
        # Add your additional DataFrame operations here

#Fill nulls, drop unwanted columns, change dtypes, reformat dtypes,rename columns, create columns needed

df['Destination']=df['Custom field (Destination)']
df['Samples'] = df['Custom field (Number of Samples)']
pd.to_numeric(df['Samples'],downcast='integer')
df.fillna({'Samples':95}, axis = 0,inplace = True)
df.fillna({'Destination':'No Destination'},axis = 0, inplace = True)
df['Resolved'] = pd.to_datetime(df['Resolved'])
df['Created'] = pd.to_datetime(df['Created'])
df['Summary'] = df['Summary'].astype(str)
df['TaT'] = df['Resolved']-df['Created']
df['TaT'] = np.round(df['TaT'] / pd.to_timedelta(1, unit='D'),2)
df['Key'] = df['Issue key']
df['Year Week Created'] = df['Created'].dt.strftime('%Y-w%V')
cols_to_drop = ['Issue key','Issue id','Custom field (Destination)','Custom field (Number of Samples)']
df.drop(cols_to_drop,axis = 1,inplace = True)
df['Destination'] = np.where(df['Destination'] =='WGS' , 'Genomes', df['Destination'])
df['Destination'] = np.where(df['Destination'] =='PCR Free' , 'Genomes', df['Destination'])
df['Destination'] = np.where(df['Destination']=='Standard Germline Exome','BGE & SGE',df['Destination'])
df['Destination'] = np.where(df['Destination']=='Blended Genome Exome','BGE & SGE',df['Destination'])
df.fillna({'TaT':datetime.now() - df['Created']}, axis = 0,inplace = True)
df['Destination'] = np.where(df['Destination'] =='Exome Express' , 'Sonic', df['Destination'])
df['Destination'] = np.where(df['Destination'] =='Blood Biopsy' , 'Sonic', df['Destination'])
df['Destination'] = np.where(df['Destination'] =='Microbial' , 'Other', df['Destination'])
df['Destination'] = np.where(df['Destination'] =='Pacbio' , 'Other', df['Destination'])
df['Destination'] = np.where(df['Destination'] =='Long Reads' , 'Other', df['Destination'])
df = df[df.Status == 'Closed']
df['Week of Date Completed'] = df['Resolved'].dt.to_period('W').apply(lambda r: r.start_time)
df = df.rename(columns={'Resolved':'Resolution Date'})
df['TaT'] = df['TaT'].astype('float32')
df['Samples'] = df['Samples'].astype('float32')
#Check groupings
#print(df[df['Destination']=='Genomes'])
#print(df[df['Destination']=='BGE & SGE'])
#print(df[df['Destination']=='Other'])
#print(df[df['Destination']=='Infinium'])
#print(df[df['Destination']=='Fluidigm'])
#print(df[['Key','TaT']])

def save_csv_file(df):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer dialog for saving a CSV file
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        # Save the DataFrame as a CSV file in the chosen location
        df.to_csv(file_path, index=False)
        print("CSV file saved successfully.")
    else:
        print("No file selected for saving.")

save_csv_file(df)
