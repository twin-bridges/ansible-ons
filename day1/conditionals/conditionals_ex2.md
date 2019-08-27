# Conditionals Exercise 2

1. Write a Playbook that executes the "ios_facts" module against the cisco group. Register the output of this task to a new variable.

2. Add a Task to print (debug module) the value of a variable that does not exist in the registerred output -- for example "device_hostname". Executing your Playbook should indicate that the variable is not defined.

3. Add an additional Task that prints the same variable as the the previous step -- but does so only when the the variable is defined.
