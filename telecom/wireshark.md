very useful if you're stuck without wireshark/gui
```sh
tshark -r file.pcap -V 
```


parse tshark output data in pdml format 
```sh
tshark -r <pcap_file> -T pdml | python m3ua-up.py
```
m3ua-up.py script is available [m3ua-up.py](https://github.com/ownport/my-notes/blob/master/telecom/scripts/m3ua-up.py)

