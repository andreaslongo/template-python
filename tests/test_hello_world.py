from template_python.lib import say_hello


def test_greeting():
    assert say_hello() == "Hi there."
