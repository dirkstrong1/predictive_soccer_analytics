-- Hometeam per league per season stats
CREATE TABLE hometeam_stats
AS
    (SELECT
        home.home_team AS hometeam,
        season,
        league,
        SUM(home.h_win) AS home_win,
        SUM(home.h_loss) AS home_loss,
        SUM(home.h_draws) AS home_draws,
        SUM(home.home_team_goal) AS home_goals,
        SUM(home.away_team_goal) AS home_agst
        
        FROM 

        (SELECT l.name AS league,
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
        ) as home

        GROUP BY hometeam, season, league);