import os
from pathlib import Path

SCRIPT_DIR = os.path.dirname(__file__)  
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")    

with open(INPUT_FILE, mode="rt") as f:  
    inputdata = f.read().splitlines()  
gamenr = 1

sumlist = []

       
class game:
  def __init__(self, blue, red, green):
    self.blue = blue
    self.red = red
    self.green = green

games = [game(0,0,0) for _ in range(len(inputdata))] 

def parsing (data):
    data = data.split(':')
    #print(data)
    gamenr = int(data[0].split()[1])-1
    data = data[1:]
    for d in data:
        data[data.index(d)] = d.split(';')
    classadd(data,gamenr)

def classadd(game,gamenr):
    for g in game[0]:
        g = g.split(',')
        for cubes in g:
            cubes = cubes.split()
            if cubes[1] == 'red' and int(cubes[0]) > games[gamenr].red:
                games[gamenr].red = int(cubes[0]) 
            if cubes[1] == 'green' and int(cubes[0]) > games[gamenr].green:
                games[gamenr].green = int(cubes[0]) 
            if cubes[1] == 'blue' and int(cubes[0]) > games[gamenr].blue:
                games[gamenr].blue = int(cubes[0])                 
        
def comparemachine(gamenr):
    return games[gamenr].red*games[gamenr].green*games[gamenr].blue

if __name__ == "__main__":
    games = list()
    for i in range(len(inputdata)):
        games.append(game(0,0,0))

    result = []
    for data in inputdata:
        parsing(data)

    for game in games:
        sumlist.append(comparemachine(games.index(game)))

print(sum(sumlist))






