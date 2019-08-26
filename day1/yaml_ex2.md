# YAML Exercise 2

1. Create a YAML document (.yml/.yaml) that contains a list of values AND a dictionary. Ensure this dictionary contains at least four keys -- the values of these keys could be strings, booleans, lists, or another dictionary.

Use the following Python snippet to print this list to screen (substitute "myfile.yaml" with your filename):

```python
#!/usr/bin/env python
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    filename = "myfile.yaml"
    pprint(read_yaml(filename))
```
