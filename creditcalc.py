import math
import argparse


# Calculates loan principal
def loan_principal(annuity_payment, month_c, loan_inter):
    loan_inter /= 1200
    loan_principal_1 = (loan_inter * math.pow((1 + loan_inter), month_c))
    loan_principal_2 = (math.pow((1 + loan_inter), month_c) - 1)
    loan_prin = math.ceil((annuity_payment * loan_principal_2) / loan_principal_1)
    print(f'Your loan principal = {loan_prin}!')
    print('\nOverpayment =', overpayment(loan_prin, annuity_payment * month_c))


# Calculates annuity monthly payment amount
def annuity_pay(loan_prin, month_c, loan_inter):
    loan_inter /= 1200
    annuity_payment_1 = loan_inter * math.pow(1 + loan_inter, month_c)
    annuity_payment_2 = pow(1 + loan_inter, month_c) - 1
    annuity_payment = math.ceil(loan_prin * annuity_payment_1 / annuity_payment_2)
    print(f'Your monthly payment = {annuity_payment}!')
    print('\nOverpayment =', overpayment(loan_prin, annuity_payment * month_c))


# Calculates number of monthly payments
def number_payments(loan_prin, annuity_payment, loan_inter):
    loan_inter /= 1200
    number_payments_1 = annuity_payment / (annuity_payment - loan_inter * loan_prin)
    number_pay = math.ceil(math.log(number_payments_1, loan_inter + 1))
    years = number_pay // 12
    months = number_pay % 12
    print('It will take', end=" ")
    if years > 0:
        print(f'{years} year{"s" if years > 1 else ""}', end=" ")
    if years and months:
        print(f'{"and"}', end=" ")
    if months > 0:
        print(f'{months} month{"s" if months > 1 else ""}', end=" ")
    print('to repay this loan!')
    print('\nOverpayment =', overpayment(loan_prin, annuity_payment * number_pay))


# Calculates different payment for 'm' month
def diff_pay(loan_prin, month_c, loan_inter, m):
    loan_inter /= 1200
    diff_payment = loan_prin / month_c + loan_inter * (loan_prin - (loan_prin * (m - 1)) / month_c)
    return math.ceil(diff_payment)


# Calculates different payment for every month
def diff_pay_all(loan_prin, month_c, loan_inter):
    diff_list = []
    for i in range(1, month_c + 1):
        diff = diff_pay(loan_prin, month_c, loan_inter, i)
        diff_list.append(diff)
        print(f'Month {i}: payment is {diff}')
    print('\nOverpayment =', overpayment(loan_prin, sum(diff_list)))


# Calculates overpayment
def overpayment(first, second):
    return int(second - first)


parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()
elements = [args.type, args.principal, args.periods, args.interest, args.payment]
alist = []
for i in elements:
    if i:
        alist.append(i)

if len(alist) != 4 or alist[0] not in ('diff', 'annuity') or min(alist[1:]) < 0 or not args.interest or (args.type == 'diff' and args.payment):
    print("Incorrect parameters")
elif args.type == 'diff' and not args.payment:
    diff_pay_all(args.principal, args.periods, args.interest)
else:
    if not args.principal:
        loan_principal(args.payment, args.periods, args.interest)
    elif not args.periods:
        number_payments(args.principal, args.payment, args.interest)
    else:
        annuity_pay(args.principal, args.periods, args.interest)
