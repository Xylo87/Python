import sys
import argparse

# import functions
# from lib import functions
from lib.functions import bark

print('Hello')

bark()



# > Running program with arguments
print(sys.argv)

parser = argparse.ArgumentParser(
    description = 'Test'
)

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow'}, help='the color to search for')

args = parser.parse_args()
print(args.color)