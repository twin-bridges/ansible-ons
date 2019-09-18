# Gathering Info Exercise 4

1. Write a Playbook that contains a Play to run the "show system info" command on the pan_firewalls group. You can accomplish this with the "panos_op" module.

2. Convert the "stdout" text to a dictionary using a filter (we'll cover these more later) that converts json text to a dictionary. Example:

```
json_output: "{{ output['stdout'] | from_json }}"
```

3. Parse this new dictionary object to capture the "family" type -- in our case this should be "vm". Use the debug module to print the "vm-mode" of the firewall, but only WHEN the family is equal to "vm".

4 (Optional). Parse the stdout_xml to determine the "family" type of the device. If the family type is "vm" print the "vm-mode" to stdout.

*Note* this task can be a bit difficult if you don't have some exposure to XML/xpath!
