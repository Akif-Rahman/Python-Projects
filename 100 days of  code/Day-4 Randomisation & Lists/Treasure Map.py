
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
x = input("Where do you want to put the treasure? ")

coloumn = int(x[0])
row = int(x[1])

map[row-1][coloumn-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
