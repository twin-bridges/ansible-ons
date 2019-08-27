# Modules Exercise 1

1. Add credential information to the previously created inventory file. This can be stored under the "all" vars section (or in the all.yaml group vars if you prefer). The username and password are as follows:

```
username: pyclass
password: 88newclass
```

2. Create a new Playbook, and a Play that operates against the "cisco" group. Create two tasks, the first should use the "ios_facts" module to gather facts and "register" this to a varaiable. The second task should use the "debug" module to print this output to stdout.

3. Add another Play to your Playbook to gather and print facts from the Arista devices.
