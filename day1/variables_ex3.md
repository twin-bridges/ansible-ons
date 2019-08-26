# Variables Exercise 3

1. Create a new Playbook to run against only the nxos1 host. Use the "set_fact" module to create a new variable that concatenates the first two items of the list variable previously created (if you didn't create a list with at least two entries, do so now!). Use the debug module to print this newly created variable to stdout.

2. Create another variable that contains only the domain name of the nxos1 host -- i.e. capture just the "lasthop.io" portion of "nxos1.lasthop.io", store this in a variable and print it to stdout.
