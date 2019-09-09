# Variables Exercise 1

1. Use the debug module to "print" the value of the "ansible_host" variable for the arista hosts in the previously created inventory file.

2. Create a directory for both "host_vars" and "group_vars". Create a group vars file for each of the groups in your inventory, in the vars file add a variable "ansible_network_os" and assign it the appropriate platform value:
    - Arista = eos
    - Cisco = ios
    - NXOS = nxos
    - Juniper = junos

Add another Play that contains a task to "print" (debug) the value of the ansible_network_os for each host in your inventory.
