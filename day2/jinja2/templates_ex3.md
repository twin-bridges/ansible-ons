# Templates Exercise 3

1. Create a new template that configures a range of interfaces. This template should use a for loop to iterate through a list of dictionaries that define the state of an interface. Use conditional checks to determine if the interface is "l2" or "l3" -- if it is "l3" the template should configure the port to have the following settings:

```
no switchport
ip address 1.2.3.4/32
```

Where the IP address is a variable in the dictionary defining the port. If the switchport is "l2" the template should contain the following configurations:

```
switchport
swithcport mode trunk
```

Ensure that the template and the dictionary that defines each interface also contains a flag for port state ("shutdown" vs "no shutdown").

Create variables in the host vars for the nxos devices to configure at least 5 ports -- use any ports in the range 1/8-1/128.

2. Render your configurations and validate that they are correct. Add a macro for disabled ports - this macro should shut the port, set it to switchport, and set the access VLAN to an unused "black hole" VLAN.
