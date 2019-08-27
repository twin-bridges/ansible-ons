# Loops Exercise 2

1. Create a dictionary containing ACL data for the "localhost" host. The data should look similar to the following.

```
my_acl:
  source: 0.0.0.0/0
  destination: 8.8.8.8/32
  protocol: tcp
  action: permit
```

2. Using the "with" syntax, iterate through list of IP addresses and print them out with a message. Your output should be similar to the following:

```
$ ansible-playbook -i inventory.yaml loops2.yaml

PLAY [looping with "with" -- dicts] ***************************************************************************************************

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
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```
