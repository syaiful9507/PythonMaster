import os
# print current working directory
print(f'Before CWD = {os.getcwd()}')

# change current working directory
os.chdir('/Users/syaiful/Documents/Programming')

# print current working directory
print(f'After CWD = {os.getcwd()}')