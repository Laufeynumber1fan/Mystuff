## [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure)
<table>
    <tbody align=center>
        <tr>
            <td>Type</td>
            <td>Code</td>
        </tr>
        <tr>
            <td colspan=2>Checksum</td>
        </tr>
        <tr>
            <td>Identifier</td>
            <td>Sequence No.</tr>
        </tr>
        <tr>
            <td colspan=2>Data</td>
        </tr>
    </tbody>
</table>
  
## [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)
<table>
    <tbody align=center>
        <tr>
            <td colspan=2>Source Port</td>
            <td colspan=2>Dest. Port</td>
        </tr>
        <tr>
            <td colspan=4>Sequence No.</td>
        </tr>
        <tr>
            <td colspan=4>Ack. No.</td>
        </tr>
        <tr>
            <td>Data Offset</td>
            <td>Flags</td>
            <td colspan=2>Window</tr>
        </tr>
        <tr>
            <td colspan=2>Checksum</td>
            <td colspan=2>Urgent Pointer</td>
        </tr>
        <tr>
            <td colspan=4>Data</td>
        </tr>
    </tbody>
</table>