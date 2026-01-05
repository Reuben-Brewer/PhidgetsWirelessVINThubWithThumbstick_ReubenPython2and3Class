###########################

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

Software Revision H, 12/31/2025

Verified working on:

Python 3.12/13.

Windows 10/11 64-bit

Raspberry Pi Bookworm

(Might work on Mac in non-GUI mode but haven't tested)

*NOTE THAT

0. YOU MUST INSTALL Bonjour64.msi BEFORE STARTING.

1. YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.

2a. The device's red LED will be lit continously when working correctly.

2b. Low/drooping voltage from a battery can cause the red LED to be illuminated continuously but not allow proper operation.

3. Your browser and program may be able to communicate with the device even if the Phidgets Control Panel doesn't show it.

4. VMware's and Checkpoint/VPN's virtual network adapters often interfere with the device's connectivity to your computer.

5. The device's connectivity to your computer may depend upon the quality of the WiFi card (integrated vs USB-WiFi vs with large antenna or not).*

###########################

########################### Python module installation instructions, all OS's

PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class, ListOfModuleDependencies: ['Joystick2DdotDisplay_ReubenPython2and3Class', 'LowPassFilter_ReubenPython2and3Class', 'Phidget22', 'ReubenGithubCodeModulePaths']

PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['keyboard', 'MyPrint_ReubenPython2and3Class', 'ReubenGithubCodeModulePaths']

PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['numpy']

PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class, ListOfModuleDependencies_All:['Joystick2DdotDisplay_ReubenPython2and3Class', 'keyboard', 'LowPassFilter_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'Phidget22', 'ReubenGithubCodeModulePaths']

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