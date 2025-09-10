# 📊 Customer Churn Analyzer

This project provides a data-driven approach to predicting and reducing customer churn in the telecommunications industry. By leveraging machine learning, this analysis identifies customers at a high risk of leaving and pinpoints the key factors driving their decisions, enabling proactive and targeted retention strategies.

---

### 🚀 Project Overview

**Business Problem:** High customer churn directly impacts revenue, as acquiring new customers is significantly more expensive than retaining existing ones. Understanding and mitigating churn is crucial for sustained profitability.

**Project Objective:** The goal is to build a predictive model to identify customers at high risk of churning and understand the key drivers to inform proactive retention strategies. This analysis uses a dataset of customer usage patterns, subscription details, and demographic information to train and evaluate several machine learning models.

---

### ⚙️ Data & Methodology

**Dataset:** The project utilizes the `Customer Churn.csv` dataset, which contains 3150 rows and 14 columns of anonymized customer data[cite: 19].

**Data Preparation:** The initial data preparation involved several key steps:
* Standardized column names for consistency.
* Removed 300 duplicate rows to ensure data quality.
* Confirmed that no missing values were present in the dataset.

**Key Insights from Analysis:**
* **Imbalanced Data:** The dataset shows a churn rate of 15.6%, indicating an imbalance between churners and non-churners. This was managed during modeling by using `class_weight='balanced'`.
* **Strongest Correlations:** The features with the strongest correlation to churn were `Complains` and `Subscription_Length`.
* **Usage Patterns:** Customers who churned demonstrated significantly lower call duration (`Seconds_of_Use`) and SMS frequency.

**Model Development:**
* [cite_start]**Algorithms Tested:** The analysis evaluated Logistic Regression, Decision Tree, and Random Forest models[cite: 34].
* [cite_start]**Optimization:** `GridSearchCV` was employed to tune the hyperparameters of the Random Forest model, specifically optimizing for the F1-score to best handle the class imbalance[cite: 36].
* [cite_start]**Final Model:** An **Optimized Random Forest** was selected as the final model due to its superior F1-score and overall accuracy[cite: 38].

---

### 📈 Final Model Performance

The final Optimized Random Forest model achieved strong performance on the unseen test data:

* [cite_start]**Accuracy:** 96.1% [cite: 41]
* [cite_start]**F1-Score (for Churn class):** 0.870 [cite: 42]
* [cite_start]**AUC (Area Under ROC Curve):** 0.983 [cite: 42]

---

### 🎯 Key Drivers of Customer Churn

The model identified the following five factors as the most influential in predicting customer churn:

1.  [cite_start]Subscription Length [cite: 45]
2.  [cite_start]Complains [cite: 46]
3.  [cite_start]Seconds of Use [cite: 47]
4.  [cite_start]Frequency of SMS [cite: 48]
5.  [cite_start]Distinct Called Numbers [cite: 49]

---

### 💡 Actionable Business Recommendations

Based on the model's findings, the following strategies are recommended to reduce churn:

1.  [cite_start]**Onboarding & Loyalty:** Target new customers with shorter subscription lengths for enhanced onboarding programs and early loyalty rewards[cite: 52].
2.  [cite_start]**Proactive Complaint Management:** Implement a high-priority alert system for any customer complaint to trigger engagement from a retention specialist[cite: 54].
3.  [cite_start]**Usage-Based Re-engagement:** Automate outreach campaigns for customers whose call or SMS usage drops below a defined threshold[cite: 56].
4.  [cite_start]**Tariff Plan Optimization:** Review and $A/B$ test Tariff Plan 2 to improve its value proposition, as it is associated with a higher churn rate[cite: 58].

---

### 📂 Repository Contents

* `customer_churn_analysis.ipynb`: The complete Jupyter Notebook containing all steps from data loading and cleaning to EDA, model training, and final recommendations.
* `Customer Churn.csv`: The raw dataset used for the analysis.
* [cite_start]`Customer_Churn.pdf`: The presentation slides summarizing the project's findings and recommendations[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67].
* `customer_churn_model.pkl`: The final, trained Optimized Random Forest model saved as a pickle file for deployment.
* `README.md`: This file, providing a comprehensive overview of the project.

---

### 🛠️ Setup and Usage

To replicate this analysis, please follow the steps below.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/customer-churn-analyzer.git](https://github.com/your-username/customer-churn-analyzer.git)
cd customer-churn-analyzer
