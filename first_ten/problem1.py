# This code attempts to solve ProjectEuler.net Problem 1.
# Wednesday November 5th, 2014

sum = 0

for x in range(1,1000):
    if (x%3 == 0 or x%5 == 0):
        sum+= x
print(sum)
