from sqlalchemy import create_engine
import pandas as pd 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

engine = create_engine('postgresql:///soccer_database')



def df_gd_builder(parameter, league_name):

    """Builds a pandas dataframe for goal differential from a SQL query
    parameter = assigning aggregated selection
    league_name = league of interest selected"""
    engine = create_engine('postgresql:///soccer_database')
    df_gd_league = pd.read_sql_query(f"""SELECT club, SUM(ABS(gol_dif)) AS {parameter}
                         FROM team_stats 
                         WHERE league = '{league_name}'
                         GROUP BY club
                         ORDER BY {parameter} DESC;""", engine)
    return df_gd_league



def league_ttest(epl, df_league, parameter, alpha):
    
    """Conducts a two tail T-test using English Premier League as population and alternative league as sample
       Alpha = Set significant threshold for test
       EPL = population to test against
       df_league = Sample league for testing"""


    epl_mean = epl.mean()
    n = len(df_league['club'])
    df = n-1
    t_critical = stats.t.ppf(1-alpha, df)
    league_epl_ttest = stats.ttest_1samp(a= df_league[f"{parameter}"], popmean= epl_mean)
    t_value = league_epl_ttest[0]
    p_value = league_epl_ttest[1]

    #if abs(t_value) > t_critical and p_value < alpha:
        #print('Reject null hypthesis')
    #elif abs(t_value) < t_critical:
        #print('Dont reject null hypothesis')

    return (f"""T-Critical = {t_critical}, T-Value = {t_value}, P-Value = {p_value}""")




def df_total_goal_builder(parameter, league_name):

    """Builds a pandas dataframe for total goals from a SQL query
    
    parameter = assigning aggregated selection
    league_name = league of interest selected"""


    engine = create_engine('postgresql:///soccer_database')
    df_goal_league = pd.read_sql_query(f"""SELECT club, SUM(gol_for) AS {parameter}
                         FROM team_stats 
                         WHERE league = '{league_name}'
                         GROUP BY club
                         ORDER BY {parameter} DESC;""", engine)
    return df_goal_league
    


def df_draw_percent_builder(parameter, league_name):
    """Builds a pandas dataframe for percentage draws from a SQL query
    
    parameter = assigning aggregated selection
    league_name = league of interest selected"""


    engine = create_engine('postgresql:///soccer_database')
    df_draw_league = pd.read_sql_query(f"""SELECT club, SUM(draws)/SUM(win+loss+draws) AS {parameter}
                         FROM team_stats 
                         WHERE league = '{league_name}'
                         GROUP BY club
                         ORDER BY {parameter} DESC;""", engine)
    return df_draw_league