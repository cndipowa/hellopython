from hellopython import say_hello

def test_hellopython_no_params():
    assert say_hello() == "Hello, World!"
    
def test_hellopython_with_params():
    assert say_hello(Jon) == "Hello, Jon!"
