# Basic Configuration

Depending on what you need to configure, and the type of device you are trying to configure, you likely will have multiple methods available to you. In general (for network specific things) those will be:

1. ios/eos/junos/etc. config modules
2. Configuration specific module such as: eos_user, nxos_l3_interface, etc.
3. cli_config -- essentially an agnostic wrapper for "network-cli" compatible devices
4. url -- for API enabled devices (more on this later!)

Note that configurations will *not necessarily* be idempotent. It is incumbent on the Playbook creator (not the module creator) to ensure that tasks are idempotent!

Execute the example basic configuration Playbook to see this firsthand:

```
$ ansible-playbook -i inventory.yaml basic_config1.yaml

PLAY [basic config ex1] ***************************************************************************************************************

TASK [eos_config] *********************************************************************************************************************
changed: [arista5]

TASK [eos_user] ***********************************************************************************************************************
changed: [arista5]

TASK [cli_config] *********************************************************************************************************************
changed: [arista5]

PLAY RECAP ****************************************************************************************************************************
arista5                    : ok=3    changed=3    unreachable=0    failed=0
```

The same exact configuration is ran three ways, none of which are idempotent! (in this case this is because the password hashes make this a bit complicated)
