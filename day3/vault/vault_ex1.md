# Vault Exercise 1

1. Rather than storing the credentials in the inventory file, create a directory "all" in the group_vars folder (also remove them from the inventory file!). Within this folder create a "creds.yaml" file that contains the device credentials.

2. Use Vault to encrypt this file: "ansible-vault encrypt MYFILE"; use a simple password so you don't forget!

3. Write a Playbook that connects to any of the devices and gathers facts, use debug to print the facts to stdout to validate that you are able to access the devices with the encrypted credentials. To execute your Playbook and decrypt the vaulted file you can add the "--ask-vault-pass" argument. Your output should be similar to the following:

```
$ ansible-playbook -i inventory.yaml vault1.yaml --ask-vault-pass
Vault password:

PLAY [vault ex1] **********************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
ok: [cisco1]

TASK [debug] **************************************************************************************************************************
ok: [cisco1] => {
    "ansible_facts": {
        "VHC128": {
            "device": "VHC128",
            "flags": [],
            "ipv4": [],
            "ipv6": [],
            "macaddress": "unknown",
            "mtu": "0",
            "type": "unknown"
        },
        [SNIP]
```
