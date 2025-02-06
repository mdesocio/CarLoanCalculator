def calculate_loan_term(original_balance, balance, annual_interest_rate, monthly_payment, extra_payment=0, payments_made=0):
    """
    Calculate the time to pay off a loan with optional extra payments towards principal,
    accounting for payments already made.

    Parameters:
        original_balance (float): The original loan balance.
        balance (float): The current loan balance (principal).
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        monthly_payment (float): The regular monthly payment.
        extra_payment (float): The additional payment towards the principal each month. Default is 0.
        payments_made (int): The number of payments already made. Default is 0.

    Returns:
        dict: Contains original and reduced loan term in months and total interest saved.
    """

    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_interest_with_extra = 0

    # Calculate original loan term from current balance without extra payments
    remaining_balance_original = balance
    months_original_remaining = 0
    total_interest_original_remaining = 0

    while remaining_balance_original > 0:
        interest = remaining_balance_original * monthly_interest_rate
        principal_payment = monthly_payment - interest
        if principal_payment <= 0:
            raise ValueError("Monthly payment is too low to cover interest. Increase payment.")
        total_interest_original_remaining += interest
        remaining_balance_original -= principal_payment
        months_original_remaining += 1

    # Calculate reduced loan term with extra payments
    remaining_balance = balance
    months_with_extra = 0
    while remaining_balance > 0:
        interest = remaining_balance * monthly_interest_rate
        principal_payment = (monthly_payment + extra_payment) - interest
        if principal_payment <= 0:
            raise ValueError("Monthly payment + extra payment is too low to cover interest. Increase payment.")
        total_interest_with_extra += interest
        remaining_balance -= principal_payment
        months_with_extra += 1

    # Add payments already made to both terms
    months_original_total = months_original_remaining + payments_made
    months_with_extra += payments_made

    return {
        "original_term_months": months_original_total,
        "reduced_term_months": months_with_extra,
        "months_saved": months_original_total - months_with_extra,
        "total_interest_saved": total_interest_original_remaining - total_interest_with_extra
    }

# Example usage
if __name__ == "__main__":
    original_loan_balance = float(input("Enter the original loan balance: "))
    loan_balance = float(input("Enter the current loan balance (principal): "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
    monthly_payment = float(input("Enter your regular monthly payment: "))
    extra_payment = float(input("Enter additional payment toward the principal each month: "))
    payments_made = int(input("Enter the number of payments already made: "))

    result = calculate_loan_term(original_loan_balance, loan_balance, annual_rate, monthly_payment, extra_payment, payments_made)

    print("\nLoan Payment Details:")
    print(f"Original loan term: {result['original_term_months']} months")
    print(f"Reduced loan term with extra payments: {result['reduced_term_months']} months")
    print(f"Time saved: {result['months_saved']} months")
    print(f"Total interest saved: ${result['total_interest_saved']:.2f}")
