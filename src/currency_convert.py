# LD 1st
# Code for converting the current money being used and displayed

# Have a default that is USD. Ryan can make a drop down for selecting the currency. Identify which currency is selected and apply a corresponding convertion expresion to base USD
# BUILD

# Currency being used: 
    # Euros -> USD_amound * 0.87
    # British Pound -> USD_amound * 0.75
    # Japanese Yen -> USD_amount * 159.60
    # Chinese Renminbi -> USD_amound * 6.91

def convert_money(selection):
    if selection == "USD":
        pass
    elif selection == "EUROS":
        pass
    elif selection == "BRITISH POUND":
        pass
    elif selection == "JAPANESE YEN":
        pass
    elif selection == "CHINESE RENMINBI":
        pass
    else:
        print("This should have not happened")