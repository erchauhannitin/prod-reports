dest = None

lines = open("waitreports\input.txt", 'r').read()
blocks = lines.split("\n\n")

if dest: dest.close()

for block in blocks:
    
    titles = block.split("\n")
    dest = open(titles[0] + '.txt', 'w')
    dest.write(block)

lines = open("cluster.txt", 'r').read()
for line in lines:
    print(line)