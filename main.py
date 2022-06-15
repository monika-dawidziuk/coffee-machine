water_avail = 400
milk_avail = 540
beans_avail = 120
cups_avail = 9
money_avail = 550


def current_state():
    statement = """\
The coffee machine has:
{water_avail} ml of water
{milk_avail} ml of milk
{beans_avail} g of coffee beans
{cups_avail} disposable cups
${money_avail} of money
""".format(water_avail=400, milk_avail=540, beans_avail=120, cups_avail=9, money_avail=550)
    print(statement)


def one_esp():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail

    one_espresso = min(water_avail // 250, beans_avail // 16, cups_avail // 1)
    if one_espresso >= 1:
        print("I have enough resources, making you a coffee!")
        esp_water = 250
        water_avail -= esp_water
        esp_beans = 16
        beans_avail -= esp_beans
        esp_cost = 4
        money_avail += esp_cost
        cup = 1
        cups_avail -= cup

    else:
        if water_avail // 250 < 1:
            print("Sorry, not enough water!")
        elif beans_avail // 16 < 1:
            print("Sorry, not enough beans!")
        elif cups_avail // 1 < 1:
            print("Sorry, not enough cups!")


def one_lat():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail

    one_latte = min(water_avail // 350, milk_avail // 75, beans_avail // 20, cups_avail // 1)
    if one_latte >= 1:
        print("I have enough resources, making you a coffee!")
        latte_water = 350
        water_avail -= latte_water
        latte_milk = 75
        milk_avail -= latte_milk
        latte_beans = 20
        beans_avail -= latte_beans
        latte_cost = 7
        money_avail += latte_cost
        cup = 1
        cups_avail -= cup
    else:
        if water_avail // 350 < 1:
            print("Sorry, not enough water!")
        elif milk_avail // 75 < 1:
            print("Sorry, not enough milk!")
        elif beans_avail // 20 < 1:
            print("Sorry, not enough beans!")
        elif cups_avail // 1 < 1:
            print("Sorry, not enough cups!")


def one_cap():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail

    one_cappuccino = min(water_avail // 200, milk_avail // 100, beans_avail // 12, cups_avail // 1)
    if one_cappuccino >= 1:
        print("I have enough resources, making you a coffee!")
        cap_water = 200
        water_avail -= cap_water
        cap_milk = 100
        milk_avail -= cap_milk
        cap_beans = 12
        beans_avail -= cap_beans
        cap_cost = 6
        money_avail += cap_cost
        cup = 1
        cups_avail -= cup
    else:
        if water_avail // 200 < 1:
            print("Sorry, not enough water!")
        elif milk_avail // 100 < 1:
            print("Sorry, not enough milk!")
        elif beans_avail // 12 < 1:
            print("Sorry, not enough beans!")
        elif cups_avail // 1 < 1:
            print("Sorry, not enough cups!")


def buy_action():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail

    c_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
    if c_type == "1":
        one_esp()
    elif c_type == "2":
        one_lat()
    elif c_type == "3":
        one_cap()
    elif c_type == "back":
        return


def take_action():
    global money_avail
    print("I gave you $" + str(money_avail))
    money_avail = 0


def fill_action():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail
    fill_w = int(input("Write how many ml of water you want to add: \n"))
    fill_m = int(input("Write how many ml of milk you want to add: \n"))
    fill_b = int(input("Write how many grams of coffee beans you want to add: \n"))
    fill_c = int(input("Write how many disposable cups you want to add: \n"))
    water_avail += fill_w
    milk_avail += fill_m
    beans_avail += fill_b
    cups_avail += fill_c


def output():
    print("The coffee machine has:")
    print(water_avail, "ml of water")
    print(milk_avail, "ml of milk")
    print(beans_avail, "g of coffee beans")
    print(cups_avail, "disposable cups")
    print("$" + str(money_avail), "of money")


def remaining_action():
    global water_avail
    global beans_avail
    global money_avail
    global cups_avail
    global milk_avail
    output()


# current_state()
def coffee_machine():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): \n")
        if action == "buy":
            buy_action()
        elif action == "take":
            take_action()
        elif action == "fill":
            fill_action()
        elif action == "remaining":
            remaining_action()
        elif action == "exit":
            break


coffee_machine()