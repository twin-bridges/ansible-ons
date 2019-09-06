#!/usr/bin/env python
from pprint import pprint
import sys
import yaml


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    filename = sys.argv[1:][0]
    pprint(read_yaml(filename))
