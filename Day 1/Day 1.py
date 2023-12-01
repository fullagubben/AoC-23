import os
from pathlib import Path

SCRIPT_DIR = os.path.dirname(__file__)  
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")    

with open(INPUT_FILE, mode="rt") as f:  
    inputdata = f.read().splitlines()    




def parsing (data):
        data = list(data)
        databack = list(reversed(data))
        i = 0
        back = 0
        front = 0
        while i < len(data):
            if data[i].isnumeric() and front == 0:
                    firstvalue = data[i]
                    front = 1
            if databack[i].isnumeric() and back == 0:
                    secondvalue = databack[i]
                    back = 1
            if back == 1 & front == 1:
                output = str(firstvalue) + str(secondvalue)
                return output
                break
            i += 1
                

def wordreplacer(inputdata):
    i = 0
    wordreplace = ['one','two','three','four','five','six','seven','eight','nine']
    for char in wordreplace:
        inputdata = inputdata.replace(char, char[0] + str(wordreplace.index(char)+1) + char[-1])
    return inputdata

     
         


if __name__ == "__main__":
    p = 0
    result = []
    while p < len(inputdata):
         result.append(int(parsing(wordreplacer(inputdata[p]))))
         #print(findword(inputdata[p]))
         p = p + 1

print(sum(result))
