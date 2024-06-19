#Jordan Faulkner 
#Started on 6-14-2024
#In this project I will automate the SRS Key Performance Inficator process. 
#The output of this code will be a pivot table displaying the Average Turnaround Time for samples in a percentage completed in UNDER 2 days PER year week. 

import pandas as pd 
import numpy as np 
from datetime import * 
import tkinter as tk
from tkinter import filedialog

def open_csv_file():
    root = tk.Tk()
    root.withdraw()  

    
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    else:
        print("No file selected.")
        return None

if __name__ == "__main__":
    df = open_csv_file()
    if df is not None:
        
        print(df.head())  

df.rename(columns={'Issue key':'Key', 'Custom field (Destination)':'Destination','Custom field (Number of Samples)':'Samples','Issue id':'ID'},inplace= True) 
df.drop(columns={'ID','Summary','Status','Resolution','Destination','Samples'},inplace=True)
df.dropna(subset='Created',inplace=True)
df.dropna(subset = 'Resolved',inplace = True)
df['Created'] = pd.to_datetime(df['Created'], errors='coerce')
df['Resolved'] = pd.to_datetime(df['Resolved'], errors='coerce')
df['YW'] = df['Created'].dt.strftime('%Y-%W')
df['TaT'] = (df['Resolved']-df['Created']).dt.days
print(df.head())
under_2_days = df['TaT'] < 2
percentage_under_2_days = (under_2_days.sum() / len(df)) * 100
print(f"Percentage of tickets consolidated in under 2 days: {percentage_under_2_days:.2f}%")
pivot_table = pd.pivot_table(df, values='Key',index='YW', aggfunc='count', 
                             columns=pd.cut(df['TaT'], bins=[-1, 2, float('inf')]), 
                             fill_value=0)


pivot_table.columns = ['Under 2 Days', 'Over 2 Days']
pivot_table['Percentage Under 2 Days'] =np.round((pivot_table['Under 2 Days'] / pivot_table.sum(axis=1)) * 100,3)

def save_csv_file(table):
    root = tk.Tk()
    root.withdraw()  

    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        
        pivot_table.to_csv(file_path, index=True)
        print("CSV file saved successfully.")
    else:
        print("No file selected for saving.")

save_csv_file(pivot_table)

