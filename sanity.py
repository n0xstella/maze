"""
Just to keep sane regarding the creation of matrices.
"""


matrix = [
    ["a", "b", "c"],  # Row 1
    ["d", "e", "f"],  # Row 2
    ["g", "h", "i"]   # Row 3
]

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(i,row, element)
    print()


#self._cells = [
#    [Cell(), Cell(), Cell()],  # Column 0
#    [Cell(), Cell(), Cell()],  # Column 1
#    [Cell(), Cell(), Cell()]   # Column 2
#]
