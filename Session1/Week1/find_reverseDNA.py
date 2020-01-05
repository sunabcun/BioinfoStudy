#Read text file
file1 = open("myfile.txt","r")  
print file1.read()

trans = str.maketrans('ATGC', 'TACG')
y=file1.translate(trans)
y_reversed = y[-1::-1]
print(y_reversed)