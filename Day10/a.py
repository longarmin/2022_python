class Day10():
  xreg = 1
  signalsum=0

  def __init__(self):
    pass

  def parser(self, inp):
    cmds = []
    for line in inp:
      cmd=line.strip().split(" ")
      if cmd[0] == 'addx':
        cmd[1] = int(cmd[1])
      cmds.append(cmd)
    # print(cmds)
    return cmds

  def solver(self, data):
    cycle_count = 0
    for cmd in data:
      if cmd[0] == 'noop':
        cycle_count = self.check_strong_signal(cycle_count, 1)
      elif cmd[0] == 'addx':
        cycle_count = self.check_strong_signal(cycle_count, 2)
        self.xreg += cmd[1]
    return self.signalsum
  
  def check_strong_signal(self, cc, cycles):
    for _ in range(cycles):
      cc += 1
      if (cc+20)%40 < 1:
        self.signalsum += cc*self.xreg
    return cc
        
def main(inp):
  d = Day10()
  data=d.parser(inp)
  res = d.solver(data)
  print(res)

if __name__=="__main__":
    import os
    import sys
    with open("Day10/input.txt", "r", newline="\n") as inp:
        main(inp)
    
