# APIs Exercise 5

1. Before doing much of anything with the Palo Alto firewall, we'll need to figure out how to get a token. The Palo Alto docs provide a handy curl command that we can execute:

```
curl -X -k GET 'https://[FIREWALL IP/NAME]/api/?type=keygen&user=[USERNAME]&password=[PASSWORD]'
```

Using the "get_url" and "xml" modules, create a Playbook which executes a get, saves the response to an xml file, and then parses the result to capture the API key needed for further working with the firewall.

2. Using the "uri" module, capture the API key as done in the previous step.


