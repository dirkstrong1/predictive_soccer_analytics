-- practice sql

SELECT l.name AS league,
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
        USING (country_id);