class rope:
  start_point = []
  pos_H = []
  pos_T = []
  visited = set()
  dbg_matrix = []
  str_mvmnt = []
  mvmnt = []
  DIR = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}

  def __init__(self):
    self.pos_H = [0,0]
    self.pos_T = [0,0]
    self.visited = set()
    self.mvmnt = []

  def proc_mvmnt(self, mvmnt, stepnum):
    self.pos_H =list(map(sum, zip(self.pos_H, mvmnt[0])))
    d = [self.pos_H[0]-self.pos_T[0], self.pos_H[1]-self.pos_T[1]]
    if (abs(d[0]) > 1 and abs(d[1]) > 0) or (abs(d[0] > 0 and abs(d[1] > 1))):
      self.pos_T[0] += int(d[0]/abs(d[0]))
      self.pos_T[1] += int(d[1]/abs(d[1]))
    elif abs(d[0]) > 1:
      self.pos_T[0] += int(d[0]/abs(d[0]))
    elif abs(d[1]) > 1:
      self.pos_T[1] += int(d[1]/abs(d[1]))
    self.visited.add(tuple([self.pos_T[0],self.pos_T[1]]))
  def plot_mat(self):
    l = ''
    for i in range(40):
      l += '.'
    self.dbg_matrix = [l for j in range(40)]
    self.dbg_matrix[self.start_point[1]] = l[:self.start_point[0]] + 's' + l[(self.start_point[0]+1):]
    self.dbg_matrix[self.pos_T[1]+20] = self.dbg_matrix[self.pos_T[1]+20][:(self.pos_T[0]+20)] + 'T' + self.dbg_matrix[self.pos_T[1]+20][(self.pos_T[0]+21):]
    self.dbg_matrix[self.pos_H[1]+20] = self.dbg_matrix[self.pos_H[1]+20][:(self.pos_H[0]+20)] + 'H' + self.dbg_matrix[self.pos_H[1]+20][(self.pos_H[0]+21):]
    for i,k in enumerate(self.dbg_matrix):
      if i-20 < 10 and i-20 > -1:
        print(str(i-20) + " " + str(k))
      else:  
        print(str(i-20) + str(k))
    time.sleep(0.5)
    os.system('clear')

  def append_mvmnt(self, d, q):
    bla =tuple([self.DIR[d], int(q)])
    self.mvmnt.append(bla)
    self.str_mvmnt.append(str(d)+str(q))

def main(inp):
  r = rope()
  str_mvmnt = []
  r.start_point = [20,20]
  for line in inp:
    d,q = line.strip().split(" ")
    r.append_mvmnt(d, q)
  r.plot_mat()
  for i,m in enumerate(r.mvmnt):
    for j in range(0,m[1]):
      r.proc_mvmnt(m,j)
      r.plot_mat()
  print(len(r.visited))
  return(len(r.visited))

if __name__=="__main__":
    import os
    import sys
    import time
    visited = set()
    with open("Day9/testinput.txt", "r", newline="\n") as inp:
        main(inp)