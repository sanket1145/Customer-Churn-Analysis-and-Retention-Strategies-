SELECT 
    Contract,
    PaymentMethod,
    AVG(MonthlyCharges) AS avg_monthly_charges,
    COUNT(*) AS churned_customers
FROM churn_data
WHERE Churn = 'Yes'
GROUP BY Contract, PaymentMethod
ORDER BY churned_customers DESC
LIMIT 5;
