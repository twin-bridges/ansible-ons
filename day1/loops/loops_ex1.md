# Loops Exercise 1

1. Add a "local" group containing a host for your localhost to the inventory file. Ensure that the localhost "ansible_connection" is set to local (do this in the inventory, host, or group vars).

2. Create a list of IP addresses in host vars for the "localhost" host -- this list should contain at least three IP addresses.

3. Using the "with" syntax, iterate through list of IP addresses and print them out with a message. Your output should be similar to the following:

```
$ ansible-playbook -i inventory.yaml loops1.yaml

PLAY [looping with "with"] ************************************************************************************************************

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

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```
