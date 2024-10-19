#!/usr/bin/python3

with open("monfichier.txt","r+",encoding='utf-8') as f:
    f.write("adama seye fle")
    f.read(4)
    f.write("an other line")
    f.write("aammmdmmmd")
    f.seek(0)
    f.read()