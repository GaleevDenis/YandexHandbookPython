from sys import stdin

lines = stdin.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")
len_list = int(lines[0])
listing = list(map(int, lines[1].split()))
rev_lisiting = list(reversed(listing))
maximum = 0
max_left_j = 0
max_right_l = 0
for i in range(len_list):
    left_j = listing[i]
    right_l = rev_lisiting[i]
    if right_l - left_j > maximum:
        maximum = right_l - left_j
        max_left_j = i + 1
        max_right_l = len_list - i
print(max_right_l, max_left_j)