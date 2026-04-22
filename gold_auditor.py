# Project 3: Practical Gold Price Auditor 
# Goal: Finding the "Hidden" cost in a jewelry quote.

print("--- ⚖️ GOLD SHOP DEFENDER ---")

# 1. RAW DATA INPUTS
# Note: Use float so the user can enter decimals (like 10.5 grams)
rate_22k = float(input("Today's 22K rate per gram (₹): "))
gross_wt = float(input("Total weight on scale (grams): "))
stone_wt = float(input("Weight of stones (0 if none): "))
quote = float(input("Total price shop is asking (₹): "))

# 2. THE CALCULATIONS
net_gold_wt = gross_wt - stone_wt
pure_gold_value = net_gold_wt * rate_22k

# Including mandatory Govt charges (GST 3% + HUID ₹45)
govt_charges = (pure_gold_value * 0.03) + 45
fair_price_limit = pure_gold_value + govt_charges

# 3. EXPOSING THE HIDDEN FEES (Making Charges + Wastage)
extra_fees = quote - fair_price_limit
markup_percentage = (extra_fees / pure_gold_value) * 100

# 4. THE TRUTH REPORT
print("\n" + "="*35)
print("          BILL ANALYSIS")
print("="*35)
print(f"Net Gold:        {net_gold_wt} grams")
print(f"Gold Value:      ₹{pure_gold_value:,.2f}")
print(f"Govt Tax + HUID: ₹{govt_charges:,.2f}")
print("-" * 35)
print(f"HIDDEN CHARGES:  ₹{extra_fees:,.2f}")
print(f"PERCENTAGE:      {markup_percentage:.1f}%")
print("="*35)

# 5. THE ADVICE
if markup_percentage > 18:
    print("❌ ALERT: Very high charges. Negotiate or walk away!")
elif markup_percentage > 12:
    print("⚠️  NOTE: Moderate charges. Okay for complex designs.")
else:
    print("✅ SUCCESS: This is a very fair market deal.")