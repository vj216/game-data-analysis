import pandas as pd
import duckdb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("data/gaming_data.csv")

df["EngagementLevelEncoded"] = df["EngagementLevel"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

features = ["PlayTimeHours","SessionsPerWeek","AvgSessionDurationMinutes","InGamePurchases","PlayerLevel","AchievementsUnlocked"]

X=df[features]
y = df["EngagementLevelEncoded"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# random forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\n=== RANDOM FOREST CLASSIFIER ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))

# logistic regressor
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

log_reg_pred = log_reg.predict(X_test_scaled)
print("\n=== LOGISTIC REGRESSION ===")
print("Accuracy:", accuracy_score(y_test, log_reg_pred))
print(classification_report(y_test, log_reg_pred))

importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print(importance)
