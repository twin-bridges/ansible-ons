# Regular Expressions Exercise 1

1. Write a Playbook to gather the output of "show interface Ethernet1" from the arista5 device.

2. Set a fact for each of the following values -- use the regular expression filter to parse the stdout to capture the values.
    - packets input
    - packets output
    - bytes input
    - bytes output

3. Print the captured results to stdout:

```
ok: [arista5] => {
    "msg": [
        "Ethernet 1 packets: 123054 input; 29256 output",
        "Ethernet 1 bytes: 15291503 input; 2760276 output"
    ]
}
```
