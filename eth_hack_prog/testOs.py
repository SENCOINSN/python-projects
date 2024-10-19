import os 

f = "testing_sys.py"
result = os.path.isfile("manipOS.py")
print("result ",result)

####################

print(os.getcwd())

print("\nCMD")

os.system("dir")

print("list dir ",os.listdir("C:/Users/pc/Desktop"))

for actual,dirs,files in os.walk("C:/Users/pc/Desktop/python-projects"):
    print(actual)
    print(dirs)
    print(files)
    print("\n")