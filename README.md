<h1 align="center" size="10px">Bluetooth DOS-Attack Script</h1>
<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/pypi/pyversions/Django.svg">
  </a>
</p>
<p align="center">Script for quick and easy DOS-attacks on bluetooth devices for pentest purposes</p>

## Disclaimer
<p align="center">This project was created only for good purposes and personal use.</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.
## Installing

```
$ sudo apt update
$ sudo apt install python3
$ sudo git clone https://github.com/jieggiI/BLUETOOTH-DOS-ATTACK-SCRIPT.git
$ cd Bluetooth-DOS-attack-script
$ python3 Bluetooth-DOS-Attack.py
```
### Note
<p>The script works only with Linux systems. It tested on Kali Linux</p>
<p>You must have "l2ping" util on your linux machine (it installed as default on Kali Linux)</p>

## Using
<p>First of all, you must scan network for Bluetooth devises. For example, you can use hcitool</p>
```
$ apt install hcitool
$ sudo service bluetooth start
$ hcitool scan
```

