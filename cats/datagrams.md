## [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#Packet_structure)
<table>
    <thead align=center>
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
    </thead>
    <tbody align=center>
        <tr>
            <td colspan=4>Hardware type</td>
            <td colspan=4>Protocol type</td>
            <td colspan=4>Hardware size</td>
            <td colspan=4>Protocol size</td>
            <td colspan=8>Opcode (request/reply/etc)</td>
            <td colspan=2>Sender MAC</td>
            <td colspan=2>Sender Protocol Addr. (Sender IP)</td>
            <td colspan=2>Target MAC</td>
            <td colspan=2>Target Protocol Addr. (Target IP)</td>
        </tr>
    </tbody>
</table>

## [DNS Query](https://en.wikipedia.org/wiki/Domain_Name_System#Question_section)
<table>
    <thead align=center>
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
            <td colspan=2>Transaction ID</td>
            <td colspan=2>Flags</td>
            <td colspan=2>Questions</td>
            <td colspan=2>Answer RRs</td>
            <td colspan=2>Authority RRs</td>
            <td colspan=2>Additional RRs</td>
            <td>Name (varying length)</td>
            <td colspan=2>Type</td>
            <td colspan=2>Class</td>
        </tr>
    </tbody>
</table>

## [DNS Query Response](https://en.wikipedia.org/wiki/Domain_Name_System#Resource_records)
<table>
	<thead align=center>
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
            <td colspan=2>Transaction ID</td>
            <td colspan=2>Flags</td>
            <td colspan=2>Questions</td>
            <td colspan=2>Answer RRs</td>
            <td colspan=2>Authority RRs</td>
            <td colspan=2>Additional RRs</td>
            <td>Name (varying length)</td>
            <td colspan=2>Type</td>
            <td colspan=2>Class</td>
            <td colspan=4>TTL</td>
            <td colspan=2>Data Length</td>
            <td colspan=4>IP Address</td>
        </tr>
    </tbody>
</table>

## [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure)
<table>
    <tbody align=center>
        <tr>
            <td colspan=4>Type</td>
            <td colspan=4>Code</td>
        </tr>
        <tr>
            <td colspan=8>Checksum</td>
        </tr>
        <tr>
            <td colspan=4>Identifier</td>
            <td colspan=4>Sequence Number</tr>
        </tr>
        <tr>
            <td colspan=8>Data</td>
        </tr>
    </tbody>
</table>
  
## [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)
<table>
    <tbody align=center>
        <tr>
            <td colspan=4>Source Port</td>
            <td colspan=4>Destination Port</td>
        </tr>
        <tr>
            <td colspan=8>Sequence Number</td>
        </tr>
        <tr>
            <td colspan=8>Acknowledgement Number.</td>
        </tr>
        <tr>
            <td colspan=2>Data Offset</td>
            <td colspan=2>Flags</td>
            <td colspan=4>Window</tr>
        </tr>
        <tr>
            <td colspan=4>Checksum</td>
            <td colspan=4>Urgent Pointer</td>
        </tr>
        <tr>
            <td colspan=8>Data</td>
        </tr>
    </tbody>
</table>
  
`Destination` and `Source` ports will determine the protocol of the payload. For example, an SSH connection is encapsulated within a TCP packet, the `destination` of `port 22` will identify the TCP payload as an SSH packet.