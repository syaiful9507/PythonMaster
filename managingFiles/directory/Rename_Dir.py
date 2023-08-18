import os

# rename the directory
try:
    os.rename('file', 'renameDir')
except FileNotFoundError:
    print('File Not Found')

