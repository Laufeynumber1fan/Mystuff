TODO: Redo datagrams in 32bit intervals like in [RFC793](https://datatracker.ietf.org/doc/html/rfc793#section-3.1)
or like wireshark 16bit  

## [Address Resolution Protocol](https://datatracker.ietf.org/doc/html/rfc6747#section-2.1) <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark.ico> `arp` <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/tcpdump.ico> `arp`
<table>
    <thead align=center>
        <tr>
            <th colspan=10>0</th>
            <th colspan=10>1</th>
            <th colspan=10>2</th>
            <th colspan=2>3</th>
        </tr>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
            <th>16</th>
            <th>17</th>
            <th>18</th>
            <th>19</th>
            <th>20</th>
            <th>21</th>
            <th>22</th>
            <th>23</th>
            <th>24</th>
            <th>25</th>
            <th>26</th>
            <th>27</th>
            <th>28</th>
            <th>29</th>
            <th>30</th>
            <th>31</th>
        </tr>
    </thead>
    <tbody align=center>  
        <tr>
            <td colspan=16>Hardware Type<br><a href=https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml#arp-parameters-2>arp.hw.type</a><br>.hwtype<sup>⟩𝑆</sup></td>
            <td colspan=16>Protocol Type<br><a href=https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml#ieee-802-numbers-1>arp.proto.type<sup>[1]</sup></a><br>.pytype<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=8>Hardware Access Length<br>arp.hw.size<sup>[2]</sup><br>.hwlen<sup>⟩𝑆</sup></td>
            <td colspan=8>Protocol Address Length<br>arp.proto.size<sup>[3]</sup><br>.plen<sup>⟩𝑆</sup></td>
            <td colspan=16>Opcode<br><a href=https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml#arp-parameters-1>arp.opcode</a><br>.plen<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=32>Sender Hardware Address<br>arp.src.hw<br>arp and ether src host<br>.hwsrc<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=16>Sender Hardware Address cont.<br>arp.src.hw<br>arp and ether src host<br>.hwsrc<sup>⟩𝑆</sup></td>
            <td colspan=16>Sender IPv4 Address<br>arp.src.proto_ipv4<br>arp src host<br>.psrc<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=16>Sender IPv4 Address cont.<sup>[4]</sup><br>arp.src.proto_ipv4<br>arp src host<br>.psrc<sup>⟩𝑆</sup></td>
            <td colspan=16>Target Hardware Address<br>arp.dst.hw<br>arp and ether dst host<br>.hwdst<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=32>Target Hardware Address cont.<br>arp.dst.hw<br>arp and ether dst host<br>.hwdst<sup>⟩𝑆</sup></td>
        </tr>
        <tr>
            <td colspan=32>Target IPv4 Address<sup>[4]</sup><br>arp.dst.proto_ipv4<br>arp dst host<br>.pdst<sup>⟩𝑆</sup></td>
    </tbody>
</table>

⟩𝑆 = Scapy header field.  
  
[1]: IPv4 type for example is 0x800.  
[2]: A.K.A Hardware Size. `Sender` and `Target Hardware Address` has a variable size depending on the network technology so `Hardware Access Length` specifies the size, For ex. Ethernet MAC Addresses is `arp.hw.size==6`  
[3]: A.K.A. Protocol Size. IPv4 addresses for example is 4.  
[4]: After both IPv4 fields there's actually a field called `Node Identifier` for Sender and Target. This is used in a proposed protocol called [Identifier-Locator Network Protocol](https://en.wikipedia.org/wiki/Identifier-Locator_Network_Protocol).

## [Domain Name System](https://datatracker.ietf.org/doc/html/rfc1035) <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark.ico> `dns` <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/tcpdump.ico> `port 53`
<table>
    <thead align=center>
        <tr>
            <th colspan=16><a href=https://datatracker.ietf.org/doc/html/rfc1035#section-3.2.1>DNS Header</a></td>
        </tr>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
        </tr>
    </thead>
    <tbody align=center>  
        <tr>
            <td colspan=16>Transaction ID<br>dns.id</td>
        </tr>  
        <tr>
            <td colspan=16>Flags<br>dns.flags.*<sup>[1]</sup></td>
        </tr>
        <tr>
            <td colspan=16>Questions Count<br>dns.count.queries</td>
        </tr>
        <tr>
            <td colspan=16>Answers Count<br>dns.count.answers</td>
        </tr>
        <tr>
            <td colspan=16>Authority Count<br>dns.count.auth_rr</td>
        </tr>
        <tr>
            <td colspan=16>Additional Count<br>dns.count.add_rr</td>
        </tr>
    </tbody>
</table>

[1]: `dns.flags.response==0` for queries, `dns.flags.response==1` for replies. Check [wireshark reference](https://www.wireshark.org/docs/dfref/d/dns.html).

<table>
    <thead align=center>
        <tr>
            <th colspan=16><a href=https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.2>DNS Query</a></td>
        </tr>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
        </tr>
    </thead>
    <tbody align=center>  
        <tr>
            <td colspan=16>Question Name<br>dns.id</td>
        </tr>  
        <tr>
            <td colspan=16>Question Type<sup>[1]</sup><br>dns.qry.name</td>
        </tr>
        <tr>
            <td colspan=16>Class Code<sup>[2]</sup><br>dns.qry.class</td>
        </tr>
    </tbody>
</table>

[1]: Types of RR like A, AAAA, MX, CNAME, etc...  
[2]: Will most usually be `IN` for internet.  

<table>
    <thead align=center>
        <tr>
            <th colspan=16><a href=https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.3>DNS Resource Record (RR)</a></td>
        </tr>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
        </tr>
    </thead>
    <tbody align=center>  
        <tr>
            <td colspan=16>Response Name<br>dns.resp.name</td>
        </tr>
        <tr>
            <td colspan=16>Response Type<br>dns.resp.type</td>
        </tr>
        <tr>
            <td colspan=16>Response Class<br>dns.resp.class<sup>[1]</sup></td>
        </tr>
        <tr>
            <td colspan=16>Time To Live<br>dns.resp.ttl</td>
        </tr>
        <tr>
            <td colspan=16>Record Length<br>dns.resp.len</td>
        </tr>
        <tr>
            <td colspan=16>Record Type<br>dns.resp.type</td>
        </tr>
        <tr>
            <td colspan=16>Data<br>dns.*<sup>[2]</sup></td>
        </tr>
    </tbody>
</table>

[1]: Will most usually be `IN` for internet.  
[2]: The value of the filter will depend on the Record Type. For ex. an A record would be `dns.a==x.x.x.x`, a PTR record would be `dns.ptr.domain_name==google.com`. Check [wireshark reference](https://www.wireshark.org/docs/dfref/d/dns.html).  
  
## [HTTP](https://en.wikipedia.org/wiki/HTTP) TODO
TODO

## [Internet Protocol](https://datatracker.ietf.org/doc/html/rfc791#section-3.1) <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark.ico> `ip` <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/tcpdump.ico> `ip`
<table>
    <thead align=center>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
            <th>16</th>
            <th>17</th>
            <th>18</th>
            <th>19</th>
            <th>20</th>
            <th>21</th>
            <th>22</th>
            <th>23</th>
            <th>24</th>
            <th>25</th>
            <th>26</th>
            <th>27</th>
            <th>28</th>
            <th>29</th>
            <th>30</th>
            <th>31</th>
        </tr>
    </thead>
    <tbody align=center>  
        <tr>
            <td colspan=4>Version<br><a href="https://www.iana.org/assignments/version-numbers/version-numbers.xhtml#version-numbers-1">ip.version</a><br>ip || ip6</td>
            <td colspan=4>Internet Header Length<sup>[1]</sup><br>ip.hdr_len</td>
            <td colspan=8>Differentiated Services<br>ip.dsfield</td>
            <td colspan=16>Total Length<sup>[1]</sup><br>ip.len</td>
        </tr>
        <tr>
            <td colspan=16>Identification<br>ip.id</td>
            <td colspan=3>Flags<br>ip.flags<sup>[2]</sup></td>
            <td colspan=13>Fragment Offset</td>
        </tr>
        <tr>
            <td colspan=8>Time to Live<br>ip.ttl</td>
            <td colspan=8>Protocol<br>ip.proto<br>proto<sup>[3]</sup></td>
            <td colspan=16>Header Checksum<br>ip.checksum<sup>[4]</sup>
        </tr>
        <tr>
            <td colspan=32>Source Address<br>ip.src<sup> ip.src_host</sup><br>ip src host</td>
        </tr>
        <tr>
            <td colspan=32>Destination Address<br>ip.dst<sup> ip.dst_host</sup><br>ip dst host</td>
        </tr>
        <tr>
            <td colspan=24><a href=https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml>Options</a><br>ip.opt.*<sup>[5]</sup></td>
            <td colspan=8>Padding<sup>[6]</sup></td>
        </tr>
    </tbody>
</table>

[1]: `IHL` specifies the length of IP header in bytes. `Total Length` specifies the length of the IP packet's header + data. A TCP packet for example could be in the IP payload and may have a TCP payload of variable length, `Total Length` determines the end of the TCP packet and start reading the next frame/packet.  
[2]: There are only 4 flags, see in [wireshark reference](https://www.wireshark.org/docs/dfref/i/ip.html).  
[3]: Possible protocols: **ether**, link, wlan, **ip**, ip6, arp, **tcp**, **udp**, sctp, iso, isis, rarp, decnet, fddi, tr, ppp and slip.  
[4]: There are some advanced checksum flags, see in [wireshark reference](https://www.wireshark.org/docs/dfref/i/ip.html).  
[5]: There are a lot of IP options, refer to other sources ([1](https://www.wireshark.org/docs/dfref/i/ip.html), [2](https://datatracker.ietf.org/doc/html/rfc791#section-3.1)).  
[6]: Options is variable length so padding is added to make sure the packet is disivisble by 32 bits.


## [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure) [Layer 3]
TODO
  
## [Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc9293#name-header-format) [Layer 4] <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark.ico> `tcp` <img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/tcpdump.ico> `tcp`
<table>
    <thead align=center>
        <tr>
            <th>00</th>
            <th>01</th>
            <th>02</th>
            <th>03</th>
            <th>04</th>
            <th>05</th>
            <th>06</th>
            <th>07</th>
            <th>08</th>
            <th>09</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
            <th>16</th>
            <th>17</th>
            <th>18</th>
            <th>19</th>
            <th>20</th>
            <th>21</th>
            <th>22</th>
            <th>23</th>
            <th>24</th>
            <th>25</th>
            <th>26</th>
            <th>27</th>
            <th>28</th>
            <th>29</th>
            <th>30</th>
            <th>31</th>
        </tr>
    </thead>
    <tbody align=center>
        <tr>
            <td colspan=16>Source Port<br>tcp.srcport<br>tcp src port</td>
            <td colspan=16>Dst Port<br>tcp.dstport<br>tcp dst port</td>
        </tr>
        <tr>
            <td colspan=32>Sequence Number<br>tcp.seq<sup>tcp.seq_raw</td>
        </tr>
        <tr>
            <td colspan=4><a href="https://datatracker.ietf.org/doc/html/rfc9293#section-3.1-6.10">Data Offset</a></td>
            <td colspan=4><a href="https://datatracker.ietf.org/doc/html/rfc9293#section-3.1-6.11">Reserved</a></td>
            <td colspan=8><a href="https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml#tcp-header-flags">Flags</a><br>tcp.flags<sup>[1]</sup><br><a href=https://www.tcpdump.org/manpages/pcap-filter.7.html#lbAG>tcp-(syn || ack...)</a></td>
            <td colspan=16>Window<br>tcp.window_size</td>
        </tr>
        <tr>
            <td colspan=16>Checksum<br>tcp.checksum<br></td>
            <td colspan=16>Urgent Pointer<br>tcp.urgent_pointer</td>
        </tr>
        <tr>
            <td colspan=32>Options<br>tcp.options.*<sup> [2]</sup</td>
        </tr>
        <tr>
            <td colspan=32>Data<br>tcp.len<sup>[3] tcp contains[4] tcp.payload[5]</sup></td>
    </tbody>
</table>
  
[1]: `tcp.flags` filter can use the bitmap based on the [iana chart](https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml#tcp-header-flags) or you can specify the boolean of the subflag, for ex. `tcp.flags.syn==True`, `tcp.flags.ack`, etc. Check [wireshark reference](https://www.wireshark.org/docs/dfref/t/tcp.html).  
[2]: Refer to the [wireshark reference](https://www.wireshark.org/docs/dfref/t/tcp.html) for all tcp option subflags.  
[3]: In most situations, a packet with `tcp.len>0` usually has a data payload.  
[4]: `tcp contains STRING` searches the entire content of packets but will find the string inside of the data payload. See [other note](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/display_filters.md#tcp-data-payload).  
[5]: Same-ish with `tcp contains` but compares hexdigits. See [other note](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/display_filters.md#tcp-data-payload).  
  
## [TLSv1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security) [Layer 4 and 7]<sup>[1]</sup> TODO
TODO
 