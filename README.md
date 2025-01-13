# 📞 Telco Customer Churn Analysis  

## 📋 Project Overview  
This project aims to analyze customer churn for a telecommunication company. By leveraging data analysis and machine learning techniques, we identify key factors contributing to customer churn and develop predictive models to improve retention strategies.  

---

## 🎯 Objectives  
- **Understand churn behavior**: Explore patterns in customer behavior and demographics.  
- **Identify churn factors**: Analyze variables influencing churn, such as contract type, payment method, and tenure.  
- **Build predictive models**: Use machine learning to predict churn and evaluate model performance.  
- **Provide actionable insights**: Suggest strategies to reduce churn rates.  

---

## 🗂️ Dataset  
- **Source**: [Kaggle Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  
- **Size**: ~7,043 rows, 21 columns  
- **Features**:  
  - Customer demographic details (e.g., gender, tenure, etc.)  
  - Service details (e.g., internet service, contract type, etc.)  
  - Churn status (target variable: **Yes/No**)  

---

## 🛠️ Tools and Technologies  
- **Languages**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Machine Learning Models**: Random Forest, KNN  

---

## 🧪 Methodology  

1. **Data Cleaning and Preparation**  
   - Handle missing values and outliers.  
   - Encode categorical variables (Label Encoding).  
   - Normalize numerical features.  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize customer distributions and churn patterns.  
   - Analyze correlations and significant features.
   
3. **Feature Importance**  
   - Using Random Forest


3. **Model Development**  
   - Train machine learning models on a balanced dataset (SMOTE applied).  
   - Evaluate model performance using metrics like accuracy, precision, recall, and F1 score.  

4. **Insights and Recommendations**  
   - Identify critical factors influencing churn (e.g., contract type, monthly charges).  
   - Propose customer retention strategies.  

---

## 📊 Key Findings  
- Customers with **month-to-month contracts** are more likely to churn.  
- High **monthly charges** and short **tenure periods** correlate with churn.  
- Payment methods such as **electronic checks** show higher churn rates compared to other methods.  

---

## 🚀 Results  
- **Best Model**: Random Forest Classifier  
- **Performance Metrics**:  
  - Accuracy: 93%  
  - Precision: 84%  
  - Recall: 92%  
  - F1 Score: 88%  


