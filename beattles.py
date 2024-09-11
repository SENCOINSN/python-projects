beatles = []

beatles.append("John Lennon")

beatles.append("Paul McCartney")

beatles.append("George Harrison")

print("step 1", beatles)

for i in range(2):
    user = input("Who was a member of the beatles? ")
    beatles.append(user)


print("step 2", beatles)
# del Stu sutcliffe and Pete Best

beatles.remove("Stuart Sutcliffe")
beatles.remove("Pete Best")

print("step 3 remove Stuart and Pete ", beatles)

# inser ringo 

beatles.insert(0, "Ringo Star")


print("step 4", beatles)
