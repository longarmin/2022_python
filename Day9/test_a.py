import pytest
from a import rope

tstlist = [[[('D',4),('U',2),('L',2)], 5],
    [[('R',4),('U',4),('L',3),('D',1),('R',4),('D',1),('L',5),('R',2)], 13],
    [[('U',3),('D',3),('R',3),('L',3),('D',3),('U',3),('L',3),('R',3)], 9],
    [[('U',3),('D',3),('R',3),('L',3),('D',3),('U',3),('L',3),('R',2),('U',2)], 10],
    [[('U',23),('D',24),('R',3),('L',3),('D',3),('U',3),('L',3),('R',3)], 30]]

@pytest.fixture
def r():
    return rope()

@pytest.mark.parametrize("test_inp,expected", [(k[0],k[1]) for k in tstlist])
def test_if_all_tail_movements_are_counted(r, test_inp, expected):
    r.__init__()
    for d in test_inp:  
        r.append_mvmnt(d[0], d[1])
    for i,m in enumerate(r.mvmnt):
        for j in range(0,m[1]):
            r.proc_mvmnt(m,i)
    count = len(r.visited)
    print("count: " + str(count) + " expected: " + str(expected))
    assert (count == expected)

def test_append_movement(r):
    mvmntDirs =     ['L','R','U','D']
    mvmntDirVals =  [[-1,0], [1,0], [0,1], [0,-1]]
    for i,a in enumerate(mvmntDirs):
        for val in range(0,25):
            r.append_mvmnt(a, val)
            assert r.mvmnt[-1] == (mvmntDirVals[i],val)