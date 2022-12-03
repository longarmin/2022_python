def find_common(lines, start, end):
    for char in lines[start]:
        if char in lines[start + 1] and char in lines[start + 2]:
            return calc_prio(char)
        pass

def calc_prio(c):
    assert c >= 'A', "Character is out of Range: %s" % c
    assert c <= 'z', "Character is out of Range: %s" % c
    if c < 'a':
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

def main(inp):
    common = set()
    lines = [line.strip() for line in inp]
    prio_list = []
    for i in range(0, int(len(lines)), 3):
        prio_list.append(find_common(lines, i, i+2))
    print(str(sum(prio_list)))

if __name__=="__main__":
    import os
    import sys
    with open("Day3/input.txt", "r", newline="\n") as inp:
        main(inp)
    
