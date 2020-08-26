# Write your code here
import random
import math
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS card')
cur.execute('CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()
card_list = []
login_card_list = []
login_card_input = ''
login_pin_input = ''


def start_menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_num = int(input())
    if user_num == 1:
        return create_account()
    elif user_num == 2:
        return login_check()
    elif user_num == 0:
        return exit_menu()
    else:
        print("Please select a valid option.")
        return start_menu()


def create_account():
    global card_list
    generated_pin = random.randint(1000, 10000)
    generated_card_suffix = str(random.randint(1000000000, 9999999999))
    generated_card = int('400000' + generated_card_suffix)
    test_card = generated_card // 10
    test_list = [int(x) for x in str(test_card)]
    test_list[::2] = [i * 2 for i in test_list[::2]]
    for n in range(0, len(test_list)):
        if test_list[n] > 9:
            test_list[n] += -9
    control_number = sum(test_list)
    if control_number % 10 == 0:
        test_card *= 10
        print("Your card has been created")
        print("Your card number: ")
        print(test_card)
        print("Your card PIN: ")
        print(generated_pin)
        card_list.append(str(test_card))
        card_list.append(str(generated_pin))
        cur.execute('INSERT INTO card (number, pin, balance) VALUES (?, ?, ?);', (str(test_card), str(generated_pin), 0))
        conn.commit()
        return start_menu()
    elif control_number % 10 != 0:
        control_number_test = control_number / 10
        checksum_digit_tens = math.ceil(control_number_test) * 10
        checksum_digit = checksum_digit_tens - control_number
        final_card = str(test_card) + str(checksum_digit)
        print("Your card has been created")
        print("Your card number: ")
        print(final_card)
        print("Your card PIN: ")
        print(generated_pin)
        card_list.append(str(final_card))
        card_list.append(str(generated_pin))
        cur.execute('INSERT INTO card (number, pin, balance) VALUES (?, ?, ?);', (str(final_card), str(generated_pin), 0))
        conn.commit()
        return start_menu()


def exit_menu():
    return print("Bye!")


def login_check():
    global login_card_input
    global login_pin_input
    global card_list
    global login_card_list
    print("Enter your card number: ")
    login_card_input = input()
    print("Enter your PIN: ")
    login_pin_input = input()
    if login_card_input in card_list and login_pin_input in card_list:
        login_card_list.append(str(login_card_input))
        login_card_list.append(str(login_pin_input))
        print("You have successfully logged in!")
        return log_into_account()
    else:
        print("Wrong card number or PIN!")
        return start_menu()


def log_into_account():
    global login_card_list
    global login_card_input
    global login_pin_input
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
    user_num = int(input())
    if user_num == 1:
        current_balance = cur.execute('SELECT balance FROM card WHERE number = ?', login_card_input)
        conn.commit()
        print(f"Balance: {current_balance}")
    elif user_num == 2:
        print("Enter income: ")
        income_added = int(input())
        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (income_added, login_card_input))
        conn.commit()
        print("Income was added!")
        return log_into_account()
    elif user_num == 3:
        return do_transfer()
    elif user_num == 4:
        return close_account()
    elif user_num == 5:
        login_card_input = ''
        login_pin_input = ''
        print("You have successfully logged out!")
        return start_menu()
    elif user_num == 0:
        return exit_menu()


def do_transfer():
    print("Transfer")
    print("Enter card number:")
    transfer_card = input()
    existing_cards = cur.execute('SELECT number FROM card;').fetchall()
    conn.commit()
    if transfer_card == login_card_input:
        print("You can't transfer money to the same account!")
        return log_into_account()
    elif transfer_card[0] != '4':
        print("Such a card does not exist.")
        return log_into_account()
    elif luhn_check(int(transfer_card)) is False:
        print("Probably you made mistake in the card number. Please try again!")
        return log_into_account()
    elif luhn_check(int(transfer_card)) is True:
        existing_cards = cur.execute('SELECT number FROM card;').fetchall()
        conn.commit()
        if (transfer_card,) not in existing_cards:
            print("Such a card does not exist.")
            return log_into_account()
        else:
            print("Enter how much money you want to transfer: ")
            transfer_amount = input()
            money_available = cur.execute('SELECT balance FROM card WHERE number = ?;', (login_card_input,)).fetchone()
            money_available = ''.join(map(str, money_available))
            if int(transfer_amount) > int(money_available):
                print("Not enough money!")
                return log_into_account()
            else:
                cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (transfer_amount, transfer_card))
                cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?;', (transfer_amount, login_card_input))
                conn.commit()
                print("Transfer successful!")
                return log_into_account()


def close_account():
    cur.execute('DELETE FROM card WHERE number = ? AND pin = ?;', (login_card_input, login_pin_input))
    conn.commit()
    print("This account has been closed!")
    return start_menu()


def luhn_check(card_to_check):
    test_card = card_to_check // 10
    test_list = [int(x) for x in str(test_card)]
    test_list[::2] = [i * 2 for i in test_list[::2]]
    for n in range(0, len(test_list)):
        if test_list[n] > 9:
            test_list[n] += -9
    control_number = sum(test_list)
    if control_number % 10 == 0:
        test_card *= 10
        return True
    else:
        control_number_test = control_number / 10
        checksum_digit_tens = math.ceil(control_number_test) * 10
        checksum_digit = checksum_digit_tens - control_number
        final_card = str(test_card) + str(checksum_digit)
        final_card = int(final_card)
        if final_card != card_to_check:
            return False
        elif final_card == card_to_check:
            return True


start_menu()
