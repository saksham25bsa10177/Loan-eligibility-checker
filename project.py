# loan_check.py
MIN_CREDIT_SCORE = 650
MIN_INCOME = 40000.0         # USD per year
MAX_DTI_RATIO = 0.35        # e.g., 0.35 == 35%

def main():
    print(" ### Loan Eligibility Check ### ")

    try:
        # Get Credit Score input
        credit_score = int(input("Enter your Credit Score: "))

        # Get Annual Income input
        annual_income = float(input("Enter your Annual Income (in dollars): $"))

        # Get Monthly Debt Payments input
        total_monthly_debt = float(input("Enter your Total Monthly Debt Payments (in dollars): $"))

        # Compute monthly income
        monthly_income = annual_income / 12.0

    except ValueError:
        print("\nERROR: Please enter valid numeric values for all inputs.")
        return

    # Calculate DTI Ratio
    if monthly_income > 0:
        dti_ratio = total_monthly_debt / monthly_income
    else:
        dti_ratio = 1.0  # set high so it will fail
        print("\nWarning: Monthly income is zero or negative. DTI set to 100% for safety.")

    # Check Eligibility
    is_eligible = True
    reasons_for_rejection = []

    # Rule 1: Credit score
    if credit_score < MIN_CREDIT_SCORE:
        is_eligible = False
        reasons_for_rejection.append(
            f"Credit Score ({credit_score}) is below the minimum required ({MIN_CREDIT_SCORE})."
        )

    # Rule 2: Annual income
    if annual_income < MIN_INCOME:
        is_eligible = False
        reasons_for_rejection.append(
            f"Annual Income (${annual_income:,.2f}) is below the minimum required (${MIN_INCOME:,.2f})."
        )

    # Rule 3: DTI ratio
    if dti_ratio > MAX_DTI_RATIO:
        is_eligible = False
        reasons_for_rejection.append(
            f"DTI Ratio ({dti_ratio:.2f} = {dti_ratio*100:.0f}%) is above the maximum allowed ({MAX_DTI_RATIO*100:.0f}%)."
        )

    # Final result
    print("\n" + "="*40)
    print("             FINAL DECISION")
    print("="*40)

    if is_eligible:
        print("CONGRATULATIONS! You are ELIGIBLE for the loan.")
        print("\nBased on the current rules, you meet all requirements.")
    else:
        print("SORRY. You are NOT ELIGIBLE for the loan.")
        print("\nReasons for Ineligibility:")
        for reason in reasons_for_rejection:
            print(f"- {reason}")

    print("="*40)


if __name__ == "__main__":
    main()