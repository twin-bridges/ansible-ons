# Debugging Exercise 2

1. Configure five VLANs on the arista7 switch. Use random VLAN IDs between 100 and 999. Assign both a VLAN name and a VLAN ID. Note, arista7 will already have VLANs 1 - 7 configured using a name of "default" or "VLAN000X".

2. Validate that the ONLY VLANs on that switch are the five VLANs that you just configured and the eight default VLANs (VLANs 1 - 7).

3. Have the playbook fail with a clear error message if any additional VLANs are configured on that switch.
