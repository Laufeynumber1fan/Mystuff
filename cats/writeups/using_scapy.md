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

Let's then use `tcpdump` to start a capture.  
`tcpdump -i eth0 -w test.pcap` <sub>(`-i` is the interface name. Use `ip a` to get your interface name.)</sub>   

After a couple seconds `Ctrl + C` and an ARP packet asking for 172.16.20.1 will be written into `test.pcap`. That right there is a custom packet, pretty cool.  

Don't forget that `scapy` is literally a python package. You can use if statements, loops, and the whole she bang. Consider making a trash packet with just 15kb worth of garbage:

```
# This will a send 15KB packet. Or rather, it's supposed **to**
b=''
while len(b) != 15000:
    b+='01'
pkt = Raw(b)
send(pkt)
```

Our goal is to make a very big packet, but if you haven't noticed yet, **scapy returns an error** when sending the packet. Why? There's something called [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit), a network interface will drop sending or receiving packets that exceeds its MTU setting (by default 1500 bytes).

To set an interface's MTU, refer to this [blog](https://www.baeldung.com/linux/maximum-transmission-unit-change-size)  
Do this at a different terminal `sudo ifconfig eth0 mtu 15000 up`  
  
Now switch back to the scapy terminal and retry `send(pkt)`  
If you get a good return message, make another terminal and run a pcap capture `tcpdump -i eth0 -w test.pcap`  
Then go back to scapy and send again `send(pkt)`  

Cancel tcpdump and look at it in wireshark or tshark or whatever, I'm not gonna hold your hand on that, but the gist of the process is that we started with a fabricated ARP packet and now with a little bit of tweaking a network interface we can write a highly irregular packet into a pcap file and view it.

Let's learn to make a more advanced custom packet. Making an http connection between a client and server, the beauty of scapy is that we can simulate fake traffic between two machines by just editing the source & dest IPs and MACs. I'm not gonna go into too much scrutiny with making "proper" packets because I am making fake traffic just for myself, however there are scenarious such as MITM attacks using scapy where disguising custom packets into geniune traffic come into play.  

For now let's just pay attention into making a packet that's readable in wireshark instead of trying to fool an IDS.  

```
# Layer 3
client = "10.0.0.2"
server = "10.0.0.3"

# Layer 4
client_p = 12345
server_p = 80
seq_client = 1000
seq_server = 2000
ack_from_server = seq_client + len(http_post)

# Layer 7, payload data
with open('image.jpeg', 'rb') as f:
    b = f.read()
load_layer("http")
```

Now let's build a barebones HTTP get and reply.

```
http_get = (
    f"GET /upload.jpeg HTTP/1.1\r\n"
    f"Host: {server}\r\n"
    f"Content-Type: image/jpeg\r\n"
    f"\r\n").encode()

http_reply = (
    f"HTTP/1.1 200 OK\r\n"
    f"Content-Type: image/jpeg\r\n"
    f"Content-Length: {len(b)}\r\n"
    f"\r\n").encode()

# Add image bytes into the reply
http_reply += b
```

Now normally you would need a machine to be an http client and you need another to be an http server, but if you go down a level of abstraction, all those HTTP clients and server applications' main purpose is to send something like these 2 http headers down a wire.

Time to use scapy's framework to package these fields into actual packets for transit.

```
get_pkt = IP(src=client, dst=server)/TCP(sport=client_p, dport=server_p, flags="A", seq=seq_client, ack=seq_server)/HTTP()/Raw(load=http_get)
reply_pkt = IP(src=server, dst=client)/TCP(sport=server_p, dport=client_p, flags="A", seq=seq_server, ack=ack_from_server)/HTTP()/Raw(load=http_reply)
```

Then test for errors for send.
```
send(get_pkt)
send(reply_pkt)
```

The reason how wireshark or any other analysis tool will recognise that `reply_pkt` is responding to `get_pkt` is because of the IP in layer 3, then the matching ports in layer 4, and then the sequence numbers in TCP. All this information work in tandem which we added into our custom packets.  

If the packets were able to be sent, get tcpdump again on another terminal to capture.  
`tcpdump -i eth0 http_test.pcap`

To see if the image was correctly use wireshark. `File` > `Export Objects` > `HTTP`
  
And that's that. This is not essentially a tutorial, but more like an introduction to the scope of customisable packets. For further reading into scapy I recommend these more in-depth (and more reputable) tutorials.
  
[How to Inject Code into HTTP Responses in the Network in Python](https://thepythoncode.com/article/injecting-code-to-html-in-a-network-scapy-python?utm_source=chatgpt.com)  
[How to Build an ARP Spoofer in Python using Scapy](https://thepythoncode.com/article/building-arp-spoofer-using-scapy)  