## [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#Packet_structure) [Layer 2] 
<table>
    <thead align=center>
        <th></th>
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
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td colspan=2>Hardware type</td>
            <td colspan=2>Protocol type</td>
            <td colspan=1>Hardware size<sup>[1]</sup></td>
            <td colspan=1>Protocol size<sup>[1]</sup></td>
            <td colspan=2>Opcode (request/reply/etc)</td>
            <td colspan=6>Sender MAC</td>
            <td colspan=4>Sender IP</td>
            <td colspan=6>Target MAC</td>
            <td colspan=4>Target IP</td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/a/arp.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td colspan=2>arp.hw.type</td>
            <td colspan=2>arp.proto.type</td>
            <td colspan=1>arp.hw.size<sup>[1]</sup></td>
            <td colspan=1>arp.proto.size<sup>[1]</sup></td>
            <td colspan=2>arp.opcode</td>
            <td colspan=6>arp.src.hw_mac </td>
            <td colspan=4>arp.src.proto_ipv4</td>
            <td colspan=6>arp.dst.hw_mac</td>
            <td colspan=4>arp.dst.proto_ipv4</td>
        </tr>
    </tbody>
</table>
  
1: Hardware and Protocol size is usually only 1 byte long however this can increase depending on the devices and protocols used. In most cases IPv4 over Ethernet traffic will have 28 byte ARP packets, anything more is unideal.

## [DNS Query](https://en.wikipedia.org/wiki/Domain_Name_System#Question_section) [Layer 7, Port 53] 
<table>
    <thead align=center>
        <th></th>
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
        <th>*</th>
        <th>*+1</th>
        <th>*+2</th>
        <th>*+3</th>
        <th>*+4</th>
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td colspan=2>Transaction ID</td>
            <td colspan=2>Flags</td>
            <td colspan=2>Questions</td>
            <td colspan=2>Answer RRs</td>
            <td colspan=2>Authority RRs</td>
            <td colspan=2>Additional RRs</td>
            <td>Domain Name (*)</td>
            <td colspan=2>Type<sup>[2]</sup></td>
            <td colspan=2>Class<sup>[3]</sup></td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/d/dns.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td colspan=2>dns.id</td>
            <td colspan=2>dns.flags<sup>[2]</sup></td>
            <td colspan=2>dns.count.queries</td>
            <td colspan=2>dns.count.answers</td>
            <td colspan=2>dns.count.auth_rr</td>
            <td colspan=2>dns.count.add_rr</td>
            <td>dns.qry<sup></td>
            <td colspan=2>dns.qry.type<sup>[2]</sup></td>
            <td colspan=2>dns.qry.class<sup>[3]</sup></td>
        </tr>
    </tbody>
</table>
  
1: The rest of the fields are inside a DNS query. The first field is a domain name with a variable size.  
2: i.e. DNS Record Type  
3: Defines how this DNS was transported. This is usually `IN` for Internet. Anything else may be anomalous.  

## [DNS Query Response](https://en.wikipedia.org/wiki/Domain_Name_System#Resource_records) [Layer 7, Port 53] 
<table>
	<thead align=center>
        <th></th>
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
        <th>*</th>
        <th>*+1</th>
        <th>*+2</th>
        <th>*+3</th>
        <th>*+4</th>
        <th>*+5</th>
        <th>*+6</th>
        <th>*+7</th>
        <th>*+8</th>
        <th>*+9</th>
        <th>*+10</th>
        <th>*+11</th>
        <th>*+12</th>
        <th>*+13</th>
        <th>*+14</th>
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td colspan=2>Transaction ID</td>
            <td colspan=2>Flags</td>
            <td colspan=2>Questions</td>
            <td colspan=2>Answer RRs</td>
            <td colspan=2>Authority RRs</td>
            <td colspan=2>Additional RRs</td>
            <td>Domain Name<sup>[1]</sup></td>
            <td colspan=2>Type<sup>[3]</sup></td>
            <td colspan=2>Class<sup>[5]</sup></td>
            <td colspan=4>TTL</td>
            <td colspan=2>Data Length</td>
            <td colspan=4>DNS Record</td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/d/dns.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td colspan=2>dns.id</td>
            <td colspan=2>dns.flags<sup>[2]</sup></td>
            <td colspan=2>dns.count.queries</td>
            <td colspan=2>dns.count.answers</td>
            <td colspan=2>dns.count.auth_rr</td>
            <td colspan=2>dns.count.add_rr</td>
            <td>dns.resp.name<sup>[1]</sup></td>
            <td colspan=2>dns.resp.type</td>
            <td colspan=2>dns.resp.class<sup>[5]</sup></td>
            <td colspan=4>dns.resp.ttl</td>
            <td colspan=2>dns.resp.len</td>
            <td colspan=4>dns.*<sup>[4]</sup></td>
        </tr>
    </tbody>
