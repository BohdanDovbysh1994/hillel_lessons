# #Example 1
# from argparse import ArgumentParser
#
# parser = ArgumentParser(description='Our custom cli parser')
#
# parser.add_argument('--n_one', help='Number one from our cli command', default=5)
# parser.add_argument('--n_two', help='Number two from our cli command', default=10)
#
# args = parser.parse_args()
# # print(args)
# arguments = {key: float(value) for key, value in args.__dict__.items()}
#
# print(f'{arguments["n_one"]} + {arguments["n_two"]} = {arguments["n_one"] + arguments["n_two"]}')

# Example 2
# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# Example 3
from argparse import ArgumentParser

class Chrome:
    def __init__(self):
        print('Your browser is Chrome')

class FireFox:
    def __init__(self):
        print('Your browser is FireFox')
parser = ArgumentParser(description='Choose browser')
default = 'Chrome'
parser.add_argument('--browser', help='inisialized provided browser', default=default)
args = parser.parse_args()

if args.browser == 'chrome':
    driver = Chrome()
elif args.browser == 'firefox':
    driver = FireFox()
else:
    print('Get Default Chrome')
