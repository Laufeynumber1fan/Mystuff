# Also known as `tshark/wireshark` filters 

Misc docs:  
[What are checksums for?](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvChecksums.html)  
  
## ARP
**ARP TYPE**  
`arp.opcode` Filter arp packets based on type.  
`arp.opcode==1` are arp requests. `arp.opcode==2` are arp replies.  
More opcodes [here](https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml#arp-parameters-1)

## TCP

**TCP FLAGS**  
More flags [here](https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml#tcp-header-flags)

**TCP HANDSHAKES**  
`tcp.completeness` Filters tcp packets based on the progression of their handshake.  
For example: `tcp.completeness==7` filters packets that are transmitting **data payloads**. [ref](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html#_tcp_conversation_completeness)  
Note: The bitmask chart on the [ref](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html#_tcp_conversation_completeness) needs to be minus by one! The bitmask is 64 bits long so `tcp.completeness==0` refers to SYNs, `tcp.completeness==1` refers to SYN-ACKs, and so on.

**Why use `tcp.completeness` and not `tcp.flags`?**  
One argument is that tcp.completeness values are more sequential in the TCP handshake. Like `0` is the start and `31` is the finish. Whereas `tcp.flags` would have `2` as SYN and then `4` as RST. So unlike in `tcp.flags` you can use `>` and `<` for `tcp.completeness` and it will be a range on the handshake progression of TCP packets.  
  
**Examples `tcp.completeness`:**  
`tcp.completeness<4 && tcp.flags!=20` displays packets doing the SYN handshake but exclude any (RST, ACK) flags.  
`tcp.completeness==31` displays packets doing the FIN handshake.  

**TCP DATA PAYLOAD**  
`tcp contains ****` can be used to filter out hexdumps of TCP payloads.  
For example, consider the word "velociraptor", to look for data payloads with that word you can use `contains` filter `tcp contains "velociraptor"`

`contains` is a simplified version of tcp.payload which is used to search for hex.  

`tshark -r foo.pcap -Y tcp -T fields -e tcp.payload | grep 76656c6f6369726170746f72` is the same as `tcp contains "velociraptor` but with tcp.payload you can spot how many times the word "velociraptor" appears in a packet or the entire pcap with cmdline tools.  

  
TODO: ADD THESE  
`tcp_hdr.len` Length of the TCP header  
`tcp.len` Length of TCP payload  
`ip_hdr.len` Lenght of the IP header  
`ip.len` Size of the IP frame (including headers, loks like)  
`frame.len` Length of the on-the-wire frame (ethernet, most probably)  
`frame.cap_len` Length of the capture  