</table>
  
1: The rest of the fields are inside a DNS response. The first field of the response `Domain Name` has a variable size  
2: Each individual flag has a different filter. For ex. `dns.flags.response == True`. See [documentation](https://www.wireshark.org/docs/dfref/d/dns.html).   
3: i.e. DNS Record Type  
4: `dns.aaaa` for AAAA, `dns.a` for A, `dns.cname` for CNAME, etc. See [documentation](https://www.wireshark.org/docs/dfref/d/dns.html).  
5: Defines how this DNS was transported. This is usually `IN` for Internet. Anything else may be anomalous.  
  
## [HTTP](https://en.wikipedia.org/wiki/HTTP) TODO
<table>
	<thead align=center>
        <th></th>
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
        <th>*</th>
        <th>*+1</th>
        <th>*+2</th>
        <th>*+3</th>
        <th>*+4</th>
        <th>*+5</th>
        <th>*+6</th>
        <th>*+7</th>
        <th>*+8</th>
        <th>*+9</th>
        <th>*+10</th>
        <th>*+11</th>
        <th>*+12</th>
        <th>*+13</th>
        <th>*+14</th>
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td colspan=2>Transaction ID</td>
            <td colspan=2>Flags</td>
            <td colspan=2>Questions</td>
            <td colspan=2>Answer RRs</td>
            <td colspan=2>Authority RRs</td>
            <td colspan=2>Additional RRs</td>
            <td>Domain Name<sup>[1]</sup></td>
            <td colspan=2>Type<sup>[3]</sup></td>
            <td colspan=2>Class<sup>[5]</sup></td>
            <td colspan=4>TTL</td>
            <td colspan=2>Data Length</td>
            <td colspan=4>DNS Record</td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/d/dns.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td colspan=2>dns.id</td>
            <td colspan=2>dns.flags<sup>[2]</sup></td>
            <td colspan=2>dns.count.queries</td>
            <td colspan=2>dns.count.answers</td>
            <td colspan=2>dns.count.auth_rr</td>
            <td colspan=2>dns.count.add_rr</td>
            <td>dns.resp.name<sup>[1]</sup></td>
            <td colspan=2>dns.resp.type</td>
            <td colspan=2>dns.resp.class<sup>[5]</sup></td>
            <td colspan=4>dns.resp.ttl</td>
            <td colspan=2>dns.resp.len</td>
            <td colspan=4>dns.*<sup>[4]</sup></td>
        </tr>
    </tbody>
</table>

## [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure) [Layer 3]
<table>
    <thead align=center>
        <th></th>
        <th>00</th>
        <th>01</th>
        <th>02</th>
        <th>03</th>
        <th>04</th>
        <th>05</th>
        <th>06</th>
        <th>07</th>
        <th>*</th>
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td>Type<sup>[1]</sup></td>
            <td>Code</td>
            <td colspan=2>Checksum</td>
            <td colspan=2>Identifier</td>
            <td colspan=2>Sequence No.</td>
            <td>Data<sup>[2]</sup></td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/i/icmp.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td>icmp.type<sup>[1]</sup></td>
            <td>Code</td>
            <td colspan=2>Checksum</td>
            <td colspan=2>Identifier</td>
            <td colspan=2>Sequence No.</td>
            <td>Data<sup>[2]</sup></td>
        </tr>
    </tbody>
</table>
  
1: ICMP type as in ping request `icmp.type == 0`, ping reply `icmp.type == 8`, etc. See [list](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)  
2: The data payload can be used for padding bytes to reach the minimum ICMP packet size of 64 bytes. Additionally, ICMP max size is also 10^256 bytes.
  
## [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure) [Layer 4]
<table>
    <thead align=center>
        <th></th>
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
        <th colspan=8>17:57</th>
        <th>*</th>
    </thead>
    <tbody align=center>
        <tr>
            <th>Fields</th>
            <td>Source Port</td>
            <td>Dst. Port</td>
            <td colspan=4>Sequence No.</td>
            <td colspan=4>Ack. No.</td>
            <td>Data Offset<sup>[1]</sup></td>
            <td colspan=2>Flags<sup>[2]</sup></td>
            <td colspan=2>Window</td>
            <td colspan=2>Urg. Pointer</td>
            <td colspan=8>Options<sup>[3]</sup></td>
            <td>Data<sup>[4]</sup></td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/t/tcp.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td>tcp.srcport</td>
            <td>tcp.dstport</td>
            <td colspan=4>tcp.seq_raw</td>
            <td colspan=4>tcp.ack</td>
            <td>tcp.hdr_len<sup>[1]</sup></td>
            <td colspan=2>tcp.flags<sup>[2]</sup></td>
            <td colspan=2>tcp.window_size_value<sup>[5]</sup></td>
            <td colspan=2>tcp.urgent_pointer</td>
            <td colspan=8>tcp.options<sup>[2][6]</sup></td>
            <td>tcp.segment_data<sup>[3][7]</sup></td>
        </tr>
    </tbody>
</table>
  
1: Determines the size of the `Options` field. It only has a max size of the first 4 bits so the last 4 bits must always be unused.  
2: 
3: Up to 40 bytes long. Contains TCP config data with up to 10 different types of options. Multiple options can appear inside this field with up to a valid size of 0-40 bytes ([see more](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)).  
4: Maximum size of a TCP packet is 2^256. The data payload however will never reach this because of Network [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit).  
5: Wireshark also finds Calculated Window Size `tcp.window_size` and Window Size Scaling Factor `tcp.window_size_scalefactor`. Window * Window Size Scaling Factor = Calculated Window Size ([see more](https://www.lumen.com/help/en-us/network/tcp-windowing.html)).  
6: There's a lot of wireshark filters for TCP options. See [documentation](https://www.wireshark.org/docs/dfref/t/tcp.html)  
7: tcp.segment_data == a string of hexdigits. For example: `tcp.segment_data == 05:45:dc:4c:d5:06:25`  
  
## [TLSv1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security) [Layer 4 and 7]<sup>[1]</sup> TODO
<table>
    <thead align=center>
        <th></th>
        <th>00</th>
        <th>01</th>
        <th>02</th>
        <th>03</th>
        <th>04</th>
    </thead>
    <tbody align=center>
        <tr>
            <td>Fields</td>
            <td>Content Type</td>
            <td colspan=2>Version</td>
            <td colspan=2>Length</td>
        </tr>
        <tr>
            <th><a href=https://www.wireshark.org/docs/dfref/i/icmp.html><img src=https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/wireshark_icon.png>Filters</a></th>
            <td><a href=https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-5>tls.record.content_type</a></td>
            <td colspan=2>tls.record.version</td>
            <td colspan=2>tls.record.length</td>
        </tr>
    </tbody>
</table>
  
1: TLS operates at different ports as it is used by other protocols. 443 is TLS over HTTPS, 465 is TLS over SMTPS, etc.  
 