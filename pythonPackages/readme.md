Creating Packages
Now let's see how we can implement the code structure we mentioned in the previous page.

To keep things simple, we will only implement the characters package. The core concept of implementing other packages will be the same.

Creating the Game Package
To create this package,

- We will first create a directory named game. 
- Inside this folder, we will create a file named __init__.py. This is a special file that tells Python that this directory is a Python package. 
- Let's keep this __init__.py empty for now. 
- Inside the game package, we will create the characters package. Hence, we will create a directory named characters inside the game directory. 
- To tell the game directory is also a package, we will create the __init__.py file inside it. 
- Inside the game, we will create two modules player.py and boss.py. 
- Outside of the game directory, we will create a file named main.py, from where we will access our package components.

- The overall structure looks like this:

+ main.py
+ game
  + __init__.py
  + characters
    + __init__.py
    + player.py
    + boss.py

Folder structure in Python packages.

