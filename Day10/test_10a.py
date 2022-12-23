import pytest
import copy
from a import Day10

test_expoutput = [['noop'],['addx', 3],['addx', -5]]


@pytest.fixture
def day():
    return Day10()

def test_append_movement(day):
    pass
    # assert r.mvmnt[-1] == (mvmntDirVals[i],val)

@pytest.mark.parametrize("expected", [test_expoutput])
def test_parser(day,expected):
    with open("Day10/testinput.txt", "r", newline="\n") as inp:
        bla=day.parser(inp)
    assert(bla == expected)

@pytest.mark.parametrize("expected", [13140])
def test_solver(day, expected):
    day.__init__()
    with open("Day10/testinput2.txt", "r", newline="\n") as inp:
        bla=day.parser(inp)
    assert(day.solver(bla) == expected)
