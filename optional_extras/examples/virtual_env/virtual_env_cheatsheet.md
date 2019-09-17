# Virtual Environment Basics


## Create a Virtual Environment
```
python -m venv <name of your virtual environment>
```


## Activating a Virtual Environment
```
source <name of your virtual environment>/bin/activate
```
*assuming you are in the directory where you created the virtual environment!*


## Determine which Python binary is active for your shell
```
which python
```

Output should indicate that you are using the Python binary in the virtual environment:

```
$ which python
/home/youruser/yourproject/venv/bin/python
```


## Install packages into your Virtual Environment
```
python -m pip install netmiko
```


## Check packages installed in your Virtual Environment
```
python -m pip list
```


## Output installed packages to requirements file
```
python -m pip list > requirements.txt
```


## Deactivate your Virtual Environment
```
deactivate
```
