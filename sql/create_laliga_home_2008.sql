--create laliga home records for 2008 season

CREATE TABLE laliga_home_2008
AS (
   SELECT
    laliga_home.home_team AS hometeam,
    SUM(laliga_home.h_win) AS home_win,
    SUM(laliga_home.h_loss) AS home_loss,
    SUM(laliga_home.h_draws) AS home_draws,
    SUM(laliga_home.home_team_goal) AS home_goals,
    SUM(laliga_home.away_team_goal) AS home_agst
    
    FROM 

    (SELECT
    Season, 
    t1.team_long_name AS home_team,
    t2.team_long_name AS away_team,
    away_team_goal, home_team_goal,
    CASE WHEN home_team_goal > away_team_goal THEN 1 ELSE 0 END AS h_win,
    CASE WHEN home_team_goal < away_team_goal THEN 1 ELSE 0 END AS h_loss,
    CASE WHEN home_team_goal = away_team_goal THEN 1 ELSE 0 END AS h_draws
    FROM Match
    JOIN Team AS t1
        ON Match.home_team_api_id = t1.team_api_id 
    JOIN Team AS t2
        ON Match.away_team_api_id = t2.team_api_id 
    JOIN league AS l
        USING (country_id)
    WHERE Season = '2008/2009' AND l.name = 'Spain LIGA BBVA') as laliga_home

    GROUP BY laliga_home.home_team);  