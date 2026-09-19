from teo.main import run
from teo.errors.parser import TeoParserError
import pytest


def test_1(capsys):
    source = """
    a = 5
    b = 10

    console_log a
    console_log b
    console_log a + b

    var c = a * b
    console_log c

    c = c + 2
    console_log c
    """
    
    run(source)
    
    output = capsys.readouterr()
    
    assert output.out == "5\n10\n15\n50\n52\n"


def test_2(capsys):
    source = """
    a = 5
    b = 10

    console_log a
    console_log b

    console_log a + b
    console_log a * 2
    console_log -a

    c = a + b * 2
    console_log c
    """
    
    run(source)
    
    output = capsys.readouterr()
    
    assert output.out == "5\n10\n15\n10\n-5\n25\n"


def test_3():
    source = """
    a = 
    """
    
    with pytest.raises(TeoParserError):
        run(source)


def test_4():
    source = """
    a = 4 b = 1
    """
    
    with pytest.raises(TeoParserError):
        run(source)
