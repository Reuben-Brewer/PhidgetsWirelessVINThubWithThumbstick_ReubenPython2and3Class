########################

PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) for reading a 2-axis thumbstick over a Wireless VINT Hub.
Great for wireless hand-controller.

From Phidgets' website:
"The Wireless VINT Hub is a simple way to use Phidgets in locations away from a
computer by making them available on your local network via the Phidget Network Server.
The HUB5000 requires a local WiFi signal and a power supply.
You can also wire it directly into your modem or network switch using an ethernet cable.

The Thumbstick Phidget provides a familiar 2-axis thumbstick similar to those on a video game controller.
The stick springs back to the neutral position when released. It can also be pressed down with a click,
which will register in software and can be tied to a function in your software.
This Phidget connects to your computer through a VINT Hub."

Wireless VINT Hub
ID: HUB5000_0
https://www.phidgets.com/?tier=3&catid=2&pcid=1&prodid=1143

Coupled with

Thumbstick Phidget
ID: HIN1100_0
https://www.phidgets.com/?&prodid=962

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision C, 05/21/2022

Verified working on: 
Python 2.7, 3.8.
Windows 8.1, 10 64-bit
Raspberry Pi Buster 
(no Mac testing yet)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

########################  

########################### Python module installation instructions, all OS's

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22
 
###########################