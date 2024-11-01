import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', required=True, type=int, help="count")
parser.add_argument('-r', '--range', default=4, type=int, help="counting range")
args = parser.parse_args()

count = args.count
count_range = args.range

def Counter(count, count_range):
	hex_cou = f"{hex(count)[2:]:-<{count_range}}"

	if len(hex_cou) > count_range:
		hex_cou = "!" * count_range
	return hex_cou

hex_cou = Counter(count, count_range)
print("Count:", hex_cou)
