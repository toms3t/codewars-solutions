import random

suits = ['S', 'D', 'C', 'H']
nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

l = []
d = []
for i in range(15):
    l = []
    for i in range(5):
        r = random.choice(nums) + random.choice(suits)
        if r not in l:
            l.append(r)
        else:
            r = random.choice(nums) + random.choice(suits)
            l.append(r)
    d.append(l)

print(d)

for x in d:
    print(len(x))

for x in d:
    e = ' '.join(x)
    print(e)
