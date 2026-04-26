# Mobile Game Engagement Analytics

Analysing what drives player engagement in mobile games using SQL, Python, and ML.

---

## Business Questions

- What separates high-engagement players from low-engagement ones?
- Which genres and difficulty levels produce the most engaged players?
- Can we predict a player's engagement level and explain why?

---

## Project Structure

```
mobile-game-engagement-analytics/
│
├── data/
│   └── gaming_data.csv       # Kaggle: Online Gaming Behavior Dataset
│
├── main.py                   # DuckDB + SQL queries + Matplotlib visualisations
├── model.py                  # Random Forest, Logistic Regression, SHAP analysis
├── analysis.sql              # SQL queries for exploration
├── requirements.txt
└── README.md
```

---

## What's Inside

**`analysis.sql`** — exploratory queries covering:
- Engagement distribution across player base
- Playtime, session frequency, and session duration by engagement tier
- In-game purchases and achievements vs engagement
- Difficulty level and genre breakdowns

**`main.py`** — loads data into DuckDB, runs SQL queries, and plots genre vs average playtime

**`model.py`** — predicts player engagement level (Low / Medium / High) using:
- Random Forest Classifier
- Logistic Regression (baseline)
- SHAP analysis to explain which features drive high engagement

---

## Key Findings

- Sessions per week is the strongest predictor of high engagement
- High-engagement players unlock significantly more achievements
- Random Forest outperforms Logistic Regression on this classification task
- SHAP analysis shows playtime and session frequency push players toward high engagement the most

---

## Stack

| Tool | Purpose |
|---|---|
| DuckDB | In-process SQL analytics |
| Pandas | Data loading and wrangling |
| Matplotlib | Visualisations |
| scikit-learn | Classification models |
| SHAP | Model explainability |

---

## How to Run

```bash
git clone https://github.com/YOUR_USERNAME/mobile-game-engagement-analytics
cd mobile-game-engagement-analytics

# Add dataset: download from Kaggle and place at data/gaming_data.csv

python main.py      # visualisations
python model.py     # ML models + SHAP
```

---

## Dataset

[Online Gaming Behavior Dataset](https://www.kaggle.com/) — Kaggle
