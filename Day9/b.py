class rope:
  start_point = []
  d=[]
  pos_H = []
  pos_T = [[] for i in range(9)]
  visited = set()
  dbg_matrix = []
  str_mvmnt = []
  mvmnt = []
  DIR = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}

  def __init__(self):
    self.pos_H = [0,0]
    self.pos_T = [[0,0] for i in range(9)]
    self.visited = set()
    self.mvmnt = []
    self.d=[]

  def tail_move(self, pos_prev, pos_prev_old, index):
    pos_T_old = copy.deepcopy(self.pos_T[index])
    self.d = [pos_prev[0]-self.pos_T[index][0], pos_prev[1]-self.pos_T[index][1]]
    if (abs(self.d[0]) > 1 and abs(self.d[1]) > 0) or (abs(self.d[0]) > 0 and abs(self.d[1]) > 1):
      self.pos_T[index][0] += int(self.d[0]/abs(self.d[0]))
      self.pos_T[index][1] += int(self.d[1]/abs(self.d[1]))
    elif (self.d == [2,0]):
      self.pos_T[index][0] += 1
    elif (self.d == [-2,0]):
      self.pos_T[index][0] -= 1
    elif (self.d == [0,2]):
      self.pos_T[index][1] += 1
    elif (self.d == [0,-2]):
      self.pos_T[index][1] -= 1
    if index < 8:
      self.tail_move(self.pos_T[index], pos_T_old, index+1)
    else:
      self.visited.add(tuple([self.pos_T[8][0],self.pos_T[8][1]]))
    
  def proc_mvmnt(self, mvmnt, stepnum):
    import copy
    self.pos_H_old = copy.deepcopy(self.pos_H)
    self.pos_H =list(map(sum, zip(self.pos_H, mvmnt[0])))
    self.tail_move(self.pos_H, self.pos_H_old, 0)

  def plot_mat(self):
    l = ''
    for i in range(40):
      l += '.'
    self.dbg_matrix = [l for j in range(40)]
    self.dbg_matrix[self.start_point[1]] = l[:self.start_point[0]] + 's' + l[(self.start_point[0]+1):]
    self.dbg_matrix[self.pos_H[1]+20] = self.dbg_matrix[self.pos_H[1]+20][:(self.pos_H[0]+20)] + 'H' + self.dbg_matrix[self.pos_H[1]+20][(self.pos_H[0]+21):]
    for index in reversed(range(9)):
      self.dbg_matrix[self.pos_T[index][1]+20] = self.dbg_matrix[self.pos_T[index][1]+20][:(self.pos_T[index][0]+20)] + str(index+1) + self.dbg_matrix[self.pos_T[index][1]+20][(self.pos_T[index][0]+21):]
    for i,k in enumerate(reversed(self.dbg_matrix)):
      if 20-i < 10 and 20-i > -1:
        print(str(19-i) + " " + str(k))
      else:  
        print(str(19-i) + str(k))
    time.sleep(0.5)
    os.system('clear')

  def append_mvmnt(self, d, q):
    self.mvmnt.append(tuple([self.DIR[d], int(q)]))
    self.str_mvmnt.append(str(d)+str(q))

def main(inp):
  r = rope()
  r.start_point = [20,20]
  for line in inp:
    d,q = line.strip().split(" ")
    r.append_mvmnt(d, q)
  # r.plot_mat()
  for i,m in enumerate(r.mvmnt):
    for j in range(0,m[1]):
      # print(r.str_mvmnt[i])
      r.proc_mvmnt(m,j)
      # r.plot_mat()
  print(len(r.visited))
  return(len(r.visited))

if __name__=="__main__":
    import os
    import sys
    import time
    import copy
    visited = set()
    with open("Day9/input.txt", "r", newline="\n") as inp:
        main(inp)