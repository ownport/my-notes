* very useful if you're stuck without wireshark/gui
```
tshark -r file.pcap -V 
```
* parse tshark output data in pdml format 
```
tshark -r <pcap_file> -T pdml | python m3ua-up.py
```
m3ua-up.py script is available [m3ua-up.py](https://github.com/ownport/my-notes/blob/master/telecom/scripts/m3ua-up.py)

* select messages for one call in BSSAP trace
  - find 'setup' message by calling or called number 
  - select dlr and filter messages by this number 'sccp.slr==DLR'
  - find dlr in RLSD message
  - filter: sccp.slr==slr1||sccp.slr==slr2||sccp.dlr==slr1||scccp.dlr==slr2