
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
x = input("Where do you want to put the treasure? ")

coloumn = int(x[0])
row = int(x[1])

selected_coloumn = map[coloumn-1]
selected_coloumn[row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
