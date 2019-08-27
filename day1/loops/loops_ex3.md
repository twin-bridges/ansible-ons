# Loops Exercise 3

1. Create a new Playbook to iterate over the list of IP addresses in your variables. This time, use the "loop" syntax instead of "with_items".

2. Add a second task to acheive the same result as done previously with the "with_dict" syntax, but this time using a loop. We haven't covered filters yet, but a filter will be necessary to acheive the same output. A filter essentially transforms data. In this case, we need a filter to convert the dictionary to a list of key/value pairs. Your loop clause should look similar to:

```
loop: "{{ my_acl | dict2items }}"
```

Your final output should be similar to the following:

```
$ ansible-playbook -i inventory.yaml loops3.yaml

PLAY [looping with "loop"] ************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [localhost] => (item=172.20.1.1) => {
    "msg": "Some IP address... 172.20.1.1"
}
ok: [localhost] => (item=172.30.255.1) => {
    "msg": "Some IP address... 172.30.255.1"
}
ok: [localhost] => (item=10.5.4.1) => {
    "msg": "Some IP address... 10.5.4.1"
}
ok: [localhost] => (item=192.168.99.1) => {
    "msg": "Some IP address... 192.168.99.1"
}

TASK [debug] **************************************************************************************************************************
ok: [localhost] => (item={'key': 'source', 'value': '0.0.0.0/0'}) => {
    "msg": "dictionary key: source; dictionary value: 0.0.0.0/0"
}
ok: [localhost] => (item={'key': 'destination', 'value': '8.8.8.8/32'}) => {
    "msg": "dictionary key: destination; dictionary value: 8.8.8.8/32"
}
ok: [localhost] => (item={'key': 'protocol', 'value': 'tcp'}) => {
    "msg": "dictionary key: protocol; dictionary value: tcp"
}
ok: [localhost] => (item={'key': 'action', 'value': 'permit'}) => {
    "msg": "dictionary key: action; dictionary value: permit"
}

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
