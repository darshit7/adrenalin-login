#!/bin/bash

#Add '. /home/username/filepath/login.sh to /home/username/.profile file

#activate environment having all required packages.
source /opt/myvirtual/testenv/bin/activate

#Path to store log files files
export AD_LOG_PATH=''

#SECRET key to hash password
#Run following code to generate random SECRET key.
#from cryptography.fernet import Fernet
#Fernet.generate_key()
export AD_SEC_KEY=''

#Hashed password string
#Run following code to generate hash of password
#cipher_suite = Fernet(SECRET)
#cipher_text = cipher_suite.encrypt(b"Your Password")
export AD_PASS_HASH=''


#URL of adrenalin.
export AD_URL=''

#Employee ID
export AD_EMP_ID=''


#run python script
python /home/username/folder/login.py

#Reset Environemtn variables.
unset AD_LOG_PATH
unset AD_SEC_KEY
unset AD_PASS_HASH
unset AD_URL
unset AD_EMP_ID

#deactivate virtual environament
deactivate
#Removed
