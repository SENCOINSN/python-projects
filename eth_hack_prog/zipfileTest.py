#!/usr/bin/python3

from zipfile import ZipFile

# list_file = ["file1.txt","file2.txt","file3.txt","test"]

# with ZipFile("myzip.zip","w") as z:
#     for f in list_file:
#         z.write(f)

with ZipFile("myzip.zip","r") as z:
    #z.printdir()
    z.extract("file2.txt")
    print(z.read('file1.txt'))
    #z.extractall()
    print(z.infolist())