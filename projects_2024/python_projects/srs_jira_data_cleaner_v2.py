import pandas as pd 
import numpy as np
from datetime import datetime
import os

def find_csv_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().startswith("tat") and file.endswith(".csv"):
                return os.path.join(root, file)
    return None

directory_path = "C:\\Users\\jfaulkne\\Desktop\\srs_jira_data" 
csv_file_path = find_csv_file(directory_path)

if csv_file_path:
    df = pd.read_csv(csv_file_path)
    print("DataFrame loaded successfully.")
else:
    print("CSV file starting with 'tat' not found in the specified directory.")

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
print(df.dtypes)
print(df['TaT'])
#Save the csv to the designated folder for SRS Data 
path = 'C:\\Users\\jfaulkne\Desktop\\SRSData\\'
output_file = os.path.join(path,'SRS Data.csv')
df.to_csv(output_file, index=False)
