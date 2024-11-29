#Jordan Faulkner - started on: 5-22-2024
#In this project I will take data queried from tableau and output the days SRS throughput in different destination types in tickets done, samples done, and then also read out the remaining tickets and samples of each destination type. 
#The groupings for destinations are as follows: Production, Tube Returns and Externals, Destructions, XTR 
#-------------------------------------------------------------------------------------------------------------------------#
import pandas as pd 
import numpy as np
from datetime import datetime
import os
def find_csv_files(directory, prefix):
    """Find CSV files in the given directory that start with the specified prefix."""
    return [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.csv')]

def load_csv_to_df(directory, filename):
    """Load a CSV file into a pandas DataFrame."""
    file_path = os.path.join(directory, filename)
    return pd.read_csv(file_path)

def main(directory):
    
    finished_files = find_csv_files(directory, 'tickets_finished')
    remaining_files = find_csv_files(directory, 'tickets_still')

    
    if finished_files:
        tickets_finished_df = load_csv_to_df(directory, finished_files[0])
    else:
        tickets_finished_df = None
        print("No 'tickets_finished' files found.")

    if remaining_files:
        tickets_remaining_df = load_csv_to_df(directory, remaining_files[0])
    else:
        tickets_remaining_df = None
        print("No 'tickets_remaining' files found.")

    return tickets_finished_df, tickets_remaining_df

if __name__ == "__main__":
    directory = r"C:\Users\jfaulkne\Desktop\srs_jira_data"  
    tickets_finished_df, tickets_remaining_df = main(directory)
#Rename the columns of both Dataframes 
tickets_finished_df.rename(columns={'Issue key':'Key','Custom field (Destination)':'Destination','Custom field (Number of Samples)':'Samples'}, inplace= True)
tickets_remaining_df.rename(columns={'Issue key':'Key','Custom field (Destination)':'Destination','Custom field (Number of Samples)':'Samples'}, inplace= True)
#clean both dataframes 
#print(tickets_finished_df.dtypes)
pd.to_numeric(tickets_finished_df['Samples'],downcast='integer')
tickets_finished_df['Summary'] = tickets_finished_df.Summary.astype('str')
tickets_finished_df['Status'] = tickets_finished_df.Status.astype('str')
tickets_finished_df.fillna({'Samples':95}, axis = 0,inplace = True)
tickets_finished_df.fillna({'Destination':'No Destination'},axis = 0, inplace = True)
tickets_finished_df['Created'] = pd.to_datetime(tickets_finished_df['Created'])
tickets_finished_df['Year Week Created'] = tickets_finished_df['Created'].dt.strftime('%Y-w%V')
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='WGS' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='PCR Free' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination']=='Standard Germline Exome','Production',tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination']=='Blended Genome Exome','Production',tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Exome Express' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Blood Biopsy' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Microbial' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Pacbio' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Long Reads' , 'Production', tickets_finished_df['Destination'])
destruct = 'Destruction'
column_name = 'Summary'
xtr = 'XTR'
extractions = 'extractions'
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Summary'].str.contains(destruct,case = False,na=False) , 'Destruction', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Summary'].str.contains(xtr,case = False,na=False) , 'XTR', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Summary'].str.contains(extractions,case = False,na=False) , 'XTR', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Fluidigm' , 'Production', tickets_finished_df['Destination'])
tickets_finished_df['Destination'] = np.where(tickets_finished_df['Destination'] =='Pico' , 'Production', tickets_finished_df['Destination'])
pd.to_numeric(tickets_remaining_df['Samples'],downcast='integer')
tickets_remaining_df['Summary'] = tickets_remaining_df.Summary.astype('str')
tickets_remaining_df['Status'] = tickets_remaining_df.Status.astype('str')
tickets_remaining_df.fillna({'Samples':95}, axis = 0,inplace = True)
tickets_remaining_df.fillna({'Destination':'No Destination'},axis = 0, inplace = True)
tickets_remaining_df['Created'] = pd.to_datetime(tickets_remaining_df['Created'])
tickets_remaining_df['Year Week Created'] = tickets_remaining_df['Created'].dt.strftime('%Y-w%V')
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='WGS' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='PCR Free' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination']=='Standard Germline Exome','Production',tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination']=='Blended Genome Exome','Production',tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Exome Express' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Blood Biopsy' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Microbial' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Pacbio' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Long Reads' , 'Production', tickets_remaining_df['Destination'])
destruct = 'Destruction'
column_name = 'Summary'
xtr = 'XTR'
extractions = 'extractions'
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Summary'].str.contains(destruct,case = False,na=False) , 'Destruction', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Summary'].str.contains(xtr,case = False,na=False) , 'XTR', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Summary'].str.contains(extractions,case = False,na=False) , 'XTR', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Fluidigm' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df['Destination'] = np.where(tickets_remaining_df['Destination'] =='Pico' , 'Production', tickets_remaining_df['Destination'])
tickets_remaining_df.drop(columns='Resolution',inplace=True)
print(tickets_remaining_df.isnull().sum())#Check if there are any null values left 
print(tickets_finished_df.isnull().sum()) #Check if there are any null values left 

#print to the console the total number of tickets consolidated and the total samples consolidated 
total_tickets_finished = len(tickets_finished_df)
print(f'total number of tickets consolidated: {total_tickets_finished}')
total_samples_finished = 0
for n in tickets_finished_df['Samples']:
    total_samples_finished += n
print(f'total Samples consolidated today: {total_samples_finished}')
total_tickets_in_progress = len(tickets_remaining_df)
print(f'total tickets in progress: {total_tickets_in_progress}')
total_samples_in_progress = 0
for x in tickets_remaining_df['Samples']:
    total_samples_in_progress+=x 
print(f'Total Samples In Progress {total_samples_in_progress}')

#Print to the console the total number of Production Tickets and Production samples 
print('Here is the total samples completed today per Destination')
print('')
print(tickets_finished_df.pivot_table(index='Destination',values='Samples',aggfunc='sum',margins=True,margins_name='Total Samples Completed Today:'))
print('')
print(f'total XTR tickets consolidated is: {len(tickets_finished_df[tickets_finished_df['Destination']=='XTR'])}')
print(f'total Production tickets consolidated is: {len(tickets_finished_df[tickets_finished_df['Destination']=='Production'])}')
print(f'total Destruction tickets consolidated is: {len(tickets_finished_df[tickets_finished_df['Destination']=='Destruction'])}')
print(f'total Tube Return and Externals tickets consolidated is: {len(tickets_finished_df[tickets_finished_df['Destination']=='Tube Return & Externals'])}')

#Display a pivot table of samples still in progress by Destination
print('')
print('Here is the total number of samples still in progress per destination')
print('')
print(tickets_remaining_df.pivot_table(index='Destination',values='Samples',aggfunc='sum',margins='True',margins_name='Total Samples In Progress: '))
print('')
print(f'Production tickets in progress: {len(tickets_remaining_df[tickets_remaining_df['Destination']=='Production'])}')
print(f'XTR tickets in progress: {len(tickets_remaining_df[tickets_remaining_df['Destination']=='XTR'])}')
print(f'Tube Return and Externals tickets in progress: {len(tickets_remaining_df[tickets_remaining_df['Destination']=='Tube Return & Externals'])}')
print(f'Destruction tickets in progress: {len(tickets_remaining_df[tickets_remaining_df['Destination']=='Destruction'])}')

