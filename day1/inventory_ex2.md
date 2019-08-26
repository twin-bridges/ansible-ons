# Inventory Exercise 2

1. Create a YAML style inventory containing the following groups/hosts:

Group: arista
Hosts:
    - arista5.lasthop.io
    - arista6.lasthop.io
    - arista7.lasthop.io
    - arista8.lasthop.io

Group: cisco
Hosts:
    - cisco1.lasthop.io
    - cisco2.lasthop.io

Group: juniper
Hosts:
    - srx1.lasthop.io

Group: nxos
Hosts:
    - nxos1.lasthop.io
    - nxos2.lasthop.io


Ensure that the name of the host is just the hostname (i.e. arista5 for arista5.lasthop.io). Add a variable in the "all" group to set the "ansible_connection" to local for all hosts in the inventory.

Use the Ansible command line to execute the ping module against the "all" group; ensure that you are "pointing" to the inventory file you just created with the "-i" flag (substitue "inventory" with the name of your inventory file below):

```
ansible all -m ping -i ./inventory
```

Your results should look similar to the following:

```
$ ansible local -m ping -i ./inventory
srx1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
arista5 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
nxos2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
nxos1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
[SNIP]
```

2. Create a simple Playbook that executes the ping module against all hosts in the inventory.
