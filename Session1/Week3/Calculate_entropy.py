import math

def Calculate_Entropy(Motifs):
    A_num = list()
    C_num = list()
    G_num = list()
    T_num = list()
    
    for i in range(len(Motifs[0])):
        A_num.append(0)
        C_num.append(0)
        G_num.append(0)
        T_num.append(0)

    
    for Motif in Motifs:
        for i in range(len(Motif)):
            if Motif[i] == 'T':
                T_num[i]+=1
            elif Motif[i] == 'A':
                A_num[i]+=1
            elif Motif[i] == 'G':
                G_num[i]+=1
            elif Motif[i] == 'C':
                C_num[i]+=1    
       
    T_num[:] = [x / 10 for x in T_num]
    A_num[:] = [x / 10 for x in A_num]
    G_num[:] = [x / 10 for x in G_num]
    C_num[:] = [x / 10 for x in C_num]
   
   
    equation_T = sum([p * math.log(p, 2) for p in T_num if p > 0])
    equation_A = sum([p * math.log(p, 2) for p in A_num if p > 0])
    equation_G = sum([p * math.log(p, 2) for p in G_num if p > 0])
    equation_C = sum([p * math.log(p, 2) for p in C_num if p > 0])
    
    SUM = equation_T + equation_A + equation_G + equation_C
    print (-SUM)

            
            
    
Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
Calculate_Entropy(Motifs)
#[1,1,1,0]