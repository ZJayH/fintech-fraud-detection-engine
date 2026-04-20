# Fintech Risk Analytics: Real-Time Fraud Detection Engine

## Dashboard Preview
![Risk Dashboard](dashboard_preview.png)

## Project Overview
In the fast-paced Fintech sector, identifying fraudulent transactions within milliseconds is critical. This project simulates a highly scalable **Risk Control & Anti-Fraud Data Pipeline**. By analyzing a dataset of 50,000 simulated cross-border transactions, the project identifies organized fraud rings utilizing "Velocity Attacks" (rapid, high-value transfers) and visualizes the interception threshold.

## 🛠️ Tech Stack & Architecture
* **PostgreSQL (Advanced SQL):** Database architecture and complex temporal feature extraction.
* **Python (Scikit-Learn, Pandas):** Machine Learning model training and Feature Importance validation.
* **Tableau:** Visual threshold configuration and real-time risk radar dashboarding.

##  Key Actions & Methodology

### 1. Feature Engineering with SQL Window Functions
Raw transaction logs lack the context needed to detect fraud rings. I engineered temporal features using PostgreSQL Window Functions (`PARTITION BY`, `RANGE BETWEEN INTERVAL`) to calculate the rolling 10-minute transaction count (`txn_count_10m`) for every user, transforming static data into dynamic behavior flows.

### 2. Machine Learning Validation (Random Forest)
To avoid relying on arbitrary business rules, I trained a `RandomForestClassifier` to statistically validate risk indicators. The model's Feature Importance extraction mathematically proved that transaction velocity (`txn_count_10m`) is just as lethal a predictor (36% importance) as the absolute transaction amount (36%).

### 3. Visual Interception Strategy (Tableau)
Developed a dark-mode Risk Radar Dashboard to separate signal from noise. By mapping the algorithmically derived Risk Score to a 2-step color divergence, the dashboard instantly isolates high-risk clusters (red) from tens of thousands of legitimate transactions (blue), enabling instant operational decision-making.

## Business Impact
* **Precision Targeting:** Successfully isolated 500 high-risk velocity attacks hidden within 49,500 normal transactions.
* **Rule Engine Optimization:** Translated opaque ML outputs into transparent, actionable metrics (Risk Score = Amount Weight + Velocity Weight) for compliance and manual review teams.
