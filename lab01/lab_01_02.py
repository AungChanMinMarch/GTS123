# Lab01_02
print("XX X X X X X X X XX")
print("XX O X O X O X O XX")
print("XX X O X O X O X XX")
print("XX O X O X O X O XX")
print("XX X X X X X X X XX")

print("using loop")
row = 3
col = 7
def alternate(first_X_or_O, sec_X_or_O):
	my_arr = [first_X_or_O] * col;
	for i in range(col):
		if i % 2 == 1:
			my_arr[i] = sec_X_or_O;
	return " ".join(my_arr) + " "


# first row & last row
def drawRow(content):
	print("XX", end=" ")
	print(content, end="")
	print("XX")
drawRow("X " * col)
for i in range(row):
	if(i%2 == 0):
		drawRow(alternate("O", "X"))
	else:
		drawRow(alternate("X", "O"))
drawRow("X " * col)
# for row in range(5):
#     # Print the left border
#     print("XX", end="")
    
#     # Loop through the 7 middle columns (indices 0 to 6)
#     for col in range(7):
#         # Determine the character to print
#         if row == 0 or row == 4:
#             # Top and bottom rows are always 'X'
#             char = "X"
#         elif (row + col) % 2 != 0:
#             # If row + col is odd, print 'O' (Checkerboard logic)
#             char = "O"
#         else:
#             # Otherwise print 'X'
#             char = "X"
            
#         # Print the character with a leading space
#         print(" " + char, end="")

#     # Print the right border and move to the next line
#     print(" XX")