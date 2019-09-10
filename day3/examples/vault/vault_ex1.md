# Vault

Ansible comes installed with "ansible-vault" which provides a way to encrypt secrets and decrypt them on the fly for Playbook execution.

There are two primary means of providing Vault passwords to decrypt vaulted secrets:

1. Use the `--ask-vault-pass` flag when executing the Playbook -- this will prompt the user for the password to decrypt the vaulted secrets
2. Use the `--vault-password-file` flag, passing in a script that returns the password.
    - This option is pretty powerful as the script can do basically anything -- including query other password managers, figure out what "environment" the Playbook is being ran in (to provide the associated vault password), or really whatever else you can think up!

To actually handle (encrypt, decrypt, view, rekey, etc.) files or variables, use the `ansible-vault` command line tool with the appropriate flags.

```
ansible-vault encrypt group_vars/all.yaml
```

Vault can be used to encrypt strings as well -- these strings can then be included in a "normal" (non-vaulted) file:

```
ansible-vault encrypt_string "sneakyvar"
```

Execute a Playbook using "ask-vault-pass":

```
ansible-playbook -i inventory.yaml vault1.yaml --ask-vault-pass
```

Or with the "vault-password-file" option -- make sure that the script has an appropriate shebang and is executable!

```
ansible-playbook -i inventory.yaml vault1.yaml --vault-password-file vault_pass.sh
```

Note: the vault password for the examples here is simply "password"
