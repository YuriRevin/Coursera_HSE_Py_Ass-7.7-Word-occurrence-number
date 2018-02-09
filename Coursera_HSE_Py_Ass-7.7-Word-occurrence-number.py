inf = open('input.txt', 'r', encoding='utf8')
count = {}
for line in inf:
    words = line.strip().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
        print(count[word] - 1, end=" ")
