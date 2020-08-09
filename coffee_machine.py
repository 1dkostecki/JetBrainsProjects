machine_water = 400
machine_milk = 540
machine_beans = 120
machine_cups = 9
machine_money = 550


def machine_state():
    print("The coffee machine has: ")
    print(f"{machine_water} of water")
    print(f"{machine_milk} of milk")
    print(f"{machine_beans} of coffee beans")
    print(f"{machine_cups} of disposable cups")
    print(f"{machine_money} of money")


def user_action():
    action_user = input("Write action (buy, fill, take, remaining, exit): ")
    if action_user == "buy":
        return user_buy()
    elif action_user == "fill":
        return user_fill()
    elif action_user == "take":
        return user_take()
    elif action_user == "remaining":
        return machine_state()
    elif action_user == "exit":
        return exit()


def user_fill():
    water_added = int(input("Write how many ml of water you want to add: "))
    global machine_water
    machine_water += water_added
    milk_added = int(input("Write how many ml of milk you want to add: "))
    global machine_milk
    machine_milk += milk_added
    beans_added = int(input("Write how many grams of coffee beans you want to add: "))
    global machine_beans
    machine_beans += beans_added
    cups_added = int(input("Write how many disposable cups you want to add: "))
    global machine_cups
    machine_cups += cups_added
    return user_action()


def user_buy():
    buy_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    global machine_water
    global machine_beans
    global machine_money
    global machine_milk
    global machine_cups
    if buy_input == "1" and machine_water >= 250 and machine_beans >= 16:
        print("I have enough resources, making you a coffee!")
        machine_water = machine_water - 250
        machine_beans = machine_beans - 16
        machine_money += 4
        machine_cups = machine_cups - 1
        return user_action()
    elif buy_input == "1" and machine_water < 250:
        print("Sorry, not enough water")
        return user_action()
    elif buy_input == "1" and machine_beans < 16:
        print("Sorry, not enough beans")
        return user_action()
    elif buy_input == "2" and machine_water >= 350 and machine_milk >= 75 and machine_beans >= 20:
        print("I have enough resources, making you a coffee!")
        machine_water = machine_water - 350
        machine_milk = machine_milk - 75
        machine_beans = machine_beans - 20
        machine_money += 7
        machine_cups = machine_cups - 1
        return user_action()
    elif buy_input == "2" and machine_water < 350:
        print("Sorry, not enough water")
        return user_action()
    elif buy_input == "2" and machine_milk < 75:
        print("Sorry, not enough milk")
        return user_action()
    elif buy_input == "2" and machine_beans < 20:
        print("Sorry, not enough beans")
        return user_action()
    elif buy_input == "3" and machine_water >= 200 and machine_milk >= 100 and machine_beans >= 12:
        print("I have enough resources, making you a coffee!")
        machine_water = machine_water - 200
        machine_milk = machine_milk - 100
        machine_beans = machine_beans - 12
        machine_money += 6
        machine_cups = machine_cups - 1
        return user_action()
    elif buy_input == "3" and machine_water < 200:
        print("Sorry, not enough water")
        return user_action()
    elif buy_input == "3" and machine_milk < 100:
        print("Sorry, not enough milk")
        return user_action()
    elif buy_input == "3" and machine_beans < 12:
        print("Sorry, not enough beans")
        return user_action()
    elif buy_input == "back":
        return user_action()


def user_take():
    global machine_money
    print(f"I gave you ${machine_money}")
    machine_money = machine_money - machine_money
    return user_action()


def user_exit():
    return print("Goodbye!")


while True:
    user_action()
    continue

