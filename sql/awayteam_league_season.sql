-- away team per league per season stats

CREATE TABLE awayteam_stats 
AS(
    SELECT
        away.away_team AS awayteam,
        season,
        league,
        SUM(away.a_win) AS away_win,
        SUM(away.a_loss) AS away_loss,
        SUM(away.a_draws) AS away_draws,
        SUM(away.away_team_goal) AS away_goals,
        SUM(away.home_team_goal) AS away_agst
        
        FROM 
        (SELECT
        l.name as league,
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
            USING (country_id)) as away

        GROUP BY awayteam,season, league);  
        