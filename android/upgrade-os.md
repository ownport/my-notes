# Intructions how to upgrade Android OS under Ubuntu

[Heimdall](http://www.glassechidna.com.au/products/heimdall/) is a cross-platform open-source tool suite used to flash firmware (aka ROMs) onto Samsung Galaxy S devices. 

DISCLAIMER:

This software attempts to flash your Galaxy S device. The very nature of
flashing is dangerous. As with all flashing software, Heimdall has the
potential to damage (brick) your phone if not used carefully. If you're
concerned, don't use this software. Flashing ROMs onto your phone may also
void your warranty. You are responsible for the result of your actions.

Install heimdall on Ubuntu machine
```
$ sudo add-apt-repository ppa:heimdall-packagers/heimdall
$ sudo apt-get update
$ sudo apt-get install heimdall
$ sudo apt-get install heimdall-frontend 
```

For the steps required to flash an Android ROM from Linux onto your Samsung device using Heimdall, see [THIS](https://github.com/Benjamin-Dobell/Heimdall/tree/master/Linux) page.

### Firmwares for Russia & Ukraine
```
 Russia	            2011 November	2.3.6	 I9000XWJVW ##	I9000SERJV5
 Ukraine (Kyivstar)	2011 October	2.3.3	 I9000XWJVN ##	I9000OXEJV3
```

### IMEI backup

For backup you just need to store the next files:

 - \efs\imei\bt.txt
 - \efs\imei\mps_code.dat
 - \efs\.nv2.bak
 - \efs\.nv2.bak.md5
 - \efs\.nv_data.bak
 - \efs\.nv_data.bak.md5
 - \efs\.nv_state

IMEI and region stored in ".nv_data.bak"

### Links

 - [The Heimdall source from GitHub](https://github.com/Benjamin-Dobell/Heimdall)
 - [Heimdall firmware packages for stock GT-I9000 firmwares](http://forum.xda-developers.com/showthread.php?t=1196179)
 - [CyanogenMod, Samsung Galaxy S: Full Update Guide](http://wiki.cyanogenmod.com/wiki/Samsung_Galaxy_S:_Full_Update_Guide)
 - [Samsung firmwares](http://www.sammobile.com/)
 - [Android - Прошивки](http://4pda.ru/forum/index.php?showforum=268)
 - [Samsung GT-I9000 Galaxy S - Прошивка (OS 2.3)](http://4pda.ru/forum/index.php?showtopic=222559)
 - [Acer Stock Firmware Files List (Full, Update and EUUs)](http://forum.xda-developers.com/showthread.php?t=1816560)
 
