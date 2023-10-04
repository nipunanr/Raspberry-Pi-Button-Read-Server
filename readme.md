# Orange Pi Button Script Autostart

This guide explains how to set up a systemd service to run a Python script on Orange Pi startup.

## Prerequisites

- Orange Pi running a compatible OS (e.g., Orange Pi OS).
- Basic knowledge of working with the terminal.

SSH Credentials
User : root
Password : orangepi

## Steps


###### Increase Watch limit

    sudo nano /etc/sysctl.conf

Add this line to the end of the file.

    fs.inotify.max_user_watches=524288

The new value can then be loaded in by running

    sudo sysctl -p

###### Install PIP

Enter the following command to update Linux:

    sudo apt update

Enter the following command to install pip3:

    sudo apt install python3-pip

###### Install Setuptools

Enter the following command to install setuptools:

    sudo pip3 install setuptools


###### Install flask

Enter the following command to install flask:

    sudo pip3 install flask


###### Install OPi.GPIO

Enter the following command to install OPi.GPIO:

    sudo pip3 install --upgrade OPi.GPIO

    More Info @ https://opi-gpio.readthedocs.io/en/latest/install.html


###### Copy Script
Copy button_script.py script from Repository to /home directory

Check for Working Script

    python3 /home/button_script.py
###### Autorun Script

Copy the python file to /bin:

    sudo cp -i /home/button_script.py /bin

Add A New Cron Job:

    sudo crontab -e

Scroll to the bottom and add the following line (after all the #'s):

    @reboot python3 /bin/button_script.py &

    The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up.

###### Setup Network

- Use  Command  "sudo orangepi-config"  to  connect  to  Wifi  and  access  settings

- Use  Command  "nmtui"  to  setup IP Addresses
 (http://www.orangepi.org/orangepiwiki/index.php/How_to_set_a_static_IP_address)

-  `/etc/network/interfaces.d/wlan0`  ---->  WiFi  Static  IP  Settings  
-  `/etc/network/interfaces.d/eth0`  ---->  Ethernet  Static  IP  Settings  


###### Test it:

    sudo reboot

## Conclusion

Your `button_script.py` should now run automatically on startup of your Raspberry Pi. Remember to replace the paths and user details with the correct values based on your setup.

Feel free to modify and improve this setup according to your specific requirements.
