# Conditionals

Ansible's "when" clause allows us to check the "truthiness" of a condition.

For example we can run a task *if* a result evaluates to be "true". Take the following when clause:

```
when: device_facts.ansible_facts.ansible_net_all_ipv6_addresses == []
```

IF the list of ipv6 addresses is empty, we can execute a task.

Conditionals can be used with boolean AND, or OR clauses as well. When given a list of conditions, Ansible will automatically assume that the conditions are joined via an "AND":

```
      when:
        - device_facts.changed == false
        - device_facts.failed == false
```

OR clauses can be simply written out:

```
      when: (device_facts.changed == true) or (device_facts.failed == false)
```

It is common practice to enclose each condition in parenthesis to make things a bit easier to read!
