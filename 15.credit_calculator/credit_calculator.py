def calculate_credit(loan_amount, annual_interest_rate, years):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    
    # Calculate number of monthly payments
    months = years * 12
    
    # Calculate monthly payment
    if monthly_interest_rate > 0:
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-months))
    else:
        monthly_payment = loan_amount / months
    
    # Calculate total repayment amount
    total_repayment = monthly_payment * months
    
    # Calculate total interest paid
    total_interest = total_repayment - loan_amount
    
    return monthly_payment, total_repayment, total_interest

def main():
    # Get input from user
    loan_amount = float(input("Enter loan amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years for loan repayment: "))
    
    # Calculate credit details
    monthly_payment, total_repayment, total_interest = calculate_credit(loan_amount, annual_interest_rate, years)
    
    # Print results
    print("\nCredit Details:")
    print(f"Loan Amount: ${loan_amount:.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate}%")
    print(f"Repayment Period: {years} years")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Repayment: ${total_repayment:.2f}")
    print(f"Total Interest Paid: ${total_interest:.2f}")

if __name__ == "__main__":
    main()
