import argparse
from random import randrange

parser = argparse.ArgumentParser(prog='Counter', description='Converts numbers to hex and outputs them in a specific range', epilog='Text at the bottom of help')
parser.add_argument('-c', '--count', required=True,type=int, help='decima counter (if number = -1, generated random number)')
parser.add_argument('-r', '--range', default=4,type=int, help="counting range (default: 4)")
args = parser.parse_args()

count_number = args.count
count_range = args.range

def Counter(count_number, count_range):
	if count_number == -1:
		count_number = randrange(16**count_range)
	hex_count = f"{hex(count_number)[2:]:-<{count_range}}"

	if len(hex_count) > count_range:
		hex_count = "!" * count_range
	return hex_count

hex_count = Counter(count_number, count_range)
print("Count:", hex_count)
