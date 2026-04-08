# LD 1st
# Code for converting the current money being used and displayed

# Have a default that is USD. Ryan can make a drop down for selecting the currency. Identify which currency is selected and apply a corresponding convertion expresion to base USD

# Currency being used: 
    # Euros -> USD_amound * 0.87
    # British Pound -> USD_amound * 0.75
    # Japanese Yen -> USD_amount * 159.60
    # Chinese Renminbi -> USD_amound * 6.91

def convert_money(selection):
    if selection == "USD":
        symbol = "$"
        return symbol
    elif selection == "EUROS":
        symbol = "€"
        return symbol
    elif selection == "BRITISH POUND":
        symbol = "£"
        return symbol
    elif selection == "JAPANESE YEN":
        symbol = "¥"
        return symbol
    elif selection == "CHINESE RENMINBI":
        symbol = "CN¥"
        return symbol
    else:
        print("This should have not happened")