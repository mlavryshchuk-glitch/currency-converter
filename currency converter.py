RATES = {
    "EUR": 0.025,
    "USD": 0.027,

}

print("Welcome to the Currency Converter (UAH -> EUR/USD)!")

try:
    uah_amount_str = input("Enter the amount in UAH: ")
    uah_amount = float(uah_amount_str)

    if uah_amount < 0:
        raise ValueError("The amount cannot be negative.")
        


    currency = input("Enter the target currency (EUR/USD): ").upper()


    rate = RATES[currency]
    converted_amount = uah_amount * rate

    print(f"{uah_amount} UAH is equal to {converted_amount:.2f} {currency}**.")

except ValueError as e:

    print(f"Amount input Error: please check if you entered a vaild number. Details: {e}")

except KeyError:
    print("Currency selection Error: please choose a supported currency (EUR or USD).")