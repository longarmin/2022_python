def main(inp):
    ElfScoreEncryption = {'A':1, 'B':2, 'C':3}
    MyScoreEncryption = {'X':1, 'Y':2, 'Z':3}
    WinMap = {'A':'Y', 'B':'Z', 'C':'X'}
    MyScore = 0
    for line in inp:
        if(WinMap[line[0]]==line[2]):
            print("Elf: " + str(line[0]) + " You: " + str(line[2]) + " You won")
            MyScore += MyScoreEncryption[line[2]] + 6
        elif(ElfScoreEncryption[line[0]] == MyScoreEncryption[line[2]]):
            MyScore += MyScoreEncryption[line[2]] + 3
        # elif (line != ''):
        else:
            MyScore += MyScoreEncryption[line[2]]

    print(MyScore)
if __name__=="__main__":
    import os
    import sys
    with open("Day2/testinput.txt", 'r', newline='\n') as inp:
        main(inp)