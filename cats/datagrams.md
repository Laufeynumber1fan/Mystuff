## [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#Packet_structure)
<table>
    <tbody align=center>
        <tr>
            <td colspan=4>Hardware type</td>
            <td colspan=4>Protocol type</td>
        </tr>
        <tr>
            <td colspan=4>Hardware size</td>
            <td colspan=4>Protocol size</td>
        </tr>
        <tr>
            <td colspan=8>Opcode (request/reply/etc)</td>
        </tr>
        <tr>
            <td colspan=2>Sender MAC</td>
            <td colspan=2>Sender Protocol Addr. (Sender IP)</td>
            <td colspan=2>Target MAC</td>
            <td colspan=2>Target Protocol Addr. (Target IP)</td>
        </tr>
    </tbody>
</table>

## [DNS Query](https://en.wikipedia.org/wiki/Domain_Name_System#Question_section)
<table>
    <tbody align=center>
        <tr>
            <td colspan=3>Transaction ID[2]</td>
            <td colspan=3>Flags[2]</td>
        </tr>
        <tr>
            <td colspan=2>Questions[2]</td>
            <td colspan=2>Answer RRs[2]</td>
            <td>Authority RRs[2]</td>
            <td>Additional RRs[2]</td>
        </tr>
        <tr>
            <td colspan=2>Name[*]</td>
            <td colspan=2>Type[2]</td>
            <td colspan=2>Class[2]</td>
        </tr>
    </tbody>
</table>

## [DNS Query Response](https://en.wikipedia.org/wiki/Domain_Name_System#Resource_records)
<table>
	<thead align=right>
    	<th scope="col">00</th>
        <th scope="col">01</th>
        <th scope="col">02</th>
        <th scope="col">03</th>
        <th scope="col">04</th>
        <th scope="col">05</th>
        <th scope="col">06</th>
        <th scope="col">07</th>
        <th scope="col">08</th>
        <th scope="col">09</th>
        <th scope="col">10</th>
        <th scope="col">11</th>
        <th scope="col">*</th>
        <th scope="col">*+1</th>
        <th scope="col">*+2</th>
        <th scope="col">*+3</th>
        <th scope="col">*+4</th>
        <th scope="col">*+5</th>
        <th scope="col">*+6</th>
        <th scope="col">*+7</th>
        <th scope="col">*+8</th>
        <th scope="col">*+9</th>
        <th scope="col">*+10</th>
        <th scope="col">*+11</th>
        <th scope="col">*+12</th>
        <th scope="col">*+13</th>
        <th scope="col">*+14</th>
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