import duckdb
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/gaming_data.csv')
# DB setup
con = duckdb.connect("game_data.db")
con.execute("DROP TABLE IF EXISTS players")
con.execute("CREATE TABLE players AS SELECT * FROM df")

df_plot = con.execute("""
SELECT GameGenre, AVG(PlayTimeHours) AS avg_playtime
FROM players GROUP BY GameGenre ORDER BY avg_playtime DESC;
""").fetch_df()

plt.plot(df_plot['GameGenre'], df_plot['avg_playtime'], marker='o')
plt.xlabel("Game Genre")
plt.grid(True)
plt.ylabel("Average playtime in hours")
plt.title("Game Genre vs Average Playtime")
plt.show()