# Inventory Exercise 1

1. Create a simple INI-style Ansible inventory file with a single entry for the localhost. Ensure that this localhost is configured under a group called "local", and that the "ansible_connection" is set to local (this is so we don't need to worry about any authentication yet).

Use the Ansible command line to execute the ping module against the group you created ("local"); ensure that you are "pointing" to the inventory file you just created with the "-i" flag (substitute "inventory_ex1" with the name of your inventory file below):

```
ansible local -m ping -i ./inventory_ex1
```

Your results should look similar to the following:

```
$ ansible local -m ping -i ./inventory_ex1
localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

2. Add another host to your "local" group, add a second group ("other") and a third host in the new group as well. Re-run the command executed previously. As the ping module is executing only against the "local" group, there should only be two results printed.

3. Execute the same command against the implicit "all" group, ping should be executed against all three hosts.
