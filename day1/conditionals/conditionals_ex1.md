# Conditionals Exercise 1

1. Write a Playbook that executes on the "localhost" host. This Playbook should contain five tasks, these task should do the following:
  1. Print a message when "False"
  2. Print a message when "True"
  3. Print a message when a variable is equal to some value (use an existing variable or define one in your Play)
  4. Print a message when a variable contains a string
  5. Print a message when a variable does NOT contain a string

Your output should be similar to the following -- note the "skipping" in several of the tasks!

```
$ ansible-playbook -i inventory.yaml conditionals1.yaml

PLAY [conditionals ex1] ***************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
ok: [localhost]

TASK [debug] **************************************************************************************************************************
skipping: [localhost]

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "TRUE: Hello World"
}

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "racecars are fast!"
}

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "racecars are still pretty fast!"
}

TASK [debug] **************************************************************************************************************************
skipping: [localhost]

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0
```
