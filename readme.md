# Raspberry Pi Button Script Autostart

This guide explains how to set up a systemd service to run a Python script on Raspberry Pi startup.

## Prerequisites

- Raspberry Pi running a compatible OS (e.g., Raspberry Pi OS).
- Basic knowledge of working with the terminal.

## Steps

1. **Create a systemd Service File**:

    Open a terminal on your Raspberry Pi and create a new systemd service file using a text editor (e.g., nano):

    ```bash
    sudo nano /etc/systemd/system/button_script.service
    ```

    Add the following content to the file:

    ```plaintext
    [Unit]
    Description=Button Script Service
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /home/pi/button_script.py
    WorkingDirectory=/home/pi
    StandardOutput=inherit
    StandardError=inherit
    Restart=always
    User=pi

    [Install]
    WantedBy=multi-user.target
    ```

    Make sure to adjust the `ExecStart` line to the correct path of your Python script and the `User` field if you're not using the default "pi" user.

2. **Save and Close the File**:

    For example, in nano, press `Ctrl + O` to save the file, and then press `Enter`. Then press `Ctrl + X` to exit the text editor.

3. **Enable and Start the systemd Service**:

    Run the following commands to enable and start your new systemd service:

    ```bash
    sudo systemctl enable button_script.service
    sudo systemctl start button_script.service
    ```

    This will make the service start automatically on boot and will start it immediately.

4. **Check the Status of the Service (Optional)**:

    You can check the status of the service to ensure it's running correctly:

    ```bash
    sudo systemctl status button_script.service
    ```

## Conclusion

Your `button_script.py` should now run automatically on startup of your Raspberry Pi. Remember to replace the paths and user details with the correct values based on your setup.

Feel free to modify and improve this setup according to your specific requirements.
