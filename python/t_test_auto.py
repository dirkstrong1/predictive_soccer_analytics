from sqlalchemy import create_engine
import pandas as pd 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def df_builder(selector: str, parameter: str, league_name: str) -> pd.DataFrame:
    """This function takes in a SQL query aggregate function as 
        a selector,parameter for defining the aggregated function 
        and the name of the league. It returns a pandas dataframe. """
    assert isinstance(selector, str), 'Selector needs to be a string.'
    assert isinstance(parameter, str), 'parameter needs to be a string.'
    assert isinstance(league_name, str), 'league_name needs to be a string.'


    query = f'''SELECT club, {selector} AS {parameter}
                         FROM team_stats 
                         WHERE league = '{league_name}'
                         GROUP BY club
                         ORDER BY {parameter} DESC;'''

    engine = create_engine('postgresql:///soccer_database')
    df = pd.read_sql_query(query, engine)

    return df 

def barh_plotter(data: pd.DataFrame, variable: str):

    """This function takes in a pandas dataframe and string variable.
        It shows a horizontal bar plot of the data"""
    fig, axs = plt.subplots(2,5, gridspec_kw={'wspace': 1, 'hspace': 0.2},
                             figsize=(60, 40), sharex = False)

    for ax, dta in zip(axs.flatten(), data.values()) :
        ax.barh(dta['club'], dta[f'{variable}'])
        ax.set_xlabel(f'{variable}', fontsize=25)
        
    
    for ax, dta in zip(axs.flatten(), data.keys()):
        ax.set_title(dta, fontsize=30)

    return plt.show()

def dist_plotter(data: pd.DataFrame, variable: str):

    """This function takes in a pandas dataframe and string variable.
        It shows a horizontal bar plot of the data"""
    fig, axs = plt.subplots(2,5, gridspec_kw={'wspace': 0.5, 'hspace': 0.5}, figsize=(15, 8), sharex = False)

    for ax, dta in zip(axs.flat, data.values()) :
        sns.distplot(dta[f'{variable}'], hist= False, ax=ax)
        ax.set_xlabel(f'{variable}')
    
    for ax, dta in zip(axs.flatten(), data.keys()):
        ax.set_title(dta)

    return plt.show()



def league_ttest(df_league_one: pd.DataFrame, df_league_two: pd.DataFrame, parameter: str, alpha: float, ):
    
    """Conducts a one tail-ttest with two leagues
       alpha = Set significance level for test
       df_league_one = population to test against
       df_league = Sample league for testing"""
    assert isinstance(df_league_one, pd.DataFrame), 'df_league_one needs to be a pandas dataframe.'
    assert isinstance(df_league_two, pd.DataFrame), 'df_league_two needs to be a pandas dataframe.'
    assert isinstance(alpha, float), 'alpha  needs to be a float.'


    df_league_one_mean = df_league_one.mean()
    n = len(df_league_one['club'])
    df = n-1
    t_critical = stats.t.ppf(1-alpha, df)
    leagues_ttest = stats.ttest_1samp(a= df_league_two[f'{parameter}'], popmean= df_league_one_mean)
    t_value = leagues_ttest[0]
    p_value = leagues_ttest[1]

    stats_values = {}

    stats_values['p_value'] = round(list(p_value)[0], 4)

    if stats_values['p_value'] < alpha:
        return ('Enough evidence to reject null hypothesis')
    elif stats_values['p_value'] > alpha:
        return ('Not enough evidence to reject null hypothesis')
