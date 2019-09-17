-- LaLiga away_team_stats in 2008/2009 season

CREATE TABLE laliga_away_2008
AS 
    (SELECT
    laliga_away.away_team AS awayteam,
    SUM(laliga_away.a_win) AS away_win,
    SUM(laliga_away.a_loss) AS away_loss,
    SUM(laliga_away.a_draws) AS away_draws,
    SUM(laliga_away.away_team_goal) AS away_goals,
    SUM(laliga_away.home_team_goal) AS away_agst
    
    FROM 
    (SELECT
    Season, 
    t1.team_long_name AS home_team,
    t2.team_long_name AS away_team,
    away_team_goal, home_team_goal,
    CASE WHEN away_team_goal > home_team_goal THEN 1 ELSE 0 END AS a_win,
    CASE WHEN away_team_goal < home_team_goal THEN 1 ELSE 0 END AS a_loss,
    CASE WHEN away_team_goal = home_team_goal THEN 1 ELSE 0 END AS a_draws
    FROM Match
    JOIN Team AS t1
        ON Match.home_team_api_id = t1.team_api_id 
    JOIN Team AS t2
        ON Match.away_team_api_id = t2.team_api_id 
    JOIN league AS l
        USING (country_id)
    WHERE Season = '2008/2009' AND l.name = 'Spain LIGA BBVA') as laliga_away

    GROUP BY laliga_away.away_team);  