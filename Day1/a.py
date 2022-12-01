def main(inp):
    max_summe = 0
    summe = 0
    for line in inp:
        if (line != '\n'):
            # print(line)
            summe += int(line)
        else:
            max_summe = max(summe, max_summe)
            summe = 0
    max_summe = max(summe, max_summe)    
    print(str(max_summe))

if __name__=="__main__":
    import os
    import sys
    with open("Day1/input.txt", 'r', newline='\n') as inp:
        main(inp)
