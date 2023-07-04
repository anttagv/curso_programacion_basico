# Sentencias breack, continue y else


for i in range(5):
    for j in range(2):
        for k in range(3):
            print(f"for | ( i = {i} , j = {j} , k = {k} )")
            break
        else:
            print("for | else k")
    else:
        print("for | else j")
else:
    print("for | else i")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

i=0
j=0
k=0
while i < 5:
    while j < 2:
        while k < 3:
            print(f"while | ( i = {i} , j = {j} , k = {k} )")
            k+=1
            break
        else:
            print("while | else k")
        j+=1
    else:
        print("while | else j")
    i+=1
else:
    print("while | else i")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

for i in range(10):
    if i == 3:
        continue
    print(i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
