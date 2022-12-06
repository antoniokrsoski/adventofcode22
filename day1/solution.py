# Part 1
curr = 0
elves: list[int] = []

with open("input.txt") as f:
    for line in f:
        data = f.read().splitlines()
    
    for i in data:
        if i == '':
            elves.append(curr)    
            curr = 0
        else: 
            curr += int(i)

print(max(elves))

# Part 2
total = 0

for k in range(3):
    total += max(elves) 
    elves.remove(max(elves))


print(total)


