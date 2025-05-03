I decided to go further into the nitty-gritty crevices of network analysis by integrating scapy.py's packet building to generate practice pcaps. The general idea is to learn more around the concepts of packets by making my own pcap instead of looking at someone else's, to be a master of my own pcaps.

Scapy has, for some time now, gained traction into cybersecurity because of the framework's ability to make completely customisable packets. While a pcap capture tool can be used to "catch" traffic like a net, scapy literally chisels a new packet to existence into the wire.   
<sub>Note: scapy is a console shell and also a python module via `import`</sub>
```
# Start the scapy shell
sudo scapy
```

I started with a [suggested guide](https://thepacketgeek.com/scapy/building-network-tools/part-05/) in scapy's doc.

```
pkt = Ether()/ARP()
pkt[ARP].hwsrc = "00:11:22:33:44:55"
pkt[ARP].pdst = "172.16.20.1"
pkt[ARP].dst = "ff:ff:ff:ff:ff:ff"
pkt
# <Ether  type=ARP |<ARP  hwsrc=00:11:22:33:44:55 pdst=172.16.20.1 |>>
```

The above code initialises a barebones arp packet.

To capture this packet into a pcap, first I make sure to isolate my VM so that other packets won't be included into the pcap (you can also just capture with a filter).  
To "isolate", remove DNS nameservers in `/etc/resolv.conf` and turn off DHCP by NetworkManager with `systemctl disable NetworkManager`. <sub>(This doesn't guarantee any other services from sending packets.)</sub>

I then use `tcpdump` to start a capture.  
`tcpdump -i eth0 -w test.pcap` <sub>(`-i` is the interface name. Use `ip a` to get your interface name.)</sub>   

After a couple seconds `Ctrl + C` and an ARP packet asking for 172.16.20.1 will be written into `test.pcap`. That right there is a custom packet, pretty cool.  

Don't forget that `scapy` is literally a python package. You can use if statements, loops, and the whole she bang. Consider making an 8 GB pcap:

```
# This will a send 15KB packet. Or rather, it's supposed **to**
b=''
while len(b) != 15000:
    b+='01'
pkt = Raw(b)
send(pkt)
```

My goal is to make an 8GB pcap, I want to send large packets through the wire because I don't want to sit here sending small byte-size (ha) packets for 4 hours until I get a 8000000000 byte pcap. So if you haven't noticed yet, scapy returns an error when sending the 15KB packet. Why? There's something called [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit), a network interface will drop sending or receiving packets that exceeds its MTU setting (by default 1500 bytes).

To set an interface's MTU I refer to this [blog](https://www.baeldung.com/linux/maximum-transmission-unit-change-size)  
I did this at a different terminal `sudo ifconfig eth0 mtu 15000 up`  
  
Now switch back to the scapy terminal and retry `send(pkt)`  
If you get a good return message, make another terminal and run a pcap capture `tcpdump -i eth0 -w test.pcap`  
Then go back to scapy and send again `send(pkt)`  

Now cancel tcpdump, look at it in wireshark or tshark or whatever, I'm not gonna hold your hand on that, but the gist of the process is that we started with a fabricated ARP packet and now with a little bit of tweaking a network interface we can write a highly irregular packet into a pcap file and view it.

while True:
    send(pkt)



Now on a different terminal tab do `ls -sh packets.txt` to monitor the size of packets.txt, the file size right now isn't going to be the pcap size because the data inside are just string representations of bytes, not actual packets.   

TODO: to readlines the packets.txt, you do eval() on each string and then pickle.loads()
When youre capturing all the packets in packets.txt, you then make a tcp packet with osaka as an image

##########
pkt = Ether()/ARP()
pkt[ARP].hwsrc = "00:11:22:33:44:55"
pkt[ARP].pdst = "0.0.0.0"
pkt[ARP].dst = "ff:ff:ff:ff:ff:ff"
pkt
# <Ether  type=ARP |<ARP  hwsrc=00:11:22:33:44:55 pdst=172.16.20.1 |>>
a,b,c,d=0,0,0,0

while True:
    sendp(pkt)
    d += 1
    if d==255:
        c+=1
        d=0
        if c==255:
            b+=1
            c=0
            if b==255:
                a+=1
                b=0
                if a==255 and d==255:
                    a,b,c,d=0,0,0,0
    pkt[ARP].pdst = f"{a}.{b}.{c}.{d}"

######
load_layer("http")

with open('00 0c 29 d5 ca 2d.jpg', 'rb') as f:
    b = f.read()
client = "10.0.0.2"
server = "10.0.0.3"
client_p = 12345
server_p = 80

http_post = (
    f"POST /upload.jpeg HTTP/1.1\r\n"
    f"Host: {server}\r\n"
    f"Content-Type: image/jpeg\r\n"
    f"Content-Length: {len(b)}\r\n"
    f"\r\n").encode()

http_post += b

http_response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: image/jpeg\r\n"
    f"Content-Length: {len(b)}\r\n"
    f"\r\n").encode()

http_response += b

seq_client = 1000
seq_server = 2000
ack_from_server = seq_client + len(http_post)

post_pkt = IP(src=client, dst=server)/TCP(sport=client_p, dport=server_p, flags="PA", seq=seq_client, ack=seq_server)/HTTP()/Raw(load=http_post)
response_pkt = IP(src=server, dst=client)/TCP(sport=server_p, dport=client_p, flags="PA", seq=seq_server, ack=ack_from_server)/HTTP()/Raw(load=http_response)

send(post_pkt)
send(response_pkt)

#######
with open('rawbytes.txt', 'rb') as f:
    b = f.read()

pkt = Raw(b)
while True:
    send(pkt)
