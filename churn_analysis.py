import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_excel("data/Telco-Customer-Churn.xlsx")

# First look at data
print(df.head())

# Dataset info
print(df.info())

# Shape of dataset
print("Rows, Columns:", df.shape)
# Convert TotalCharges to numeric
# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Handle missing values safely
median_total_charges = df['TotalCharges'].median()
df['TotalCharges'] = df['TotalCharges'].fillna(median_total_charges)

print("Missing values after treatment:", df['TotalCharges'].isnull().sum())
# Encode target variable
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

print(df['Churn'].value_counts())
# Overall churn rate
churn_rate = df['Churn'].mean()
print(f"Overall Churn Rate: {churn_rate:.2%}")

# Churn by Contract Type
plt.figure(figsize=(6,4))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title('Churn by Contract Type')
plt.show()


# Churn vs Tenure
plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title('Churn vs Customer Tenure')
plt.show()


# Monthly Charges vs Churn
plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges vs Churn')
plt.show()

#churn by Payment Method
plt.figure(figsize=(8,4))
sns.countplot(y='PaymentMethod', hue='Churn', data=df)
plt.title('Churn by Payment Method')
plt.show()

# Churn by Internet Service
plt.figure(figsize=(6,4))
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title('Churn by Internet Service')
plt.show()
