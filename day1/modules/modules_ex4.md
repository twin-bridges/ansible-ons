# Modules Exercise 4

1. Add data to your inventory structure to define the Palo Alto firewall instance. You will need the following information:

    - ansible_host: [ask your instructor for ip/name]
    - ansible_connection: local
    - ansible_python_interpreter: /usr/local/bin/python

This device should be a member of a group "pan", and "pan_firewalls". Depending on how you configured your credential information you may not need to make any changes as the firewall uses the same standard credentials as the other devices. The "ansible_python_interpreter" setting can be configured for all devices via the "all" vars in the inventory or "all" group_vars.

2. Create a new Playbook, and a Play that operates against the "pan_firewalls" group. In this Playbook use the "panos_check" module to check that the firewall is reachable. You will need to create a dictionary variable to pass to the provider argument of the the "panos_check" module. Create this dictionary in the Play level vars -- it must have the following fields:

    - ip_address
    - username
    - password

Prior to executing any "panos_" modules it is necessary to import the PaloAltoNetworks Ansible Galaxy role -- this role validates that required modules are installed (this part has been modified in the lab environment to *not* check for packages so this doesn't need to be executed each time) and sets module path arguments for you.

Prior to creating your tasks, include this in your Playbook:

```
  roles:
    - role: PaloAltoNetworks.paloaltonetworks
```

Finally, add a task that executes the "panos_check" module, this module has a "provider" argument which you should pass your previously created dictionary to.

3. Register the output of the "panos_check" task, and print this to stdout.

4.
