
EXCHANGE_RATE = .15 #One yuan is equal to .15 USD
DOMESTIC_SHIPPING = 20
is_running = True

def Main():
    print()
    print()
    print("*"*15)
    print()

    print("1 Calculate price")
    print("2 Calculate price (Boostmaster)")
    print("3 Quit program")
    print("4 Adjust settings for this run")
    print ()
    print("*"*15)
    print()
    print()

    cmd = input("Choice? ")
    print()

    if (cmd == "1"):
        #Calculate value
        calculate_price()
    elif(cmd == "2"):
        calculate_boostmaster_price()
    elif (cmd == "3"):
        #Change settings
        change_settings()
    else:
        is_running = False

def calculate_price():
    try:
        yuan = float(input("Price in yuan: "))
    except Error as e:
        print (e)
        return

    base_price = yuan_to_usd(yuan)
    print(base_price)
    input("[Press enter to return]")
    return base_price

def calculate_boostmaster_price():
    try:
        yuan = float(input("Price in yuan: "))
    except Error as e:
        print (e)
        return

    yuan = yuan * 1.1
    yuan = yuan + DOMESTIC_SHIPPING

    usd_value = yuan_to_usd(yuan)
    print("$" + str(usd_value))
    input("[Press enter to return]")
    return



def yuan_to_usd(yuan):
    return yuan * EXCHANGE_RATE

def change_settings():
    global EXCHANGE_RATE
    global DOMESTIC_SHIPPING
    EXCHANGE_RATE = float(input("New exchange rate? (Yuan to USD) "))
    DOMESTIC_SHIPPING = float(input("New shipping rate? (In Yuan) "))
    return

if (__name__ == "__main__"):
    while (is_running == True):
        Main()
