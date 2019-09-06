# Inspect vars in inventory graph format:

Use the ansible-inventory tool to add variables to the inventory graph -- an easy way to help visualize variables:

```
ansible-inventory -i inventory.yaml --graph --vars
```

Adding variables to all, groups, and specific hosts can help to show variable precedence!

# Inspecting hostvars using ansible-inventory tool

Variables configured in `host_vars` don't show up in the normal "--graph --vars" output, but you can inspect a host specifically:

```
ansible-inventory -i inventory.yaml --host=localhost1
```
