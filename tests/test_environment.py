from teo.interpreter.environment import Environment
import pytest


def test_define():
    global_env = Environment()
    
    ret = global_env.define("a", 123)
    expected = {
        "a": 123
    }
    
    assert (
        ret == True and
        global_env.values == expected
    )


def test_define_existing_same_val():
    global_env = Environment()
    global_env.define("a", 123)
    
    ret = global_env.define("a", 123)
    
    assert ret == False


def test_define_existing_different_val():
    global_env = Environment()
    global_env.define("a", 123)
    
    ret = global_env.define("a", 321)
    
    assert ret == False


def test_assign_existing_local():
    global_env = Environment()
    global_env.define("a", 123)
    
    ret = global_env.assign("a", 321)
    expected = {
        "a": 321
    }
    
    assert (
        ret == True and
        global_env.values == expected
    )


def test_assign_existing_global():
    global_env = Environment()
    function_env = Environment(global_env)
    
    global_env.define("a", 123)
    
    ret = function_env.assign("a", 321)
    expected = {
        "a": 321
    }
    
    assert (
        ret == True and
        global_env.values == expected
    )


def test_assign_inexistent_local():
    global_env = Environment()
    
    ret = global_env.assign("a", 123)
    
    expected = {
        "a": 123
    }
    
    assert (
        ret == False and
        global_env.values == expected
    )
    

def test_assign_inexistent_global():
    global_env = Environment()
    function_env = Environment(global_env)
    
    ret = function_env.assign("a", 123)
    
    expected = {
        "a": 123
    }
    
    assert (
        ret == False and
        function_env.values == expected and
        global_env.values == {}
    )


def test_assign_recursion():
    global_env = Environment()
    function_env = Environment(global_env)
    block_env = Environment(function_env)
    
    global_env.define("a", 123)
    
    ret = block_env.assign("a", 321)
    expected = {
        "a": 321
    }
    
    assert (
        ret == True and
        global_env.values == expected
    )


def test_assign_priority():
    global_env = Environment()
    function_env = Environment(global_env)
    block_env = Environment(function_env)
    
    global_env.define("a", 1)
    function_env.define("a", 2)
    block_env.define("a", 3)
    
    ret = block_env.assign("a", 321)
    expected = {
        "a": 321
    }
    
    assert (
        ret == True and
        block_env.values == expected and
        function_env.values["a"] == 2 and
        global_env.values["a"] == 1
    )


def test_get_existing_local():
    global_env = Environment()
    
    global_env.define("a", 123)
    
    ret = global_env.get("a")
    
    assert ret == 123


def test_get_inexistent_local():
    global_env = Environment()
    
    with pytest.raises(NameError):
        global_env.get("a")


def test_get_existing_global():
    global_env = Environment()
    function_env = Environment(global_env)
    
    global_env.define("a", 123)
    
    ret = function_env.get("a")
    
    assert ret == 123


def test_get_inexistent_global():
    global_env = Environment()
    function_env = Environment(global_env)
    
    with pytest.raises(NameError):
        function_env.get("a")


def test_get_recursion():
    global_env = Environment()
    function_env = Environment(global_env)
    block_env = Environment(function_env)
    
    global_env.define("a", 123)
    
    ret = block_env.get("a")
    
    assert ret == 123


def test_get_priority():
    global_env = Environment()
    function_env = Environment(global_env)
    block_env = Environment(function_env)
    
    global_env.define("a", 1)
    function_env.define("a", 2)
    block_env.define("a", 3)
    
    ret = block_env.get("a")
    
    assert ret == 3
