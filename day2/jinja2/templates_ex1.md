# Templates Exercise 1

1. Use a single Jinja2 template, a "platform" variable, and a conditional to generate configurations for the below items. You should generate configurations for the two Cisco IOS devices, the two NX-OS devices, and the four Arista switches.

    name_server1: 8.8.8.8
    name_server2: 8.8.4.4
    default_domain: lasthop.io
    ntp1: 130.126.24.24
    ntp2: 152.2.21.1

Store the template that you use to generate this configuration in a "templates" directory, store the output of the rendered templates in a "configurations" directory.

You will need to configure the following variables in your inventory to avoid an "AnsibleUndefinedVariable" error, do this in the group vars for the "all" group.

    default_domain
    name_server1
    name_server2
    ntp1
    ntp2

2. Add tasks to the play to use the standard Ansible "X_config" modules to deploy the configurations to the devices.

3. Add tags to your Playbook such that the Playbook could be executed against one of the groups at a time (cisco, nxos, eos).
