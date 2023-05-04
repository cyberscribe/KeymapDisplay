# Keymap Display
Displays full-screen images controlled by keyboard keys

# Intended Use
This programme is designed to be run on any device connected to a monitor to provide a full-screen display of images that can be changed by pressing keyboard keys.

# Installation
Download or clone the KeymapDisplay folder and run:
`python display.py`

[![Installation Video](https://i.ytimg.com/vi/DWCE5fD66hU/hqdefault.jpg)](https://www.youtube.com/watch?v=DWCE5fD66hU)

# Configuration
The mappings of keys to images is configurable using the `config.ini` file. Images can be placed in the `images/` folder.

# Use on a Raspberry Pi as a Dedicated Appliance
The motivating use case for this programme was to connect a Raspberry Pi to a backstage monitor and, via a configurable keypad (or key encoder with wired buttons) connected to the Pi via long USB cable, be able to display images with different messages on the backstage monitor from the control room.

In order to accomplish this:

 1. The Raspberry Pi must be configured to automatically log in (this is the default on some installations, otherwise use `raspi-config`)
 2. The Raspberry Pi must be configured to run the programme when it starts up (there are various [options](https://raspberrypi-guide.github.io/programming/run-script-on-boot))
 3. (Optionally) A shutdown button can be installed on the GPIO pins to allow shutdown without further keyboard/mouse control (one [option](https://gist.github.com/traumverloren/734839dbe8cd7e4865baddcff970b278))
