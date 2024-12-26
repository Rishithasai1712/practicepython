def calculate_new_capital(initial_balance, interest, years):
    capital = initial_balance
    year = 0
    while year < years:
        capital += capital * (interest / 100)
        year += 1
        print(f"Year {year}: {capital:.2f}")
    return capital

def main():
    initial_balance,interest = map(float,input("Enter the values ").split())
    years = int(input("Enter the years: "))
    final = calculate_new_capital(initial_balance, interest, years)
    print(f"\nFinal after {years} years: {final:.2f}")
main()
