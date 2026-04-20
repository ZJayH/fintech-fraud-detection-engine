import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Simulate the risk feature dataset extracted from SQL
# Columns: Transaction Amount, Transaction Count (10 mins), Cross Border Flag, Fraud Label (Target)
data = {
    'txn_amount':      [50, 12000, 8500,  12, 300, 5000,  20, 9000],
    'txn_count_10m':   [ 1,     5,    6,   1,   2,    4,   1,    7],
    'is_cross_border': [ 0,     1,    1,   0,   0,    1,   0,    1],
    'is_fraud':        [ 0,     1,    1,   0,   0,    1,   0,    1]  # 0: Normal, 1: Fraud
}
df = pd.DataFrame(data)

# 2. Define Features (X) and Target Variable (y)
X = df[['txn_amount', 'txn_count_10m', 'is_cross_border']]
y = df['is_fraud']

# 3. Initialize and train the Random Forest Classifier
print("Training Risk Control Model (Random Forest)...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# 4. Extract and rank Feature Importance
print("\n=== Feature Importance Report ===")
importances = rf_model.feature_importances_
feature_names = X.columns

# Sort and display
feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False)

for index, row in feature_imp_df.iterrows():
    print(f"Feature [{row['Feature']}]: {row['Importance']:.2%}")
    
print("\nBusiness Conclusion: The system has automatically identified the key indicators for intercepting fraudulent transactions.")