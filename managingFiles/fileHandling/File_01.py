try:
    f = open('message.txt')
    content = f.read()
    print(content)
finally:
    f.close()

with open('message.txt', 'r') as f:
    content = f.read()
    print(content)