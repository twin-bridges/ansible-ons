# Ansible On Site Training

## Day 1

### Git Overview

1. Lecture
2. [Exercise 1](/day1/git/git_ex1.md)
3. [Exercise 2](/day1/git/git_ex2.md)

### YAML

super high level intro to lists/dicts

1. Lecture
2. [Exercise 1](/day1/yaml/yaml_ex1.md)
3. [Exercise 2](/day1/yaml/yaml_ex2.md)

### Ansible Overview

1. Lecture
    need to cover config file, python version, and...? before jumping into things for real

### Ansible Inventory

1. Lecture
2. [Exercise 1](/day1/inventory/inventory_ex1.md)
3. [Exercise 2](/day1/inventory/inventory_ex2.md)


### Variables

need to get into talking about lists/dicts here a bit more

1. Lecture
2. [Exercise 1](/day1/variables/variables_ex1.md)
3. [Exercise 2](/day1/variables/variables_ex2.md)
4. [Exercise 3](/day1/variables/variables_ex3.md)


### Ansible Modules

steal from class2 ++ what is a module, show where to find module index, etc. maybe a quick discussion/highlight of copy, command/shell since those are v handy to know
here we will start actually interacting w/ lists dicts a little more (w/out loops so far)

1. Lecture
2. [Exercise 1](/day1/modules/modules_ex1.md)
3. [Exercise 2](/day1/modules/modules_ex2.md)
4. [Exercise 3](/day1/modules/modules_ex3.md)


### Loops
steal from https://github.com/ktbyers/pynet-ons-jul17/tree/master/ansible/loops

1. Lecture
2. [Exercise 1](/day1/loops/loops_ex1.md)
3. [Exercise 2](/day1/loops/loops_ex2.md)
4. [Exercise 3](/day1/loops/loops_ex3.md)
5. maybe another at least outlining how you can zip things / cartesian stuff? maybe thats too much at this point?

### Conditionals
steal from https://github.com/ktbyers/pynet-ons-jul17/tree/master/ansible/conditionals

1. Lecture
2. [Exercise 1](/day1/conditionals/conditionals_ex1.md)
3. [Exercise 2](/day1/conditionals/conditionals_ex2.md)
3. [Exercise 3](/day1/conditionals/conditionals_ex3.md)


## Day 2

### Gathering Information

probably just a quick discussion about recapping lists/dicts and then a demo of "getting" data and parsing it from something
exercises to get info from device ++ parse
facts -- both ios_facts (or w/e) but also "normal" facts

1. Lecture
2. get facts from something and access / print (debug) some thing; add a conditonal to only do this if XYZ
3.

### Basic Configuration Changes
steal from https://github.com/ktbyers/ansible_course/tree/master/class3/exercises

using built in config modules

1. Lecture
2.
3.

### Handlers
steal from

include at least something *not* network related (restart a service or even just run some other task to show that i could be whatever)

1. Lecture
2. save config handler
3. something/anything else?

### Tags
steal from

skip tags, always, never, list of tags, etc.

1. Lecture
2. maybe just one tags lecture?

### Jinja2
steal from

template configs (or literally whatever)

1. Lecture
2. basics
3. for loop
4. conditionals
5. inherits


## Day 3

### Ansible Vault

1. Lecture
2. Setup Vault
3. vault get pass
4. vault password file
5. rekey vault

### Ansible and direct API Calls

1. Lecture
2. URI module GET
3. URI module POST
4. URI module DELETE/PATCH/PUT?

### Lookups

1. Lecture


### Filters

### Roles

### Validating Changes

### Debugging


## Day 4

### Galaxy

### Network Engine

### TBD
