ISW GUI
=======

[![Logo](https://github.com/kyokenn/isw-gui/blob/master/image/isw.svg)](https://github.com/kyokenn/isw-gui/blob/master/image/isw.svg)

Ice-Sealed Wyvern. It is meant to alter fan profiles of MSI laptops.

A fork of [ISW](https://github.com/YoyPa/isw) and [ISW-Modern](https://github.com/FaridZelli/ISW-Modern) with GUI inspired by [MControlCenter](https://github.com/dmitry-s93/MControlCenter).

No building required. Depends only on [msi-ec](https://github.com/BeardOverflow/msi-ec) kernel module.
Doesn't uses acpi-ec and ec-sys kernel modules.

[![Screenshot](https://github.com/kyokenn/isw-gui/blob/master/image/screenshot.png)](https://github.com/kyokenn/isw-gui/blob/master/image/screenshot.png)


Requirements
------------

* GTK4
* Python 3.12+
* Python GObject Introspection (python3-gobject or python3-gi)
* [msi-ec](https://github.com/BeardOverflow/msi-ec)


Installation
------------

* Install [msi-ec](https://github.com/BeardOverflow/msi-ec) kernel module.

* Enable msi-ec debug mode (some features will not be available without it):
```
cp -Rfv ./etc/modprobe.d /etc/
cp -Rfv ./etc/modules-load.d /etc/
```

* Clone this git repository:
```
git clone https://github.com/kyokenn/isw-gui.git
cd isw-gui
```


Usage
-----

* Run the app from repository:
```
sudo -E ./isw-gui
```


Useful resources
----------------

* https://github.com/BeardOverflow/msi-ec
* https://github.com/dmitry-s93/MControlCenter
* https://github.com/YoyPa/isw
* https://github.com/FaridZelli/ISW-Modern
