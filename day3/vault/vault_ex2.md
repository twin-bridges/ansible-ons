# Vault Exercise 2

1. Destroy the previously created "creds.yaml" file. This time, create two files in the "all" group vars directory: "user.yaml" and "pass.yaml". Encrypt the files with the same vault password.

2. Execute the Playbook created in the previous task with the "--ask-vault-password" argument once more. This should succeed. In practice, Ansible vault works very well with a single Vault password, but is not intended for "per-user" credentials; it is more focused on per "environment" credentials. While we won't cover it here, you can assign "vault-ids" to vaulted files. These ids generally correspond to "environments" in this fashion you can have a vault password per environment and maintain isolation of the passwords/creds/sensetive information.

3. Create a simple shell or bash script that echos whatever you set your vault password to to stdout. Ensure that the script is executable. If ran, your script output should be similar to the following:

```
$ vi vault2.sh
$ chmod +x vault2.sh
$ ./vault2.sh
password
```

4. Re-execute the Playbook -- this time use "--vault-password-file" option. Pass your script to this argument, your Playbook should execute without prompting for Vault credentials.

5. Rather than passing the "--vault-password-file" argument at each execution, set the environment variable "ANSIBLE_VAULT_PASSWORD_FILE" to "point" to your script, re-run the Playbook without specifiying any vault cli arguments, ensure that your Playbook executes successfully.
