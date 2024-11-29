#Jordan Faulkner, 3-18-2024
#In this project I will write a script that will use a csv and create TaT visualizations for SRS 

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
csv = 'SRS_Data_3-18-2024.csv'
full_srs_data = pd.read_csv(csv,delimiter = ',')

#Create a subset of the full SRS Data in a seperate DF 
new_srs_data = full_srs_data[['KEY','STATUS','CREATED','RESOLUTIONDATE','Destination','NUMBER_OF_SAMPLES','SUMMARY']]

#Change the data types from object to the proper datatypes 
new_srs_data['Resolved Date'] = pd.to_datetime(new_srs_data['RESOLUTIONDATE'])
new_srs_data['Created Date'] = pd.to_datetime(new_srs_data['CREATED'])
new_srs_data['# of Samples'] = pd.to_numeric(new_srs_data['NUMBER_OF_SAMPLES'],downcast='integer')
new_srs_data['Summary'] = new_srs_data['SUMMARY'].astype(str)

#order the columns and include the new proper data type columns 
new_srs_data = new_srs_data[['KEY','STATUS','Created Date','Resolved Date','Destination','# of Samples','Summary']]


#Fill in null values according to best practice 
new_srs_data.fillna({'# of Samples':95}, axis = 0,inplace = True)
new_srs_data.fillna({'Destination':'No Destination'},axis = 0, inplace = True)


#Drop sample destruction and Malaria tickets from closed SRS df 
#new_srs_data[~new_srs_data.Summary.str.contains('Malaria (DNA)')]
#discard = 'DESTRUCTION'
#new_srs_data[~new_srs_data.Summary.str.contains('|'.join(discard))]

#Check which values are Null in the Dataframe
#null_val = new_srs_data.isnull().any(axis = 1)
#null_rows = new_srs_data[null_val]
#print(null_rows)

#Create the TaT column in the DataFrame 
new_srs_data['TaT'] = new_srs_data['Resolved Date'] - new_srs_data['Created Date']


#Sort the Dataframe by Status 
new_srs_data.sort_values(by = 'STATUS',inplace= True)

#Drop SRS Tickets that are not Closed Status and check again if there are null values 
srs_data_closed_only = new_srs_data[new_srs_data['STATUS'] == 'Closed']
srs_data_closed_only['Year Week'] = srs_data_closed_only['Created Date'].dt.strftime('%Y-w%V')

#null_val = srs_data_closed_only.isnull().any(axis = 1)
#null_rows = srs_data_closed_only[null_val]
#Now there are no null values in the dataframe 

#Make a new dataframe from the closed dataframe, only include columns needed, and correct dtypes 
srs_data_closed_only_nosummary = srs_data_closed_only[['KEY','Destination','# of Samples','Created Date','TaT','Year Week']]
srs_data_closed_only_nosummary['# of Samples'] = srs_data_closed_only_nosummary['# of Samples'].astype('int')
srs_data_closed_only_nosummary['Created Date'] = srs_data_closed_only_nosummary['Created Date'].dt.date
srs_data_closed_only_nosummary['Created Date'] = pd.to_datetime(srs_data_closed_only_nosummary['Created Date'])
srs_data_closed_only_nosummary['TaT'] = srs_data_closed_only_nosummary['TaT'].dt.days


#Make mini DFs for each Destination and the SRS keys that belong to them with the Date Resolved and TaT
fluidigm_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Fluidigm']
bge_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Blended Genome Exome']
pico_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Pico']
storage_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Storage']
tube_return_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Tube Return & Externals']
extraction_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Extraction']
rna_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='RNA']
sge_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Standard Germline Exome']
wgs_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='WGS']
infinium_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Infinium']
exome_express_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Exome Express']
pcr_free_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='PCR Free']
blood_biopsy_tat = srs_data_closed_only_nosummary[srs_data_closed_only_nosummary['Destination']=='Blood Biopsy']
only_production_df = srs_data_closed_only_nosummary[(srs_data_closed_only_nosummary['Destination']!='Tube Return & Externals')&(srs_data_closed_only['Destination']!= 'Extraction')&(srs_data_closed_only_nosummary['Destination']!='Storage')]


#All SRS Data bar graph - srs_data_closed_only_nosummary
#Production only bar graph - only_production_df
#Production plot and line graph = production_tat_by_key_and_yw
#Tube Return plot and line graph = tube_return_tat_by_key_and_yw
#Extraction plot and line graph = xtr_tat_by_key_and_yw

#Initialize Dash App 
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

#Alias the DataFrames needed 
df1 = pd.DataFrame(srs_data_closed_only_nosummary)#All SRS Data bar graph
df1.sort_values(by='Destination')
df2 = pd.DataFrame(only_production_df)#Production plot and line graph
df3 = pd.DataFrame(tube_return_tat)#Tube Return plot and line graph
df4 = pd.DataFrame(extraction_tat)#Extraction plot and line graph

