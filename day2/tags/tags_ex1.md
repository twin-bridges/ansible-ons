# Handlers Exercise 1

1. Write a Playbook with a Play that runs against only the localhost. In this Playbook create five tasks that print messages to stdout.

2. Add tags to these tasks to controll when they are executed. Add a list of tags to at least one task. Use the "never" and "always" tags.

Execute your Playbook testing a variety of different combination of tags to see the outcome:

```
ansible-playbook -i inventory.yaml tags1.yaml --tags=red
ansible-playbook -i inventory.yaml tags1.yaml --tags=red,blue
ansible-playbook -i inventory.yaml tags1.yaml --tags=always
ansible-playbook -i inventory.yaml tags1.yaml --tags=never
ansible-playbook -i inventory.yaml tags1.yaml --skip-tags=always
```

3. Add handlers into your Playbook -- put tags on your handlers to see how handlers are affected by tags. Put a "never" tag on one of your handlers and run the Playbook in such a way that this handler would be notified... does it run? What if you "skip" the never tags?

```
ansible-playbook -i inventory.yaml tags1.yaml --tags=blue --skip-tags=never
```
