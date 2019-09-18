-- this table has all the team stats per league per season

CREATE TABLE team_stats
AS 
    (SELECT hometeam as club,
            aws.Season,
            aws.league,
            SUM(home_win + away_win) AS win,
            SUM(home_loss + away_loss) AS loss,
            SUM(home_draws + away_draws) AS draws,
            SUM(home_goals + away_goals) AS gol_for,
            SUM(home_agst + away_agst) AS gol_agst,
            SUM(home_goals + away_goals-home_agst - away_agst) AS gol_dif,
            SUM(((home_win + away_win)*3+(home_draws + away_draws))) AS pts
    FROM hometeam_stats AS hs
    JOIN awayteam_stats AS aws
        ON hs.hometeam = aws.awayteam
        AND hs.season = aws.season
        AND hs.league = aws.league
    GROUP BY aws.season, aws.league, hometeam);