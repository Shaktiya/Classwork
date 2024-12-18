def currency_converter():
    #according to inr
    conversion_rates={
        "USD":0.012,
        "EUR":0.0112,
        "INR":1,
        "GBP":0.0094,
        "JPY":1.80
        }
    #the amount to be converted
    amount=float(input("Enter the amount to convert: "))
    #to which currency to be converted
    to_currency=input("Enter the target currency: ").upper()
    #the conversion 
    converted_amount=amount*conversion_rates[to_currency]
    print("The amount converted is ",converted_amount)
currency_converter()
