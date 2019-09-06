# Gather device facts for nxos1

Use the "nxos_facts" module to capture device facts, then print those facts out

```
ansible-playbook -i inventory.yaml modules_ex1.yaml
```

# Providing arguments to a module

Module documentation should always tell you what are valid arguments and what you can pass to those arguments. In this case we can limit the "facts" gathered to just the interface facts.

You can see this in the nxos_facts module documenation [here](https://docs.ansible.com/ansible/latest/modules/nxos_facts_module.html).

Trying to print out a subset of the facts that would *not* be gathered (after setting facts to only gather interface information) will cause a "VARIABLE IS NOT DEFINED" message.

```
ansible-playbook -i inventory.yaml modules_ex1.yaml
```
