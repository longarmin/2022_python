
def find_common(lines, start, end):
    import copy
    for i in range(start, end):
        common = set()
        for c in lines[i-1]:
            if c in lines[i]:
                common.add(c)
        lines[i] = copy.deepcopy(common)
    return(common.pop())

def calc_prio(c):
    res = ord(c)-ord('a')
    if res < 0:
        res = ord(c) - ord('A') + 26 + 1
    else:
        res += 1
    return res

def main(inp):
    common = set()
    lines = []
    for cnt, line in enumerate(inp):
        lines.append(line.strip())
    prio_list = []
    for i in range(0, int(len(lines)), 3):
        a = find_common(lines, i+1, i+3)
        prio_list.append(calc_prio(a))
    print(str(sum(prio_list)))

if __name__=="__main__":
    import os
    import sys
    with open("Day3/input.txt", "r", newline="\n") as inp:
        main(inp)
    
