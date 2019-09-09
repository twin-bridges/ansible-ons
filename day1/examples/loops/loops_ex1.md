# Basic loops

A list of IP addresses is defined in the group variables file for the nxos group. Using the "loop" keyword we can have Ansible "iterate" through all elements of the list. Ansible assigns the value of the current iteration to the variable "item".

```
$ ansible-playbook -i inventory.yaml loops1.yaml

PLAY [loops ex1] **********************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [nxos1] => (item=1.2.3.4) => {
    "item": "1.2.3.4"
}
ok: [nxos1] => (item=10.10.10.1) => {
    "item": "10.10.10.1"
}
ok: [nxos1] => (item=172.31.255.1) => {
    "item": "172.31.255.1"
}
ok: [nxos1] => (item=192.168.0.1) => {
    "item": "192.168.0.1"
}
ok: [nxos1] => (item=224.0.0.1) => {
    "item": "224.0.0.1"
}
ok: [nxos1] => (item=8.8.8.8) => {
    "item": "8.8.8.8"
}
```

Using very similar syntax it is also possible to iterate through a dictionary. When iterating through a dictionary, however, it must be cast to a list of key/value pairs -- this can be acheived with the `dict2items` filter (more on filters later!):

```
TASK [debug] **************************************************************************************************************************
ok: [nxos1] => (item={'key': 'interface1', 'value': '1.2.3.4'}) => {
    "item": {
        "key": "interface1",
        "value": "1.2.3.4"
    }
}
ok: [nxos1] => (item={'key': 'interface2', 'value': '10.10.10.1'}) => {
    "item": {
        "key": "interface2",
        "value": "10.10.10.1"
    }
}
[SNIP]
```

Item becomes a dictionary itself which allows for accessing either the key or the value of the current iteration:

```
    - debug:
        msg: "{{ item.value }}"
      loop: "{{ dictionary_of_ips | dict2items }}"
```

In the above example, we access the "value" (IP address in this case) and print this in our debug "msg".
