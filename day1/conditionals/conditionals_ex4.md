# Conditionals Exercise 4

1. Write a Playbook that executes the "panos_api_key" module against the pan_firewalls group. Register the output of this task to a new variable. Remember that you will need to run the paloaltonetworks role prior to executing tasks from the Galaxy module.

```
  roles:
    - role: PaloAltoNetworks.paloaltonetworks
```

2. Update the "provider" argument used to authenticate to the firewall to use the "api_key" field instead of the previously used password field. Only do this if the value of the api key returned in the previous step is not empty!

3. Execute the "panos_api_key" task again, this time using the updated "provider" dictionary. Print the result of this task to stdout.
