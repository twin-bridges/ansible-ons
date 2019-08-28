# Gathering Info Exercise 3

1. Write a Playbook that contains Plays to run the "show system info" command on the pan_firewalls group. You can accomplish this with the "panos_op" module.

2. Parse the stdout_xml to determine the "family" type of the device. If the family type is "vm" print the "vm-mode" to stdout.

Note this task can be a bit difficult if you don't have some exposure to XML/xpath - this task can be acheived by looping through stdout_lines as well, so feel free to use either method!
