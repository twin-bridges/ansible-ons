# Filters Exercise 1

1. Write a Playbook with a Play to run against the localhost. Create a task using "set_fact" to set a variable "my_ip_address" to the value of the "ip_address" variable (which does not exist). Ensure that the Playbook does not raise an error. Print the value of "my_ip_address" to stdout.

2. Add a third task to set the value of "ip_address" to a value of your choosing. Add a subsequent task that sets the value of "my_ip_address" to the value of "ip_address", ensure that if "ip_address" was not set, the Playbook would not raise an error.

3. Use debug to print a message to screen that is all lower case, using a filter, ensure that the printed message is all upper case.

4. Copy the "somejson.json" file from this repository. Use a lookup to load the contents of this file to a variable. Write the contents of this file to disk. The contents will not be very human readable! Add a task to write "pretty printed" json to a new file.

5. Maybe you don't like json, add another task to print a pretty human readable yaml representation of the json from the previous task.
