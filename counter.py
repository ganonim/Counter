import argparse
from random import randrange

parser = argparse.ArgumentParser(prog='Counter', description='Converts numbers to hex and outputs them in a specific range', epilog='Text at the bottom of help')
parser.add_argument('-c', '--count', required=True,type=int, help='decima counter (if number = -1, generated random number)')
parser.add_argument('-r', '--range', default=4,type=int, help="counting range (default: 4)")
args = parser.parse_args()

count = args.count
count_range = args.range

def Counter(count, count_range):
	if count == -1:
		count = randrange(16**count_range)
	hex_cou = f"{hex(count)[2:]:-<{count_range}}"

	if len(hex_cou) > count_range:
		hex_cou = "!" * count_range
	return hex_cou

hex_cou = Counter(count, count_range)
print("Count:", hex_cou)
