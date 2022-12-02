#!/bin/bash
#arg1 = day number
#arg2 = session value -  Go to https://adventofcode.com/2022/day/3/input, right-click, inspect, tab over to network, click refresh, click input, click cookies, and grab the value for session.
echo 'Day'$1
DIR='Day'$1
echo $DIR
pwd_last_folder=${PWD##*/}
if [ $pwd_last_folder != "2022_python"]; then
    echo "please go to dir ''2022_python'' first."
    exit 1
fi
if [ ! -d "$DIR" ]; then 
    mkdir $DIR
fi
cd $DIR
curl https://adventofcode.com/2022/day/$1/input --cookie "session=$2" > input.txt
if [ ! -f "a.py" ]; then
    touch a.py
    STDCODE="def main(inp):
  for line in inp:
    line.strip()

if __name__==\"__main__\":
    import os
    import sys
    with open(\"$DIR/input.txt\", \"r\", newline=\"\\n\") as inp:
        main(inp)
    "
    echo "$STDCODE" > a.py
else
    echo "a.py already exists, didn't touch anything!"
fi
if [ ! -f "b.py" ]; then
    touch b.py
else
    echo "b.py already exists, didn't touch anything!"
fi
if [ ! -f "testinput.txt" ]; then
    touch testinput.txt
else
    echo "testinput.txt already exists, didn't touch anything!"
fi
