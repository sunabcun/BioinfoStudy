from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
        return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    topidx = -1
    idx = 0
    openidx = []
    for i, next in enumerate(text):
        #print("topidx: ", topidx)
        #print("i: ", i, "next: ", next)
        if next in "([{":
            opening_brackets_stack.append(next)
            topidx += 1
            top = opening_brackets_stack[topidx]
            openidx.append(i+1)
        
        if next in ")]}":
            
            if len(opening_brackets_stack) != 0:
                
                if are_matching(top, next) == False:
                  #  print("YA1")
                    return False, i+1
                else:
                    del opening_brackets_stack[topidx]
                    del openidx[topidx]
                    topidx -= 1
                    
                    if len(opening_brackets_stack) != 0 and topidx >= 0:
                        top = opening_brackets_stack[topidx]
                        
                  #  print(i, len(text)-1)
                        if len(opening_brackets_stack) != 0 and i == len(text)-1:
                              #print("YA2", openidx)
                              return False, openidx[0]
                   # elif len(opening_brackets_stack) == 0 and topidx < 0 :
                    #    print("this is next:" , next)
                     #   return True, i
                 
            else:
                #print("YA3")
                return False, i+1
        
       # print(opening_brackets_stack, idx)
       # print(openidx)
        
        if i < len(text)-1:
         #   print("here")
            pass
        elif len(opening_brackets_stack) != 0 and i == len(text)-1:
        #    print("YA4")
            return False, i+1
        else:
            return True, 0
                     
            

def main():
    text = input()
    mismatch, i = find_mismatch(text)
    if mismatch != False:
        print("Success")
    else:
        print(i)
     

if __name__ == "__main__":
    main()
