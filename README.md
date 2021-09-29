# get-wifi-passwords-from-devices
The script in this repository gets all WiFi SSIDs and the passwords stored from a device (at the moment only Windows devices are supported).
Python Version used: 3.7.3 

## Modules used
The python modules used for this script are listed below:

| Module | Description |
| ------ | ------ |
| subprocess | This module is used to run new applications or programs through Python code by creating new processes |
| re | This module provides regular expression matching operations |

### How to run the script?

To use the script run the following command on the console:

```bash
python get-wifi-passwords-from-win-devices.py
```

The Result will look something like this on the return:
```bash
========================================================================

6 WiFi SSIDs were found on this device..

{'wifi_name': 'Wifi_Unifique_88', 'password': '**here_the_password**'}
{'wifi_name': 'INFOHARD5G', 'password': '**here_the_password**'}
{'wifi_name': 'Condado_5G', 'password': '**here_the_password**'}
{'wifi_name': 'Redmi', 'password': '**here_the_password**'}
{'wifi_name': 'Reiter', 'password': '**here_the_password**'}
{'wifi_name': 'Net Virtua Ap 1032', 'password': '**here_the_password**'}

```
