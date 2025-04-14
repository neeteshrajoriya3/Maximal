def test_check_abc():
    from utils.helloprinting import Abc
    obj = Abc()
    print(obj.printing_hello())  # Should print "Hello"
    assert obj.printing_hello() == "Hello"