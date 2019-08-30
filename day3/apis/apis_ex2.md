# APIs Exercise 2

1. Using the nxapi (nxapi port needs to be set to 8443!), gather the CDP or LLDP neighbors from the nxos devices. Using this data, configure appropriate descriptions on interfaces E1/1-4 -- your description should look something like the following for E1/1 on nxos1 (note that E1/1-4 all connect "back-to-back" on the nxos devices):

```
description to {{ remote host }} port {{ remote port }}
```
