class treehouse:
  forest = []

  def check_dir(self, x, y):
    for i in range(0, x):
      if self.forest[y][x] <= self.forest[y][i]:
        for j in range(x+1, len(self.forest[y])):
          if self.forest[y][x] <= self.forest[y][j]:
            for k in range(0,y):
              if self.forest[y][x] <= self.forest[k][x]:
                for l in range(y+1,len(self.forest)):
                    if self.forest[y][x] <= self.forest[l][x]:
                      return 0
                    else:
                      pass
    return 1
  
  def check_trees(self):
    cnt = 0
    for y in range(0,len(self.forest)-0):
      for x in range(0,len(self.forest[y])-0):
        cnt += self.check_dir(x,y)
    return cnt

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
    
