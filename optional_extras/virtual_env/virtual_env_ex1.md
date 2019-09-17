# Virtual Environments Exercise 1

1. Make a mock project directory "myproject" in your home directory:

   `cd ~ && mkdir myproject`

2. cd into this myproject directory

    `cd myproject`

3. Exit your current virtualenv using the "deactivate" command.
  - *Note*: Upon login to the lab host a virtual environment for your user is automatically activated, so we need to "deactivate" to get "out" of this virtual environment.

4. Create a new virtual environment named 'venv'

    `python -m venv`

5. Activate that virtual environment using:

    `source venv/bin/activate`

6. Execute the `pip list` command to make sure you have a blank virtual environment.

7. Use `pip install netmiko` to reinstall the netmiko library.

8. View `pip list` again to see what is now installed.

9. Optionally export the packages installed in your virtual environment to a `requirements.txt` file. This file could be shared with others so that they are able to reproduce your virtual environment.

    `pip list > requirements.txt`
