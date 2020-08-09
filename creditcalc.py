import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=float, help="principal")
parser.add_argument("--interest", type=float, help="interest")
parser.add_argument("--periods", type=int, help="periods")
parser.add_argument("--payment", type=float, help="payment")
parser.add_argument("--type", type=str, help="type")
args = parser.parse_args()

if len(sys.argv) == 4:
    pass
if args.interest is None:
    print('Incorrect parameters')
elif args.type == "annuity":
    if (args.payment is not None) and (args.periods is not None) and (args.interest is not None):
        payment = args.payment
        periods = args.periods
        interest = args.interest
        nominal_interest = (interest / 100) / 12
        credit_principal = payment / ((nominal_interest * ((1 + nominal_interest) ** periods)) / (((1 + nominal_interest) ** periods) - 1))
        print("Your credit principal =", str(credit_principal) + "!")
        print("Overpayment =", (payment * periods) - credit_principal)
    elif (args.principal is not None) and (args.payment is not None) and (args.interest is not None):
        nominal_interest = args.interest / (12 * 100)
        period_per_month = math.log((args.payment / (args.payment - nominal_interest * args.principal)), (1 + nominal_interest))
        period_per_month = math.ceil(period_per_month)
        Overpayment = int(args.payment * period_per_month - args.principal)
        numbers_years = period_per_month // 12
        number_month = math.floor(((period_per_month / 12) - numbers_years) * 12)
        if numbers_years > 1 and number_month > 1:
            print("You need {0} years and {1} months to repay this credit!".format(numbers_years, number_month))
        elif numbers_years == 1 and number_month == 1:
            print("You need {0} year and {1} month to repay this credit!".format(numbers_years, number_month))
        elif numbers_years == 0 and number_month > 1:
            print("You need {0} months to repay this credit!".format(number_month))
        elif numbers_years == 0 and number_month == 1:
            print("You need {0} month to repay this credit!".format(number_month))
        elif number_month == 0 and numbers_years > 1:
            print("You need {0} years to repay this credit!".format(numbers_years))
            print("Overpayment = {0}".format(Overpayment))
        elif number_month == 0 and numbers_years == 1:
            print("You need {0} year to repay this credit!".format(numbers_years))
            print("Overpayment = {0}".format(Overpayment))
    elif (args.principal is not None) and (args.periods is not None) and (args.interest is not None):
        principal = args.principal
        periods = args.periods
        interest = args.interest
        nominal_interest = (interest / 100) / 12
        annuity = principal * ((nominal_interest * ((1 + nominal_interest) ** periods)) / (((1 + nominal_interest) ** periods) - 1))
        new_annuity = math.ceil(annuity)
        print(f"Your annuity payment = {(new_annuity * periods) - principal}!")
        print(f"Overpayment = {new_annuity}")
    else:
        print("Incorrect parameters.")
elif args.type == "diff":
    if (args.principal == None) or (args.periods == None) or (args.interest == None):
        print("Incorrect parameters")
    else:
        nominal_interest = args.interest / (12 * 100)
        differentiated_payments = []
        for n_periods in range(1, args.periods + 1):
            d = math.ceil(
                (args.principal / args.periods) + nominal_interest * (args.principal - args.principal * (n_periods - 1) / args.periods))
            differentiated_payments.append(d)
            print("Month {0}: paid out {1}".format(n_periods , d))
        Overpayment = int(sum(differentiated_payments) - args.principal)
        print()
        print("Overpayment = {0}".format(Overpayment))
else:
    print("Incorrect parameters.")
