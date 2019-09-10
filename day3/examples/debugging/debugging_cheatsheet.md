# Debugging Basics

## Its basically always YAML!

If you're fighting YAML syntax/formatting issues, its worth giving this article a [read](https://www.redhat.com/sysadmin/yaml-tips).

Our favorite tips from the linked article:

1. Have your editor (vi/Sublime/Atom/etc.) show whitespace -- this helps make sure you can easily spot indentation errors.
2. Use a YAML linter such as [yamllint](https://pypi.org/project/yamllint/).
3. Pick an indentation that helps -- indent with 2 spaces, 3, 4, 8, 16... whatever works for you! By changing the indentation you can make your YAML files easier for you to read based on your preferences.


## Connection Types

For network devices, always remember that Ansible operates in a "non-standard" way for network devices in that the Playbook task modules are executed *locally*. This can cause some confusing errors such as the `unable to open shell` error. This error is often times hiding an authentication issue.

Always confirm that you are using the correct connection type for your selected module.

## Verbosity

Having issues? Crank up the verbosity using the `-v` flag. Still not seeing what you want? Add more verbosity... `-vvvv`.


## Logging

Turn on logging to help capture logs to a file for easier parsing:

```
$ export ANSIBLE_DEBUG=True
$ export ANSIBLE_LOG_PATH=~/ansible.log
$ ansible-playbook debugging1.yaml -vvvv
```
