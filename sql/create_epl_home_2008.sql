-- EPL home_team_stats in 2008/2009 season

CREATE TABLE epl_home_2008
AS (
   SELECT
    epl_home.home_team AS hometeam,
    SUM(epl_home.h_win) AS home_win,
    SUM(epl_home.h_loss) AS home_loss,
    SUM(epl_home.h_draws) AS home_draws,
    SUM(epl_home.home_team_goal) AS home_goals,
    SUM(epl_home.away_team_goal) AS home_agst
    
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
    WHERE Season = '2008/2009' AND l.name = 'England Premier League') as epl_home

    GROUP BY epl_home.home_team);  


