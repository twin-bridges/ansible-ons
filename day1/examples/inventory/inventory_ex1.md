# Test the inventory ini file

Ping all members of the local group:
```
ansible local -m ping -i ./inventory.ini
```

# Test the inventory yaml file

Ping all members of the local group:
```
ansible local -m ping -i ./inventory.yaml
```

# Test either inventory format against "all" hosts

Ping all hosts:
```
ansible all -m ping -i ./inventory.yaml
```

# Test either inventory format against all EXCEPT localhost1

Ping all hosts except localhost1; note that we must escape the `!` symbol!
```
ansible all:\!localhost1 -m ping -i inventory.yaml
```

# Use the ansible-inventory tool to investigate the inventory

"Graph" the inventory:
```
ansible-inventory -i inventory.yaml --graph
```

This is also a handy way to validate the inventory file before doing anything else!
