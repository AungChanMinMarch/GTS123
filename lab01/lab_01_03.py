# Lab01_03 - Exercise 2
print("1")
print("2 3")
print("4 5 6")
print("6 7 9 10")

print("using loop")
no_of_stair = 10;
current_num = 1;
for i in range(no_of_stair):
	for j in range(i+1):
		print(current_num, end=" ");
		current_num += 1
	print()