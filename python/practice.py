from sqlalchemy import create_engine
import pandas as pd 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


    


def df_builder(selector: str, parameter: str, league_name: str) -> pd.DataFrame:
    """This function takes in a SQL query aggregate function as 
        a selector,parameter for defining the aggregated function 
        and the name of the league """
    assert isinstance(selector, str), 'Selector needs to be a string.'
    assert isinstance(parameter, str), 'parameter needs to be a string.'
    assert isinstance(league_name, str), 'league_name needs to be a string.'


    query = f'''SELECT club, {value} AS {parameter}
                         FROM team_stats 
                         WHERE league = '{league_name}'
                         GROUP BY club
                         ORDER BY {parameter} DESC;'''

    engine = create_engine('postgresql:///soccer_database')

    df = pd.read_sql_query(query, engine)

    return df 