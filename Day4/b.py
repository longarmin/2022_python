def count_partially_covered_ranges(inp_list):
  cnt = 0
  for s in inp_list:
    a = 0
    b = 0
    for i in range(s[0][0],s[0][1]+1):
      a = a|(1 << i) 
    for i in range(s[1][0],s[1][1]+1):
      b = b|(1 << i) 
    if (a&b):
      cnt +=1
  return cnt

def main(inp):
  inp_list = []
  for line in inp:
    a = line.strip().split(',')
    a[0]=tuple(map(int, a[0].split('-')))
    a[1]=tuple(map(int, a[1].split('-')))
    inp_list.append(a)
  print(count_partially_covered_ranges(inp_list))

if __name__=="__main__":
  import os
  import sys
  with open("Day4/input.txt", "r", newline="\n") as inp:
    main(inp)
    