# Basic Configuration Exercise 3

1. Create a host_vars file for the pan firewall. In this file, create a variable "address_objects" that contains a list of dictionaries. The dictionaries should contain the following values:

    - name of address object
    - description of address object
    - type of object (ip-netmaks, ip-range, fqdn)
    - address/fdqn

2. Write a Playbook that configures the interfaces using the "panos_address_object" module.
