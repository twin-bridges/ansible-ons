# Roles

Roles allow for combining a grouping of variables, templates, files, and of course tasks that all work together to accomplish a particular outcome. This example is small and somewhat trivial in interest of keeping it simple, however the same patterns apply to much larger roles. An example of a much larger role could be the role used to install StackStorm -- you can find that [here](https://github.com/StackStorm/ansible-st2).

The example role deploys a simple "backup" shell script (really it just echoes a silly message), and creates a crontab entry to run this script every so often. This is quite similar to a "backup" role that we deploy on all of our production servers.

This role contains `files`, `tasks`, and `vars`. Files is a directory that any tasks in the role will search first for any files that need to be copied to a remote host. In this case, our shell script lives here. `vars` contains any role specific variables; role-level vars can be overridden by Playbook/inventory variables if needed. In our case, we simply have a name of the crontab entry stored in a `var` for this role.

Lastly, the `tasks` directory contains a file `main.yaml` that is the "entrypoint" for the role when the role is called. This file contains all the tasks necessary to setup our backup solution.

You can execute the `roles1.yaml` Playbook on your lab server to view the results.

Inspect the crontab before and after using the `crontab -l` command -- you can remove the crontab with `crontab -r` if you want to change any values in the role to see how it affects the outcome!
