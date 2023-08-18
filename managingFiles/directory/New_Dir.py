import os


try:
    # create new dir
    os.mkdir('file')
except:
    print('Dir "File" is Exists')

try:
    os.mkdir('../../file')
except:
    print('Dir  Exists')
# create a new directory in a specified path
try:
    os.mkdir('../../file/data_a')
except:
    print('Dir Exists')
os.chdir('../../file/data_a')
try:
    os.mkdir('test')
except:
    print('Dir Exists')
# create a file in dir file/data_a/test
os.chdir('../../file/data_a/test')
with open('test.txt', 'a') as f:
    for i in range(1, 101):
        content = f.write(f' i = {i}\n')
