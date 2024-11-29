#Author: Jordan Faulkner - Broad Institute of MIT and Harvard - GP - SRS
#In this project I will create data visualizations for Turnaround time for SRS Data

#Import packages needed 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
from matplotlib.patches import Rectangle
from dash import Dash,html,dcc,callback,Output,Input,dash_table
import plotly.express as px 
from datetime import date 
from datetime import datetime
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc

#Create CSV file path and Full Data DF in Pandas, set mode to copy on write
pd.set_option("mode.copy_on_write", True)
srs_full = pd.read_csv(r'C:\Users\jfaulkne\Downloads\SRSData-3-26-2024.csv',encoding = 'UTF-8',delimiter = ',')

#Change the Data Types from Objects to the correct dtypes and fill null values

#print(srs_full.columns)
#print(srs_full.dtypes)
#print(srs_full.isna().any())

srs_full['Created'] = pd.to_datetime(srs_full.Created)
srs_full['Resolved'] = pd.to_datetime(srs_full.Resolved)
srs_full['Samples'] = pd.to_numeric(srs_full['Custom field (Number of Samples)'],downcast = 'integer')
srs_full['Key'] = srs_full['Issue key'].astype("string")
srs_full['Status'] = srs_full['Status'].astype("string")
srs_full['Summary']=srs_full['Summary'].astype("string")
srs_full['Destination'] = srs_full['Custom field (Destination)'].astype("string")
srs_full.fillna({'Samples':95.0},inplace = True)
srs_full.fillna({'Custom field (Number of Samples)':95.0},inplace = True)
srs_full.fillna({'Custom field (Destination)':'No Destination'},inplace = True)
srs_full.fillna({'Destination':'No Destination'},inplace = True)

#Now check if any are null after conversion and fills 
#print(srs_full.columns)
#print(srs_full.dtypes)
#print(srs_full.isna().any())

#Make a new pandas DF selecting only the columns needed and in order from the original full data 
srs_df = srs_full[['Key','Destination','Samples','Summary','Status','Created','Resolved']]

#Check if new DF has null values and where and check dtypes
#print(srs_df.isna().any())
#print(srs_df.dtypes)

#Create Turnaround Time column and Year Week column
srs_df['TAT'] = srs_df['Resolved'] - srs_df['Created']
srs_df['TAT'] = srs_df['TAT'].dt.days
srs_df['YW'] = srs_df['Created'].dt.strftime('%Y-w%V')
#print(srs_df.columns)
#print(srs_df.dtypes)
#print(srs_df.isnull().any())

#Calculate the Average turnaround time of the given data 
#print(srs_df['TAT'].sum())
#print(len(srs_df['TAT']))
earliest_srs_date = srs_df['Created'].min()
latest_srs_date = srs_df['Created'].max()
#print(earliest_srs_date)
#print(latest_srs_date)
mean_tat = np.round(srs_df['TAT'].sum()/len(srs_df['TAT']),1)
#print(f'The average Turnaround Time is currently {mean_tat} Days for SRS Tickets created from {earliest_srs_date} to {latest_srs_date}')

#Find all the sample destruction and Tube Return tickets and drop from main DF
sample_destructions_df =srs_df[srs_df['Summary'].str.lower().str.contains('destruction')]
#print(sample_destructions_df.head())
tube_returns_df = srs_df[(srs_df['Destination'] == 'Tube Return & Externals') & (srs_df['Summary'].str.lower().str.contains('destruction') == False)]
#print(tube_returns_df.head())
sample_destructions_drop = srs_df[srs_df['Summary'].str.lower().str.contains('destruction')].index
tube_returns_drop = srs_df[(srs_df['Destination'] == 'Tube Return & Externals') & (srs_df['Summary'].str.lower().str.contains('destruction') == False)].index
srs_df.drop(sample_destructions_drop,inplace = True)
srs_df.drop(tube_returns_drop,inplace = True)

#Create Extractions DF and then drop it from the main DF
xtr_df = srs_df[srs_df['Destination']=='Extraction']
xtr_drop = srs_df[srs_df['Destination']=='Extraction'].index
srs_df.drop(xtr_drop,inplace = True)
#print(xtr_df.head(30))
#print(srs_df.head(50))

#drop weeks that have little data (unreliable TAT) 
drop_week1 = srs_df[srs_df['YW']=='2023-w51'].index
drop_week2 = srs_df[srs_df['YW'] == '2024-w02'].index
drop_week3 = srs_df[srs_df['YW'] == '2024-w03'].index
drop_week4 = srs_df[srs_df['YW'] == '2024-w04'].index
drop_week5 = srs_df[srs_df['YW'] == '2024-w13'].index
srs_df.drop(drop_week1,inplace = True)
srs_df.drop(drop_week2,inplace = True)
srs_df.drop(drop_week3,inplace = True)
srs_df.drop(drop_week4,inplace = True)
srs_df.drop(drop_week5,inplace = True)

#Create a bar chart showing the number of samples consolidated each year week, colored by Destination
fig1 = px.bar(srs_df,x = 'YW',y='Samples',
    color = 'Destination',
    hover_data = ['Key','Created','Resolved','Samples','TAT'],
    title = 'Number of Samples consolidated per year week',template = 'ggplot2')
fig1.show()
