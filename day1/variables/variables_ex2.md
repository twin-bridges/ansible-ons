# Variables Exercise 2

1. Create a host vars file for the "nxos1" host. Create three variables in this file:
    1. A string variable
    2. A list variable
    3. A dictionary variable

Create a new Playbook to run against only the nxos1 host. Using the debug module print all of these variables to stdout.

2. In the nxos group vars, duplicate one of the variables you created in host vars, but set it equal to a different value, re-run your playbook. Comment out the variable (#) from the host vars, and run the playbook again.

3. Add a Play to your Playbook to run the same tasks, but this time against all of the NXOS hosts.
