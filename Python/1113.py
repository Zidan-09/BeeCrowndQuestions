import sys

for line in sys.stdin:
    line = line.strip()

    n1, n2 = map(int, line.split())

    print(f'crescente') if n1 < n2 else print('decrescente')