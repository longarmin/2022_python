def main(inp):

    ElfScoreEncryption = {'A':1, 'B':2, 'C':3}
    MyScoreEncryption = {'X':1, 'Y':2, 'Z':3}
    ScoreMap ={'X':0, 'Y':3, 'Z':6}
    WinMap = {'A':'Y', 'B':'Z', 'C':'X'}
    DrawMap = {'A':'X', 'B':'Y', 'C':'Z'}
    LooseMap = {'A':'Z','B':'X', 'C':'Y'}

    MyScore = 0
    for line in inp:
        if(ScoreMap[line[2]]==6):
            MyScore += MyScoreEncryption[WinMap[line[0]]] + 6
        elif(ScoreMap[line[2]]==3):
            MyScore += MyScoreEncryption[DrawMap[line[0]]] + 3
        else:
            MyScore += MyScoreEncryption[LooseMap[line[0]]]

    print(MyScore)
if __name__=="__main__":
    import os
    import sys
    with open("Day2/input.txt", 'r', newline='\n') as inp:
        main(inp)