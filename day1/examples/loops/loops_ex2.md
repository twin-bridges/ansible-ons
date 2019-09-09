# More Complicated Loops!

As seen previously, its fairly straightforward to iterate over a list or a dictionary. Often times, though, you'll need to iterate over a list of dictionaries or some other more complicated data structure.

Using loop on a list of dictionaries is fairly easy, and prints a reasonably useful output:

```
$ ansible-playbook -i inventory.yaml loops2.yaml

PLAY [loops ex2] **********************************************************************************************************************

TASK [debug] **************************************************************************************************************************
ok: [nxos1] => (item={'ips': ['1.2.3.4', '10.10.10.1'], 'interface': 'interface1'}) => {
    "item": {
        "interface": "interface1",
        "ips": [
            "1.2.3.4",
            "10.10.10.1"
        ]
    }
}
[SNIP]
```

If we wanted to access items in dictionary currently being iterated over we can do that:

```
    - debug:
        msg: "{{ item.interface }}: {{ item.ips }}"
      loop: "{{ list_of_dicts }}"
```

Producing a useful output:

```
TASK [debug] **************************************************************************************************************************
ok: [nxos1] => (item={'ips': ['1.2.3.4', '10.10.10.1'], 'interface': 'interface1'}) => {
    "msg": "interface1: ['1.2.3.4', '10.10.10.1']"
}
```

It is possible to even iterate over `subelements` of the current loop -- such as the IP addresses:

```
    - debug:
        var: item
      loop: "{{ list_of_dicts | subelements('ips') }}"
```

Which causes an iteration per IP in the list of dictionaries!

```
[SNIP]
ok: [nxos1] => (item=[{'ips': ['224.0.0.1', '8.8.8.8'], 'interface': 'interface5'}, '224.0.0.1']) => {
    "item": [
        {
            "interface": "interface5",
            "ips": [
                "224.0.0.1",
                "8.8.8.8"
            ]
        },
        "224.0.0.1"
    ]
}
ok: [nxos1] => (item=[{'ips': ['224.0.0.1', '8.8.8.8'], 'interface': 'interface5'}, '8.8.8.8']) => {
    "item": [
        {
            "interface": "interface5",
            "ips": [
                "224.0.0.1",
                "8.8.8.8"
            ]
        },
        "8.8.8.8"
    ]
}
[SNIP]
```
