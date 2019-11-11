with open('text_5.2.txt', 'r') as file:
    i = 0
    words = 0
    for line in file:
        i += 1
        words = len(line.split())
        print(f'Lines {i} - {words} words')
    print(f'The document contains {i} lines ')