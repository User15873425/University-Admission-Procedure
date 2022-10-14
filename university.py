with open('applicants.txt') as file:
    for i in (applicants := [line.rsplit(' ', 8) for line in file.read().splitlines()]):
        for x in range(6, 11, 2):
            i.insert(x+1, {'Biotech': str(max(round((int(i[1]) + int(i[2])) / 2, 1), float(i[5]))),
                           'Physics': str(max(round((int(i[1]) + int(i[3])) / 2, 1), float(i[5]))),
                           'Engineering': str(max(round((int(i[3]) + int(i[4])) / 2, 1), float(i[5]))),
                           'Chemistry': str(max(float(i[2]), float(i[5]))),
                           'Mathematics': str(max(float(i[3]), float(i[5])))}[i[x]])
        del i[1:6]
quota = int(input())
distribution = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
for x in range(1, 6, 2):
    for i in sorted(applicants, key=lambda k: (-float(k[x+1]), k[0])):
        if len(distribution[i[x]]) < quota:
            distribution[i[x]].append(applicants.pop(applicants.index(i))[:x+2:x+1])
for i in distribution:
    with open(f'{i.lower()}.txt', 'w') as f:
        print(*[' '.join(j) for j in sorted(distribution[i], key=lambda k: (-float(k[1]), k[0]))], sep='\n', file=f)
