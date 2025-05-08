192.168.184.1 is the router  
192.168.184.132 is infected host
192.168.184.134 is prob infected host
192.168.184.135 is prob C2 server  
192.168.184.137 is prob DNS server


Weird interaction with 192.168.184.132 -> 192.168.184.131 where it's been trying to send tcp (RST, ACK) packets for 3700 secs.

1. Use a helpful Linux command to find the size of the pcap and number of packets  

`capinfos random_dooky.pcapng`  

```
File size = 42MB  
Number of packets = 100186  
```

2. How many computers are connected to network, what are their IPs and hostnames?

`tshark -r random_dooky.pcapng -Y ip -T fields -e ip.src -e ip.dst | tr '\t' '\n' | sort -T . | uniq | wc -l`  
20

`tshark -r random_dooky.pcapng -Y ip -T fields -e ip.src -e ip.dst | tr '\t' '\n' | sort -T . | uniq`
```
0.0.0.0
192.168.184.1
192.168.184.1,192.168.184.131
192.168.184.1,192.168.184.137
192.168.184.131
192.168.184.131,192.168.184.1
192.168.184.132
192.168.184.133
192.168.184.134
192.168.184.135
192.168.184.136
192.168.184.137
192.168.184.137,192.168.184.1
192.168.184.254
192.168.184.255
224.0.0.22
224.0.0.251
224.0.0.252
239.255.255.250
255.255.255.255
```

`tshark -r random_dooky.pcapng -Y ip -T fields -e ip.host -N dmn | tr ',' '\n' | sort -T . | uniq`
```
0.0.0.0
192.168.184.1
192.168.184.131
...
bobbyeverything.local
DESKTOP-2V2Q1Q2.local
DESKTOP-BMNULR4.local
DESKTOP-NA0VSP4.local
WIN-GBB5Q7HQED8.local
```

3. What does the text file say that was passed using HTTP? (don't use wireshark)
First I did this to look for tcp payloads with a .txt name
`tshark -r random_dooky.pcapng -Y tcp.completeness==7 | grep ".txt"`  
```
40486 2992.429423669 192.168.184.134 → 192.168.184.132 HTTP 561  GET /Desktop/true.txt HTTP/1.1 
40536 3001.300285651 192.168.184.134 → 192.168.184.132 HTTP 611  GET /Desktop/true.txt HTTP/1.1 
41262 3171.791305966 192.168.184.137 → 192.168.184.132 HTTP 217  GET /Desktop/true.txt HTTP/1.1 
79611 3927.860089306 192.168.184.131 → 192.168.184.136 HTTP 234  GET /robots.txt HTTP/1.1 
```

I want to then look for the tcp stream to follow so I added `-T` fields
`tshark -r random_dooky.pcapng -Y tcp.completeness==7 -T fields -e http.request.uri -e tcp.stream | grep .txt`
```
/Desktop/true.txt       24386
/Desktop/true.txt       24388
/Desktop/true.txt       24408
/robots.txt     54620
```

Then I look at the tcp stream
`tshark -r random_dooky.pcapng -qz follow,tcp,ascii,24386`
Alex is better at python than Dylan K

4. Is there a DC on the network if so what is the Domain name? 
192.168.184.136 is prob the DC. WIN-GBB5Q7HQED8.local is the resolved name

Reasons:
I looked for hosts using LDAP. 
`tshark -r random_dooky.pcapng -Y "ldap"`
Found 192.168.184.136 responding

I then look at that ip, I used grep because it highlights the actual ip.
`tshark -r random_dooky.pcapng -Y "ip" | grep 192.168.184.136`
I see it also using SMB netlogon so it is definitely the DC.

`-N dmn` to resolve the name.

How many login attempts were made? Was I successful?

I checked the smbnetlogon packets
`tshark -r random_dooky.pcapng -Y "smb_netlogon"`
And it seems that there is repeated attempts to login

`tshark -r random_dooky.pcapng -Y "smb_netlogon and ip.dst==192.168.184.136" | wc -l`
105

No you were not successful. There were no packets that showed a success login
Checked this by switching to src. `tshark -r random_dooky.pcapng -Y "smb_netlogon and ip.src==192.168.184.136"`


5. Was there any network scans? What tools were used? How many scans were there? What types of scans were done?

6. Was there any malicious activity? What was the name of the malicious file? What time did the file first appear and last appear? What was the tool used called? What happened?

7. What IPs tried to download Zooktor.exe? What were their user agents? What is the MD5 hash of Zooktor.exe? Is Zooktor.exe malicious?

8. What IPs were hosting HTTP servers?

9. What were the top 5 ports used and the least 5 ports?

10. hat types of authentication were used?

List all connections

11. List any IOCs

 
