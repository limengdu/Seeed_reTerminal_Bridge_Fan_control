# Seeed_reTerminal_Bridge_Fan_control

![](https://files.seeedstudio.com/wiki/reTerminal_Bridge/reTerminal_bridge.jpg)
 
Example Python code for using fan on reTerminal Bridge.

Install the python3 library.

```sh
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo pip3 install RPi.GPIO
$ sudo apt-get install python3-serial
```

We can directly control the fan switch by the following command.

```sh
fan on
$ raspi-gpio set 23 op pn dh

fan off
$ raspi-gpio set 23 op pn dl
```

We can also enable and disable the fan by detecting the temperature of the CPU. Please follow the steps below to download and run the program.

```sh
$ git clone https://github.com/limengdu/Seeed_reTerminal_Bridge_Fan_control.git
$ cd Seeed_reTerminal_Bridge_Fan_control.git
$ sudo python3 fan.py
```

After the code runs successfully, when the CPU temperature is detected to be higher than 40°C, the fan will be turned on. When the temperature is lower than 20°C, the fan will be turned off.

## Getting Started

- [reTerminal Bridge wiki]()

