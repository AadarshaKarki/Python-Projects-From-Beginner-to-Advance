from currency_converter import CurrencyConverter

c = CurrencyConverter()

print("=== Simple Currency Converter ===\n")


amount = float(input("Enter the amount you want to convert: "))


from_currency = input("Convert FROM which currency? (e.g., USD, EUR, INR): ").upper()
to_currency   = input("Convert TO which currency? (e.g., USD, EUR, INR): ").upper()


try:
    result = c.convert(amount, from_currency, to_currency)
    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")
except ValueError:
    print("Oops! One of the currency codes seems incorrect. Please check and try again.")