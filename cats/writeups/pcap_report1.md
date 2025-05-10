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

I first looked for any odd tcp packets. `tshark -r random_dooky.pcapng -Y tcp -T fields -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport`  

```
26305   192.168.184.131 192.168.184.136 35095   1234
26306   192.168.184.131 192.168.184.254 35095   6547
26307   192.168.184.131 192.168.184.1   35095   6646
26308   192.168.184.131 192.168.184.136 35095   9535
26309   192.168.184.131 192.168.184.254 35095   888
26310   192.168.184.131 192.168.184.136 35093   7435
26311   192.168.184.131 192.168.184.254 35093   34571
26312   192.168.184.131 192.168.184.1   35093   50002
26313   192.168.184.131 192.168.184.133 35093   981
26314   192.168.184.131 192.168.184.135 35093   1002
26315   192.168.184.131 192.168.184.136 35095   8400
26316   192.168.184.131 192.168.184.135 35093   6106
26317   192.168.184.131 192.168.184.136 35093   990
26318   192.168.184.131 192.168.184.254 35093   2869
26319   192.168.184.131 192.168.184.1   35093   8290
26320   192.168.184.131 192.168.184.133 35093   1002
26321   192.168.184.131 192.168.184.135 35093   6059
```

I then find this weird pattern by 192.168.184.131.

I investigate further:
`tshark -r random_dooky.pcapng -Y "ip.addr==192.168.184.131 and tcp.srcport==35093" | less`

```
18016 902.217684308 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 143 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18018 902.217684354 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 3306 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18026 902.221007860 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 445 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18028 902.221007952 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 22 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18030 902.221007988 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 554 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18032 902.221008022 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 139 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18038 902.221056945 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 113 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18040 902.221056991 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 995 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
18042 902.221057023 192.168.184.131 → 192.168.184.137 TCP 60  35093 → 80 [FIN, PSH, URG] Seq=1 Win=1024 Urg=0 Len=0
```
They're all FIN packets. So this is probably done with nmap using `-sF`
I look at all the packets done by source ip 192.168.184.131

SYN, TCP null, and FIN scans to 192.168.184.1, .132, .133, .135, .136, .137, .254

6. Was there any malicious activity? What was the name of the malicious file? What time did the file first appear and last appear? What was the tool used called? What happened?

To look at files
`tshark -r random_dooky.pcapng -Y "tcp.completeness==7" -T fields -e http.request.uri -e tcp.stream | less`

This file was downloaded
notapad.exe application/x-msdos-program tcp.stream 55093 useragent:wget

I looked at t
`tshark -r random_dooky.pcapng -qz follow,tcp,ascii,55093 | less`

Another malicious file that's probably trying to be downloaded was Zooktor.exe

7. What IPs tried to download Zooktor.exe? What were their user agents? What is the MD5 hash of Zooktor.exe? Is Zooktor.exe malicious?
`tshark -r random_dooky.pcapng -Y "tcp.completeness==7" -T fields -e ip.src -e ip.dst -e http.request.uri -e tcp.stream | less`

192.164.184.134, .137

I would've been able to get the hash of zooktor.exe if it was actually downloaded.

8. What IPs were hosting HTTP servers? 

`tshark -r random_dooky.pcapng -Y "tcp.port==80||tcp.port==443" | less`
192.168.184.132 is the only http server. The rest are scans

9. What were the top 5 ports used and the least 5 ports?
`tshark -r random_dooky.pcapng -Y "tcp" -T fields -e tcp.port | tr "," "\n" | tr "\t" "\n" | sort -n | uniq -c | sort -n`
```
6002 64717
8423 8889
8999 35093
9039 44850
9998 64715
```
`tshark -r random_dooky.pcapng -Y "tcp" -T fields -e tcp.port | tr "," "\n" | tr "\t" "\n" | sort -n | uniq -c | sort -nr`
```
1 32818
1 32806
1 32802
1 32800
1 32798
1 32792
```
For UDP  
`tshark -r random_dooky.pcapng -Y "udp" -T fields -e udp.port | tr "," "\n" | tr "\t" "\n" | sort -n | uniq -c | sort -n`
```
646 138
848 1900
1000 137
1294 5353
11567 53
```
`tshark -r random_dooky.pcapng -Y "udp" -T fields -e udp.port | tr "," "\n" | tr "\t" "\n" | sort -n | uniq -c | sort -nr`
```
1 32882
1 32870
1 32697
1 28531
1 1434
```
10. What types of authentication were used?

I look at tcp.completeness to ignore scans.
`tshark -r random_dooky.pcapng -Y "tcp.completeness==7" | less -S`
smbnetlogon, kerberos, ldap

11. List any IOCs
High amount of login attempts, port scanning with FIN, TCP null, and SYN scans, Attempted download of malicious velociraptor files (tcp.stream==24361) 
 
