#list of number found x in this tuple using loop nad BREAK the loop if found
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100,20,467,27,36,90,73)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,20,467,27,36,90,73)

x = 36  #serching numner

i = 0
while i < len(nums):  #statement i less then 0 as index start with zero
    if(nums[i] == x):   #condition nums i value = to x value
        print("We FOUND X valie",x, "in index :", i)
        break  #Here we used BREAK to stop the loop if we found result
    else:
        print("Finding....")
    i += 1  #incriseing with +1

print("End of Loop")