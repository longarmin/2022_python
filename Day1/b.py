def main(inp):
    highest3 = [0,0,0]
    summe = 0
    for line in inp:
        if (line != '\n'):
            # print(line)
            summe += int(line)
        else:
            highest3.append(summe)
            highest3 = sorted(highest3, reverse=True)[0:3]
            summe = 0
    highest3.append(summe)
    highest3 = sorted(highest3, reverse=True)[0:3]    
    print(str(sum(highest3)))

if __name__=="__main__":
    import os
    import sys
    with open("Day1/input.txt", 'r', newline='\n') as inp:
        main(inp)
