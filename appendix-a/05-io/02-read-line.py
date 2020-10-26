import sys

# input string
data = sys.stdin.readline().rstrip()
print(data)

data = list(map(str, sys.stdin.readline().rstrip().split()))
print(data)
