#print a list of number and don't print and skip one number and continue loop
i=0
while i <= 10:
    if(i == 5):
        i += 1   #it will not print the 5 as it's matching befor.
        continue  # this will work like SKIP
    print(i)
    i += 1