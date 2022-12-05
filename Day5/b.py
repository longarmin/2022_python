from collections import deque
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
class cargo:
    stacklevel = []
    stacks = []
    movements = []

    def move_crates(self, move):
        p = deque([])
        for i in range(move[0]):
            p.appendleft(self.stacks[move[1]-1].popleft())
        self.stacks[move[2]-1].extendleft(p)

    def craneOps(self):
        for m in self.movements:
            self.move_crates(m)

def main(inp):
    from collections import deque
    ca = cargo()
    for line in inp:
        if line[1] == '1':
            break
        else:
            ca.stacklevel.append(line)
    for line in inp:
        if line[0] == 'm':
            l = line.split(' ')
            mvmnt = [int(l[1]), int(l[3]), int(l[5])]
            ca.movements.append(mvmnt)
    j = 0
    for i,c in enumerate(max(ca.stacklevel)):
        if c >= 'A' and c <= 'Z' or c >='a' and c <= 'z':
            ca.stacks.append(deque([]))
            for lvl in ca.stacklevel:
                if lvl[i] != ' ':
                    ca.stacks[j].append(lvl[i])
            j+=1
    ca.craneOps()
    m = ''
    for c in ca.stacks:
        m = m +c[0]
    print(m)
if __name__=="__main__":
    import os
    import sys
    from collections import deque
    with open("Day5/input.txt", "r", newline="\n") as inp:
        main(inp)
    
