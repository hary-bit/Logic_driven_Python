import pandas as pd
from datetime import datetime, timedelta

# 1. Load the "Messy" Data
df = pd.read_csv('inventory.csv')

# 2. Convert the 'Expiry' column to actual dates Python understands
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])

# 3. Logic: Find items expiring in less than 30 days
soon = datetime.now() + timedelta(days=30)
expiry_alerts = df[df['Expiry_Date'] <= soon]

# 4. Logic: Find items with stock less than 5
stock_alerts = df[df['Quantity'] < 5]

# 5. Output: Combine them into a single report for the owner
report = pd.concat([expiry_alerts, stock_alerts]).drop_duplicates()
report.to_csv('Order_These_Immediately.csv', index=False)

print("Analysis Complete. Report generated for the shopkeeper.")