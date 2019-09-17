-- team match stats

SELECT Date, 
        Season, 
        t1.team_long_name AS home_team,
        t2.team_long_name AS away_team, 
        home_team_goal, away_team_goal, 
        home_team_api_id, away_team_api_id
FROM Match
JOIN Team AS t1
    ON Match.home_team_api_id = t1.team_api_id 
JOIN Team AS t2
    ON Match.away_team_api_id = t2.team_api_id 
WHERE league_id=1729;


