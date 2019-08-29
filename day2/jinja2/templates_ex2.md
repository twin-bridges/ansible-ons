# Templates Exercise 2

1. Create a Playbook to configure a BGP peering between the nxos hosts. To do so, create a Jinja2 template that, when rendered, looks similar to that show below.

Where XXXX is four random hex digits that you choose
```
interface Ethernet1/4
  ipv6 address 2001:db8:XXXX:200c::1/64
  no shutdown

router bgp 22
  neighbor 2001:db8:XXXX:200c::2 remote-as 22
    address-family ipv6 unicast
```

You can choose any interface from Ethernet1/1 to Ethernet1/4. You should make variables for any of the items that change in the template. These variables should be added into 'host_vars'.


2. Use the "napalm_install_config" module to send the configuration to the devices. To start, set "commit_changes" and "replace_config" to "False". To confirm that this operation would make a change if set to commit changes, output the diffs to a new directory "diffs". Napalm requires a "provider" argument. Craft this variable in your Play vars or in appropriate group vars files. Note that this provider argument must include an argument "optional_args" which is a dictionary -- in this dictionary there must be a key for "port" with a value of 8443. This 8443 is the nxapi port number.

3. Modify your Playbook to include tags representing each task -- config generation and config push/diff operation. Change the "napalm_install_config" task to set "commit_changes" to "True". Run your Plalybook. At the end of the configuration push, you should be able to ping IPv6 from nxos1 to nxos2 and you should have a working BGP session between the two switches.
