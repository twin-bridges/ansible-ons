# APIs Exercise 7

1. Using what you've learned, create an address object using the XML API. Take advantage of the "debug cli" to help show you how to construct your url:

```
debug cli on
configure
set address SOMEADDRESSOBJECT ip-netmask X.X.X.X/X
```

The debug cli output should be similar to:

```
<request cmd="set" obj="/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='someobject']
" cookie="4480226471677181"><ip-netmask>1.1.1.1/32</ip-netmask></request>
```

This provides you most of the information required to create your Playbook. In addition to the API key you will need to pass the following arguments:

  - type
  - action
  - xpath

Your result (by using debug to print the response from your url module call) should contain a response status indicating success:

```
<response status=\"success\" code=\"20\"><msg>command succeeded</msg></response>
```
