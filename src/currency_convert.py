def convert_money(amount_usd, selection):
    if selection == "USD":
        symbol = "$"
        converted_amount = amount_usd
    elif selection == "EUROS":
        symbol = "€"
        converted_amount = amount_usd * 0.87
    elif selection == "BRITISH POUND":
        symbol = "£"
        converted_amount = amount_usd * 0.75
    elif selection == "JAPANESE YEN":
        symbol = "¥"
        converted_amount = amount_usd * 159.60
    elif selection == "CHINESE RENMINBI":
        symbol = "CN¥"
        converted_amount = amount_usd * 6.91
    else:
        print("This should not have happened")
        symbol = ""
        converted_amount = amount_usd
    return symbol, converted_amount