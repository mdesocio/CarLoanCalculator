# 🚗 Car Loan Payment Reduction Calculator

## 📌 Overview
This Python script helps you calculate how much time and interest you can save by making additional payments toward your car loan principal. It accounts for payments already made and provides a side-by-side comparison of your original loan term versus the reduced term with extra payments.

## ✨ Features
- Calculates loan payoff time based on the **current balance**, not just the original loan term.
- Supports **extra principal payments** to determine how much time and interest you can save.
- Accounts for **payments already made** for accurate projections.
- Displays the **total interest saved** and the **months reduced** from the loan term.

## ▶️ Usage
### 🏃 Running the Script
Run the script using Python:
```sh
python car_loan_calculator.py
```

### 📝 User Inputs
The script will prompt you to enter:
- **Original Loan Balance**: The total amount of the loan at the start.
- **Current Loan Balance**: The remaining principal balance.
- **Annual Interest Rate**: The loan's interest rate as a percentage.
- **Monthly Payment**: The amount paid each month.
- **Extra Payment**: Additional money paid toward the principal.
- **Payments Made**: The number of months you have already made payments.

### 📊 Output
After entering the required information, the script will display:
- The **original loan term** (in months) from the current balance.
- The **reduced loan term** (in months) if extra payments are made.
- The **time saved** in months.
- The **total interest saved** by making extra payments.

## 📌 Example Output
```
Enter the original loan balance: 30000.00
Enter the current loan balance (principal): 27000.00
Enter the annual interest rate (as a percentage): 5.5
Enter your regular monthly payment: 500
Enter additional payment toward the principal each month: 200
Enter the number of payments already made: 6

Loan Payment Details:
Original loan term: 72 months
Reduced loan term with extra payments: 50 months
Time saved: 22 months
Total interest saved: $4000.00
```

## ⚙️ Requirements
- Python 3.x

## 🔍 Notes
- Ensure that your **monthly payment** covers at least the monthly interest, or the script will raise an error.
- If extra payments are **too low**, the reduction in time and interest savings may be minimal.

## 📜 License
This project is open-source and available for use and modification.