#Bar Graph for total samples completed stacked by Destination
fig1 = px.bar(data_frame=df1,y='# of Samples',x='Year Week',template='plotly_dark',orientation='v',color='Destination',title = 'SRS Throughput (All Samples Consolidated (Grouped by Destination)',hover_data=['KEY','Destination','# of Samples','Created Date'])
fig1.update_xaxes(showline = True,mirror = True)
fig1.update_yaxes(showline = True,mirror = True)
fig1.update_layout(xaxis={'categoryorder':'total descending'})

#Point Plot for Production Samples (Complete) by Year Week
fig2 = px.scatter(df2,x='KEY',y='TaT',color = 'Year Week',facet_col='Year Week',template='plotly_dark',title= 'Completed Production Samples TaT by Year Week',hover_data=['KEY','Destination','TaT','# of Samples'])
fig2.update_yaxes(title_text = 'TaT Days',tick0 = 0, dtick = 1,showline = True,linewidth = 2,mirror = True)
fig2.update_xaxes(showticklabels = False,showline = True,linewidth = 2,mirror = True)
fig2.update_traces(marker_size = 4)
production_mean = np.round(df2.loc[:, 'TaT'].mean(),5)
production_std = np.round(df2.loc[:,'TaT'].std(),4)
production_n = df2[df2.columns[0]].count()
fig2.add_annotation(text = f'Mean:{production_mean}',showarrow=False,xref="paper", yref="paper",x=1.16, y=0.8)
fig2.add_annotation(text = f'STD: {production_std}',showarrow=False,x = 1.15,y = 0.74,xref = 'paper',yref = 'paper')
fig2.add_annotation(text =f'N:{production_n}',showarrow = False,x = 1.13,y=0.68,xref = 'paper',yref = 'paper')

#Point plot for Tube Return and Externals Samples (Complete) by Year Week
fig3 = px.scatter(df3,x = 'KEY',y='TaT',color ='Year Week',facet_col='Year Week',template='plotly_dark',title= 'Completed Tube Return & External Platings (Completed) TaT by Year Week',hover_data=['KEY','Destination','TaT','# of Samples'])
fig3.update_yaxes(title_text = 'TaT Days',tick0 = 0, dtick = 1,showline = True,linewidth = 2,mirror = True)
fig3.update_xaxes(showticklabels = False,showline = True,linewidth = 2,mirror = True)
fig3.update_traces(marker_size = 4)
tubereturn_mean = np.round(df3.loc[:, 'TaT'].mean(),5)
tubereturn_std = np.round(df3.loc[:,'TaT'].std(),4)
tubereturn_n = df3[df3.columns[0]].count()
fig3.add_annotation(text = f'Mean:{tubereturn_mean}',showarrow=False,xref="paper", yref="paper",x=1.16, y=0.8)
fig3.add_annotation(text = f'STD: {tubereturn_std}',showarrow=False,x = 1.15,y = 0.74,xref = 'paper',yref = 'paper')
fig3.add_annotation(text =f'N:{tubereturn_n}',showarrow = False,x = 1.13,y=0.68,xref = 'paper',yref = 'paper')

#Point plot for Extractions TaT (Complete) by Year Week
fig4 = px.scatter(df4,x = 'KEY',y='TaT',color ='Year Week',facet_col='Year Week',template='plotly_dark',title= 'Extraction Consolidations(Completed) TaT by Year Week',hover_data=['KEY','Destination','TaT','# of Samples'])
fig4.update_yaxes(title_text = 'TaT Days',tick0 = 0, dtick = 1,showline = True,linewidth = 2,mirror = True)
fig4.update_xaxes(showticklabels = False,showline = True,linewidth = 2,mirror = True)
fig4.update_traces(marker_size = 4)
xtr_mean = np.round(df4.loc[:, 'TaT'].mean(),5)
xtr_std = np.round(df4.loc[:,'TaT'].std(),4)
xtr_n = df4[df4.columns[0]].count()
fig4.add_annotation(text = f'Mean:{xtr_mean}',showarrow=False,xref="paper", yref="paper",x=1.16, y=0.8)
fig4.add_annotation(text = f'STD: {xtr_std}',showarrow=False,x = 1.15,y = 0.74,xref = 'paper',yref = 'paper')
fig4.add_annotation(text =f'N:{xtr_n}',showarrow = False,x = 1.13,y=0.68,xref = 'paper',yref = 'paper')

#Create Dash App with dropdown menu showing each plot 

app.layout = html.Div(children=[
    html.H1(children='SRS Data', style={'text-align': 'center'}),
    

    html.Div([
        html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
        dcc.Dropdown( #Dropdown Menu 
            id='dropdown',
            options=[
                {'label': 'SRS Throughput', 'value': 'graph1'},
                {'label': 'Production TaT', 'value': 'graph2'},
                {'label': 'Tube Return & Externals TaT', 'value': 'graph3'},
                {'label':'Extractions TaT',  'value': 'graph4'}
                    ],
            value='graph1', #Default graph is the first when app opens 
            style={'color':'black','width':'60%'}),
        
    html.Div(dcc.Graph(id='graph')),        
        ]),

])

@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)


def select_graph(value):
    if value == 'graph1':
        return fig1
    elif value == 'graph2':
       return fig2
    elif value == 'graph3':
        return fig3
    elif value == 'graph4':
        return fig4 

if __name__ == '__main__':
    app.run_server(debug=True)

