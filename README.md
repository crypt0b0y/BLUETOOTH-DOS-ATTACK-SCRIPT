<h1 align="center">Bluetooth DOS-Attack Script</h1>
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
<p>The script works only with Linux systems. It tested on Kali Linux.</p>
<p>You must have "l2ping" util on your linux machine (it installed as default on Kali Linux).</p>

## Using
<p>First of all, you must scan network for Bluetooth devises. For example, you can use "hcitool".</p>

```
$ sudo apt update
$ apt install hcitool
$ sudo service bluetooth start
$ hcitool scan
```
<p>Output will be like:</p>

```
A1:B2:C3:D6:E7      Xiaomi portable speaker
B1:C2:D3:E4:F5      iPhone(Toivo)
C1:D2:E3:F4:G5      Some Bluetooth device
```
<p>Then you copy target addres (for example "A1:B2:C3:D6:E7") and paste it in "Target addr".</p>

## Manual

1. "Target addr" - addres of your target (Check info upper).
2. "Packages size" - size of the packages, that will be sent to the target. 600 is optimal.
3. "Threads count" - number of threads, that will send packages to the target at the same time. 50 is optimal (check table below, to understand, what number of threads you need).

## Other

<p>According to my calculations, if ping bigger than 500ms, Bluetooh device will turn off / disconnect.</p>


|  Packages size | Threads count| Ping, ms  | Distance, meters |
|:--------------:|:-----: |:----------:|:---------------------:|
|  600           | 1       | 8 - 9      |0,3|
|  600           | 10      | 37 - 38    |0,3|
|  600           | 20      | 75 - 90    |0,3|
|  600           | 50      | 180 - 200  |0,3|
|  600           | 100     | 375 - 400  |0,3|
|  600           | 200     | 750 - 800  |0,3|
|  600           | 500     | 1970 - 1975 |0,3|
|  600           | 1000    | 3370 - 3385 |0,3|
|  600           | 1000+   | Couldn't calculate  |0,3|
