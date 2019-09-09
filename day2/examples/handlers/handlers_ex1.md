# Handlers

Handlers are tasks that are ran when a change has occurred for a given task(s). Essentially the "notify" argument allows *changed* tasks to alert a handler (basically just another task just in a special place) that a change has occurred.

In theory a Playbook should aim to be as idempotent as possible, and because of this, there shouldn't really be a need for handlers, however -- especially in the network space -- this is just not reality. For networking a command handler would be to save the configuration *if* a change occurred.

To demonstrate that handlers are only executed when a task is *changed*, check out the example Playbook:

```
$ ansible-playbook -i inventory.yaml handlers1.yaml

PLAY [handlers ex1] *******************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "unhandled task :("
}

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "handled task????"
}

TASK [debug] **************************************************************************************************************************
changed: [localhost] => {
    "msg": "handled task!"
}

RUNNING HANDLER [handle_this] *********************************************************************************************************
ok: [localhost] => {
    "msg": "STUFF HAS CHANGED, DONT FREAK OUT!"
}

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0
```

In the example debug tasks will never be marked as "changed" unless done so explicitly. Marking the third debug task with "changed_when: True" will ensure that it is always in a changed state, causing the handler to "fire".

