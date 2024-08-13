import argparse
from template_python.lib import say_hello


def run():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    print(say_hello())
