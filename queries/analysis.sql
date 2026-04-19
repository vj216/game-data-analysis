-- total players
SELECT COUNT(*) AS total_players FROM players;

-- engagement
SELECT EngagementLevel, COUNT(*) AS players
FROM players GROUP BY EngagementLevel ORDER BY players DESC;

-- Playtime and engagement
SELECT EngagementLevel, AVG(PlayTimeHours) FROM players GROUP BY EngagementLevel;

-- gaming sessions per week vs engagement
SELECT EngagementLevel, AVG(SessionsPerWeek) FROM players GROUP BY EngagementLevel;

-- session duration and engagement level
SELECT EngagementLevel, AVG(AvgSessionDurationMinutes) FROM players GROUP BY EngagementLevel;

-- Purchases and engagement level
SELECT EngagementLevel, AVG(InGamePurchases) as avg_purchases
FROM players
GROUP BY EngagementLevel;

-- ACHIEVEMENTS VS ENGAGEMENT
SELECT EngagementLevel, AVG(AchievementsUnlocked) AS avg_achievements
FROM players
GROUP BY EngagementLevel;

--DIFFICULTY LEVEL VS ENGAGEMENT
SELECT
    GameDifficulty,
    EngagementLevel,
    COUNT(*) AS players
FROM players
GROUP BY GameDifficulty, EngagementLevel
ORDER BY GameDifficulty;

--PLAYER LEVEL VS ENGAGEMENT
SELECT
    EngagementLevel,
    AVG(PlayerLevel) AS avg_level
FROM players
GROUP BY EngagementLevel;

-- GENRE 
SELECT GameGenre, AVG(PlayTimeHours) AS avg_playtime, AVG(InGamePurchases)
FROM players GROUP BY GameGenre ORDER BY avg_playtime DESC;