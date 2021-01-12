# DANGER : run at your RISK ...  !!!
# Source : internet 2019
# job : creates multiple folders with specific names pattern
# ver v1

from pathlib import Path
from os import rename
import os


print(os.getcwd())

for i in range(20):
    f = "1"
    j = i+1
    if j<10:
        f = f+"0"
    fnme = f+str(j)
    print (fnme)
    try:
        os.mkdir(fnme)
    except OSError as e:
        print ("folder exists")
        continue

