# More Configuration Exercise 2

1. Create a Playbook that operates against the "arista8" host. Using NAPALM, capture the configuration from the device.

2. In a second task, write the captured configuration to a "configs" directory. Ensure that you can write the startup OR the running configuration to disk. Whatever you chose as the default option, ensure that by passing an additional argument when running the Playbook you can backup the opposite configuration (startup vs running).

3. Add a task to replace the device configuration with the configuration stored in the "configs" directory.

4. Add tags to this Playbook such that you could just backup/save the config or just deploy the config, or of course do everything.
