import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('cleaned_telco_customer_churn.csv')
mean_charges =df['monthlycharges'].mean()
median_charges =df['monthlycharges'].median()
print("Monthly charges Mean : ", mean_charges)
print("Monthly charges Median : ", median_charges)

plt.figure()
plt.hist(df['monthlycharges'], bins=20 )
plt.xlabel('Monthly Charges')
plt.ylabel('Number of Customers')
plt.title('Distribution of Monthly Charges')

plt.figure()
plt.boxplot(df['monthlycharges'])
plt.ylabel('Monthly Charges')
plt.title('Box Plot of Monthly Charges')

churn_yes = df[df['churn'] == 'Yes']['monthlycharges']
churn_no = df[df['churn'] == 'No']['monthlycharges']
print("Average Monthly Charges (churn = Yes) :", churn_yes.mean())
print("Average Monthly Charges (churn = No) :", churn_no.mean())

plt.figure()
plt.boxplot([churn_yes, churn_no], labels=['Churn = Yes', 'Churn = No'])
plt.ylabel('Monthly Charges')
plt.title('Monthly Charges by Churn Status')


plt.show()