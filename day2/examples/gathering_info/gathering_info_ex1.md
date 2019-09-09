# Ansible Facts

Often times "gather_facts" is disabled on Playbooks for network devices, and there is good reason for this! Check out the "ansible_facts" from the example 1 gathering_info Playbook -- notice anything interesting?

```
[SNIP]
        "pkg_mgr": "homebrew",
        "processor": "Intel(R) Core(TM) i9-8950HK CPU @ 2.90GHz",
[SNIP]
```

Something tells me most switches don't use "homebrew" as a package manager! This happens because even though the Arista hosts in this example are setup to use "network_cli" Ansible is still really doing "connection: local" -- meaning that it is running the modules on the local system. So, in this example, we've gathered facts about the local (MacOS in this example) system instead of the switch.

# Device Facts

Of course as you've seen, the eos/ios/junos/etc. "facts" modules can gather actual network-device specific facts. Don't overlook how useful this can be! You'll get back structured data that covers a pretty wide range of facts about devices.


# Command Modules

If you need to capture some other information, eos/ios/junos/etc. "command" modules allow for running any arbitrary command. While not covered at this point, it is also possible to use TextFSM or Cisco Genie to parse output into a structured format!
