# Debugging Exercise 1

1. Use 'ssh-keygen -R cisco1.lasthop.io' to remove the SSH key for the cisco1 device. Set the "host_key_checking" value in your ansible.cfg file to True. Verify that a simple 'ios_facts' playbook that tries to connect to the 'cisco' group now fails for this host.

2. Experiment with turning on Ansible's SSH debugging (using those Ansible environment variables). Look for the error message that you receive in the log file for cisco1.lasthop.io.

3. Modify the .ansible.cfg file to disable 'host_key_checking'. Re-execute your playbook and verify your playbook now runs.

4. Run 'ssh -l pyclass cisco1.lasthop.io' to save the SSH key in known hosts. You can decide whether you want to leave host_key_checking enabled or disabled in .ansible.cfg.
