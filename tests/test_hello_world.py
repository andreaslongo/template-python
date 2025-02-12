from template_python import lib


def test_greeting():
    assert lib.say_hello() == "Hi there."
