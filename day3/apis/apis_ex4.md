# APIs Exercise 4

1. Gather and print all physical interfaces that are in the "up" state. Accomplish this using the "nxapi-rest" API of the nxos hosts. You will need to login to the device using the following JSON payload:

```
{
    "aaaUser": {
        "attributes": {
            "name": "username",
            "pwd": "password"
        }
    }
}
```

Send this payload to the "https://nxoshost:8443/api/aaaLogin.json" endpoint via the POST method. This will return a payload that contains the "APIC-Cookie", you will need to use this cookie to authenticate to the device to gather information.

2. Use "set_fact" to create a header dictionary containing the received cookie. This dictionary should end up looking similar to the following:

```
nxos_headers:
  Cookie: "APIC-Cookie={{ token['cookies']['APIC-cookie'] }}"
```

3. Perform a GET on the "/api/node/class/l1PhysIf.json" endpoint to capture all of the physical interface information. Iterate through this returned object and print out all interfaces that are in the "up" "adminSt".
