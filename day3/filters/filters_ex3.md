# Filters Exercise 3

1. Use the napalm_get_facts module and the 'mac_address_table' filter to retrieve the switching table from nxos1. Use a 'template' lookup and an external Jinja2 template to convert the data structure retrieved by NAPALM to a new dictionary where the key is the MAC address and the corresponding value is the interface. You will want to use this external Jinja2 template lookup to generate YAML output.
