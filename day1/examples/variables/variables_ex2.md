# Variable Precedence

Variables can be defined in Playbooks as well... and lots of places really... here is the list of variable precedence straight from the docs as of Ansible 2.8:

```
Here is the order of precedence from least to greatest (the last listed variables winning prioritization):

command line values (eg “-u user”)
role defaults [1]
inventory file or script group vars [2]
inventory group_vars/all [3]
playbook group_vars/all [3]
inventory group_vars/* [3]
playbook group_vars/* [3]
inventory file or script host vars [2]
inventory host_vars/* [3]
playbook host_vars/* [3]
host facts / cached set_facts [4]
play vars
play vars_prompt
play vars_files
role vars (defined in role/vars/main.yml)
block vars (only for tasks in block)
task vars (only for the task)
include_vars
set_facts / registered vars
role (and include_role) params
include params
extra vars (always win precedence)
```

In the `variables2.yaml` Playbook an "interfaces" variable is defined in the Play variables section. This takes precedence over the group vars variable of the same name.

```
$ ansible-playbook -i inventory.yaml variables2.yaml

PLAY [variables ex2] ******************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [localhost2] => {
    "interfaces": {
        "ethernet": {
            "ethernet1": {
                "ip": false,
                "state": "disabled"
            },
            "ethernet2": {
                "ip": "1.2.3.4",
                "state": "enabled"
            }
        }
    }
}
```

Moreover, we can pass a variable on execution of the Playbook using the "-e" syntax which will overwrite the Play level variables:


```
$ ansible-playbook -i inventory.yaml variables2.yaml -e interfaces=fromcommandline!

PLAY [variables ex2] ******************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [localhost2] => {
    "interfaces": "fromcommandline!"
}
```

# Dealing with Strings

In the same "variables2.yaml" Playbook, two more variables are defined: "splittable_string" and "splittable_string_2".

Calling the "split()" method against "splittable_string" will split on the default delimiter of whitespace:

```
TASK [debug] **************************************************************************************************************************
ok: [localhost2] => {
    "msg": [
        "what",
        "can",
        "i",
        "split.",
        "this",
        "on?"
    ]
}
```

We can also call "splitlines()" against the "splittable_string_2" which contains the `\n` newline character.

```
TASK [debug] **************************************************************************************************************************
ok: [localhost2] => {
    "msg": [
        "this is ",
        " a line ",
        " i guess ",
        " we have so many ",
        " line breaks"
    ]
}
```
