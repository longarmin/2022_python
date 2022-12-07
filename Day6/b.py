def check_included(arr):
  s = set()
  for ar in arr:
    s.add(ar)
  return(len(s) == 14)

def main(inp):
  for line in inp:
    for i in range(14, len(line)):
        if check_included(line[i-14:i]):
          break
    print(i)
    
if __name__=="__main__":
    import os
    import sys
    with open("Day6/input.txt", "r", newline="\n") as inp:
        main(inp)
    
