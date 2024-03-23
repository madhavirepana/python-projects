#CURRENCY CONVERTER  WITHOUT USING GUI APPLICATION
#------------------------------------------   
# Import the necessary library
from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

def convert_currency(amount, from_currency, to_currency):
    # Fetch the exchange rate
    exchange_rate = c.get_rate(from_currency, to_currency)
    
    
    converted_amount = amount * exchange_rate
    
    # Return the result
    return converted_amount


amount_to_convert =int(input("Enter the amount: "))  
from_currency_code =input("From Currency: ").upper()
to_currency_code =input("To Currency: ").upper()

try:
        result = convert_currency(amount_to_convert, from_currency_code, to_currency_code)

        
        print(f"{amount_to_convert} {from_currency_code} is equal to {result:.2f} {to_currency_code}")
except:
        print('Please enter correct currency')
#WITH GUI AND API APPLICATIONS

