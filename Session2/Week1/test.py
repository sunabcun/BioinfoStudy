from collections import defaultdict

with open('test4.txt') as f:
    lines = [line.rstrip().replace(":", " ").replace("-", " ").replace(">", " ") for line in f]

startnode, endnode = int(lines[0]), int(lines[1])
my_list = list()

graph1 = defaultdict(list)

for i in range(len(lines)-2):
    for number in lines[i+2].split():
        my_list.append(int(number))
    graph1[my_list[0]].append((my_list[1], my_list[2]))
    #print(my_list[1])
    my_list.clear()
print(graph1)

#for j in range(my_list):


#for i in range(len(lines)-2):
 #   if lines[i+2][1] == ":":
  #      graph1[int(lines[i+2][0])].append((int(lines[i+2][3]), int(lines[i+2][5])))      



#for i in string.split():
 #   if i.isdigit():
  #      my_list.append(int(i))
#print (my_list)