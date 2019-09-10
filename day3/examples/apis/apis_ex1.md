# APIs Example 1

Depending on the platform/operating system (of network devices) that you need to interact with, it may be a very trivial change to "switch" from connecting via SSH to connecting via an API.

For the nxos and eos devices, this is certainly the case. To migrate to the httpapi, modifying a few basic settings to set the appropriate connection type, and in our case ignore self signed certificates and use SSL is all that it takes:

```
ansible_connection: httpapi
ansible_httpapi_use_ssl: True
ansible_httpapi_validate_certs: False
```

Since you can't really tell from the output of running `eos_command` tasks if you've successfully "made the switch" to using the API, you can always crank up the verbosity, or even print out the Ansible connection type via the debug module as is done in the example task.

```
ansible-playbook -i inventory.yaml apis1.yaml
```
