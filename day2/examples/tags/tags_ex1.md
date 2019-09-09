# Tags

Not exciting sounding, but very useful. In general, Playbooks should do a "thing" -- a whole "thing"! The thing that a Playbook does, however, is often times made up of multiple tasks. For example, you may have a task or group of tasks that configure a widget, and also have a group of tasks that validates the widget. Using tags you can keep all of this logically grouped in a single Playbook, but still have the ability to easily execute only the test phase for example.

There are also two "special" tags: "always", and "never" -- these do about what you'd expect! The "always" tag will always run unless explicitly skipped, and the "never" tag never runs unless explicitly included.

Take a look at the example Playbook -- use the "--list-tags" argument to check out what tags are available:

```
$ ansible-playbook tags1.yaml --list-tags

playbook: tags1.yaml

  play #1 (localhost): tags ex1 TAGS: []
      TASK TAGS: [always, ca, moon, pnw, sea, sfo]
```

Execute the Playbook using some combination of "--tags" and "--skip-tags". Also note that there are three other "special" keywords here: "tagged", "untagged", and "all" -- when passed with either tags or skip tags these work as you'd expect!

```
$ ansible-playbook tags1.yaml --tags=untagged

PLAY [tags ex1] ***********************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [localhost] => {
    "msg": "the mooooooooon!"
}

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```
