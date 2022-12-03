def main(inp):
  common = []
  for i, line in enumerate(inp):
    rucksack = line.strip()
    length = len(rucksack)/2
    comp1 = rucksack[0:int(length)]
    comp2 = rucksack[int(length):]
    for c in comp1:
      if c in comp2:
        common.append(c)
        break
    prio = []
  for c in common:
    if c < 'a':
      res = ord(c) - ord('A') + 27
    else:
      res = ord(c) - ord('a') + 1
    prio.append(res)
  print(sum(prio))

if __name__=="__main__":
    import os
    import sys
    with open("Day3/input.txt", "r", newline="\n") as inp:
        main(inp)
    
