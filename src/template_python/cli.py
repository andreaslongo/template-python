import argparse
from template_python.lib import say_hello


def run():
    parser = argparse.ArgumentParser()
    _args = parser.parse_args()

    print(say_hello())
