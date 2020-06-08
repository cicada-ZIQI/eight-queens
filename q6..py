import random
output=[]

def row(row_name,row_number):
    global column,output
    #produce a row
    name=["| "]*8 + ["|Q"]
    step=0
    while True:                                                      
        random.shuffle(name)
        diagonal=[]
        #"|Q" can't be the last object of the list
        if name.index("|Q") != 8:
            #row1 can be in any order
            if row_name == "row1":
                output += ["\n"] + name
                column.append(name.index("|Q"))
                break
            # the following discusses the rows except row1
            if name.index("|Q") not in column:
                for i in column:
                    #use the following formula to make sure the place of "Q" isn't in any diagnoses 
                    place1=i-(row_number-1-column.index(i))
                    place2=i+(row_number-1-column.index(i))
                    diagonal.append(place1)
                    diagonal.append(place2)
                step+=1
                #if the number of step is too large, that means this randomly produced 8-queen chessboard isn't solvable
                if step==20:
                    return True
                if name.index("|Q") not in diagonal:
                    output += ["\n"] + name
                    column.append(name.index("|Q"))
                    return False
                else:
                    continue
            else:
                continue
        else:
            continue
while True:
    column=[]
    output=[]
    row("row1",1)
    row("row2",2)
    row("row3",3)
    #when the chessboard isn't solvable, the function: row(rowx,x) will return True,thus the program will restart from row1
    if row("row4",4):
        continue
     
    if row("row5",5):
        continue
     
    if row("row6",6):
        continue
     
    if row("row7",7):
        continue
     
    if row("row8",8):
        continue
    else:
        print(*output)
        break

    

 

