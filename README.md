#Adrenalin Login
Python script for login to the adrenalin HRM system on system startup.
Currently this script is working on only linux device.

##Geting Started
These instructions will get you a copy of the project up and running on your local machine.

##Prerequisites
What things you need to install the software and how to install them.
We assume that you have installed pip using `sudo apt-get install python-pip` command.

##### 1. Create clone of adrenalin-login into home directory by using following command
        git clone https://github.com/darshit7/adrenalin-login

##### 2. Create virtualenv in `/opt/myvirtual/` folder and install all required packages
  Execute following commands to create virtual environment named `testenv` with all required packages.
  
        $ pip install virtualenv
        $ cd /opt
        $ mkdir myvirtual
        $ cd myvirtual
        $ virtualenv -p /usr/bin/python3.5 testenv
        $ source bin/activate
        $ pip install -r /home/adrenalin-login/requirement.txt
    
##### 3. Set credintials in script file
  To create hased equivalent of your credintials open terminal and execute following commands.
    
        $ source /opt/myvirtual/testenv/bin/activate
        $ python
        >>> from cryptography.fernet import Fernet
        >>> SECRET = Fernet.generate_key()
        >>> SECRET
  Copy generated key and assigned it to the AD_SEC_KEY value in login.sh file of adrenalin-login folder
    
        >>> cipher_suite = Fernet(SECRET)
        >>> cipher_text = cipher_suite.encrypt(b"Your Password")

  Copy hased password and assigned it to AD_PASS_HASH value in login.sh file of adrenalin-login folder

  Set URL of adrenalin host server to AD_URL in login.sh file of adrenalin-login folder

  Set youe employee id to AD_EMP_ID in login.sh file of adrenalin-login folder

  If you want to store your log at specific folder define path to AD_LOG_PATH variable in login.sh file else by default it will store in /home/username folder.

##### 4. Add command to run login.sh in /home/username/.profile name
  Open .profile file by executing `nano /home/username/.profile` in terminal window and add following line at the end of file
        
        . /home/username/adrenalin-login/login.sh

##### 5. Change permission of adrenalin-login folder so other user can't see your credintials
        
        $ chmod o-rwx adrenalin-login
        $ cd adrenalin-login
        $ chmod o-rwx login.sh
        $ chmod o-rwx login.py

#Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull request to us.
I whould appriciate if some make it avaiable for windows and mac system.

#Authors
- Darshit Patoliya
See also the list of contributors who participated in this project.

#License
This project is licensed unser the MIT License- see the [LICENSE.md](https://github.com/darshit7/adrenalin-login/blob/master/LICENSE) file for details
