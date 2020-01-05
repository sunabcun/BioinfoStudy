trans = str.maketrans('ATGC', 'TACG')
y='AAAACCCGGT'.translate(trans)
y_reversed = y[-1::-1]
print(y_reversed)