# This code attempts to solve Project Euler Problem 2.

F1 = 2
F2 = 1
answer = 2

while F1 <= 4000000:
	F1 = F1 + F2
	F2 = F1 - F2
	if F1%2 == 0:
		answer+= F1
print(answer)

