# APIs Exercise 1

1. Create a Playbook with a Play that gathers "show version" information from all of the arista hosts. Use the "eos_command" module for this, and print the results to stdout. Add a second debug task to print the "ansible_connection" argument -- at this point this should be "network_cli"

2. Modify the "arista.yaml" group vars file to set the Ansible connection type to "httpapi". If you execute the Playbook at this point it should run, however you will get a somewhat misleading error about a "command timeout triggered". Add the following lines to the arista group vars:

```
ansible_httpapi_validate_certs: False
ansible_httpapi_use_ssl: True
```

"use_ssl" is set to "False" by default for the "httpapi" connection, and the Arista devices are only listening for HTTPs, so we need to update this setting. "validate_certs" is set to "True" by defualt, but as these are lab devices we have self-signed certificates which would fail validation!

3. Executing your Playbook at this point should end in success, and the final debug task printing that the appropriate ansible_connection of "httpapi".
