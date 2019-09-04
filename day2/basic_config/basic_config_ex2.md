# Basic Configuration Exercise 2

1. Create a host_vars file for both nxos devices. In this file, create a variable "ip_interfaces" that contains a list of dictionaries. The dictionaries should contain the following values:

    - name of the interface to configure
    - type of ip to configure (ipv4/ipv6)
    - subnet mask

Ensure that you have at least one ipv4 and one ipv6 interface outlined in the vars files. Use any interface(s) between 1/8 and 1/128!

2. Write a Playbook that configures the interfaces using the "nxos_l3_interface" module. Only configure ipv4 interfaces.
