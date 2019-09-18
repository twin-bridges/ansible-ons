# Palo Alto "panos_op" Output JSON and XML

The "panos_op" module is pretty handy. It lets you run arbitrary commands against a firewall or Panorama host. This is great for those cases where there is no module to capture some desired data, however there is a pretty significant challenge here... what does the data that comes back look like?

In general you'll see a very json-looking blob of text, in addition to the "stdout_xml". Both of these options provide ways to get the data you need in a structured fashion.

## Dealing with JSON from a string

Ansible is smart enough to see json text and know that it can be easily converted to a dictionary. In this case, we capture the "stdout" from a "panos_op" module call.

```
"{{ output['stdout'] }}"
```

Once the data has been "loaded" up to a variable as a dictionary, we can access it as we would any other dictionary:

```
"{{ json_output.response.result }}"
```

## Dealing with XML

XML provides a little bit differnet challenge. XML unlike JSON is not as easy to convert to a dictionary, however we have other means of dealing with it, namely the "xml" module.

The "xml" module allows us to pass in an xml string, and search it using "xpath". "xpath" is basically used to allow us to capture the text at a particular element in the xml tree as in the following example:

```
    - xml:
        xmlstring: "{{ output['stdout_xml'] }}"
        xpath: /response/result
        content: text
```

In this case, we can get all of the "result" data from the xml tree. We don't need to get much fancier than this at this point, but if you are interested in more about xpath [here](https://www.w3schools.com/xml/xpath_syntax.asp) is a good overview.
