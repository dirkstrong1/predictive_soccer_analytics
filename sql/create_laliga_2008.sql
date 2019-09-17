-- create laliga 2008 team stats

CREATE TABLE laliga_2008_stats
AS 
    (SELECT hometeam as club, 
            SUM(home_win + away_win) AS win,
            SUM(home_loss + away_loss) AS loss,
            SUM(home_draws + away_draws) AS draws,
            SUM(home_goals + away_goals) AS gol_for,
            SUM(home_agst + away_agst) AS gol_agst,
            SUM(home_goals + away_goals-home_agst - away_agst) AS gol_dif,
            SUM(((home_win + away_win)*3+(home_draws + away_draws))) AS pts
    FROM laliga_home_2008
    JOIN laliga_away_2008
        ON laliga_home_2008.hometeam = laliga_away_2008.awayteam
    GROUP BY club
    ORDER BY pts DESC);
