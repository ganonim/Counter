import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', required=True, type=int, help="count")
parser.add_argument('-r', '--range', default=4, type=int, help="counting range")
args = parser.parse_args()

range = args.range
count = f"{hex(args.count)[2:]:-<{range}}"
if len(count) > range:
	count = "!" * range
print("Count:", count)
