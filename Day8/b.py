class treehouse:
  forest = []

  def check_dir(self, x, y):
    left = 0
    right = 0
    top = 0
    buttom = 0
    for i in reversed(range(0,x)):
      left += 1
      if self.forest[y][x] <= self.forest[y][i]:
        break
    for j in range(x+1, len(self.forest[y])):
        right += 1
        if self.forest[y][x] <= self.forest[y][j]:
            break
    for k in reversed(range(0,y)):
        top += 1
        if self.forest[y][x] <= self.forest[k][x]:
            break
    for l in range(y+1,len(self.forest)):
        buttom +=1
        if self.forest[y][x] <= self.forest[l][x]:
            break
    return left * right * top * buttom
  
  def check_trees(self):
    maxView = 0
    for y in range(0,len(self.forest)-0):
      for x in range(0,len(self.forest[y])-0):
        maxView = max(self.check_dir(x,y), maxView)
    return maxView

def main(inp):
  th = treehouse()
  
  for line in inp:
    line = line.strip('\n')
    intline = [int(tree) for tree in line]
    th.forest.append(intline)
  cnt = th.check_trees()
  print(cnt)

if __name__=="__main__":
    import os
    import sys
    with open("Day8/input.txt", "r", newline="\n") as inp:
        main(inp)
    
