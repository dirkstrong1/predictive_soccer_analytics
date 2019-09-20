import pandas as pd 
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

def df_top_builder(league_name: str):
    """This function takes in the name of a soccer league
        and returns a pandas dataframe"""
    assert isinstance(league_name, str), 'League name needs to be a str'
    
    seasons = ['2008/2009', '2009/2010', '2010/2011',
                '2012/2013', '2014/2015', '2015/2016']

    engine = create_engine('postgresql:///soccer_database')
       
    list_df = []
    for season in seasons:
        query = f"""SELECT * FROM team_stats WHERE league = '{league_name}'
        AND season = '{season}' ORDER BY pts DESC LIMIT 1;"""

        data = pd.read_sql_query(query, engine)
        list_df.append(data)
    df = pd.concat(list_df)
    
    return df.reset_index(drop=True) 

def area_plotter(league_dataframes:list, y_axis:list, league_names):
    """This function takes a list of league pandas 
        dataframes and a list of selector 
        and, it ouput back area plot"""
    fig, axs = plt.subplots(5, 2, figsize=(20,25), gridspec_kw={'wspace': 0.3, 'hspace': 0.3})
    for ax, data in zip(axs.flatten(), league_dataframes.values()):
        data.plot.area(x='season', y=y_axis, ax = ax)
    
    for ax, name in zip(axs.flatten(), league_names):
        ax.set_title(name+' Champion')

    return plt.show() 