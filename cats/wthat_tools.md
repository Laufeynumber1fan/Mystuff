# WHAT THE HELL ARE THESE TOOLS <img src="https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/angry.png">  
TODO: properly label these tools. Also specify if linux and windwows somehow
<table>
    <thead align=center>
        <th>1</th>
        <th colspan=26>Network Analysis</th>
    </thead>
    <tbody align=center>
        <tr>
            <td></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#gunzip>gunzip</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#less>less</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#man>man</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tcpdump>tcpdump</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark>tshark</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#xmllint>xmllint</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#xsltproc>xsltproc</a></td>
        </tr>
    </tbody>
</table>
  
### gunzip
Unzip `.gz` files, but if you want to unzip `.tar.gz`, use `tar`.

`gunzip foo.gz`

### less
Used for displaying long cmdline outputs  
  
Cmdline args:  
`-S` Really useful when a line of text is too long. -S prevents the line wrapping.  
`-x` Adjusts the number of spaces for every `\t`. For ex. `less -x40` means 40 spaces for every tab.  

Inside the shell:  
How to search: `/PATTERN` and then press `n` to iterate from next or `Shift + n (Uppercase N)` to iterate previously.  
`g` Jump to first line
`G` Jump to last line
`f` Forward one window
`b` Backward one window
  
TROUBLESHOOTING  
  
Screen full of `~` and (END):  
If `less` is not showing anything and the whole screen is just `~` then that means the piped command may have outputted to `stderr` and not `stdout`.  
For example, the command `tshark -z help` displays the help command for `-z` but the help info is considered an error message. When you pipe this command to `less` nothing gets displayed. 
Do `2>&1` to change the console `std` to `out` and not `err`.  
`tshark -z help 2>&1 | less`


### man
  
### tcpdump  
Cmdline pcap analyser, similar to tshark but lightweight. Has simpler filters.  

`-r` Read pcap.  
`-c [n]` Limit output to n number of packets.  
`-tttt` Switch timestamps to UTC.  
`-X` Convert ASCII and hex of payloads.  
`-n` Don't convert IPs to hostnames.

Only DNS packets `tcpdump -r foo.pcap port 53`  
Everything but DNS `tcpdump -r foo.pcap not port 53`  
Combination of filters `tcpdump -r foo.pcap not port 53 and not port 22`
Specific source IP `tcpdump -r foo.pcap src 192.168.0.1`
Combination of filter and args `tcpdump -r foo.pcap -ttttnXc 5 port 80`
  
### tshark
Cmdline wireshark, wireshark filters are processed as cmdline arguments.  

`-T` Specify different output formats like `json`, `text`, `fields`, etc.

Help cmds:
`-G` Prints every wireshark filter. Use injunction with `egrep` & `less`.  
`-G protocols` Print just protol filters.

`-D` Lists all available interfaces to listen for traffic.  

Statistics:  
`-z` Protocol Hierarchy  
`-z help | less` Display help

Examples:  
Filter help `tshark -G | egrep '\sip\.' | less -S -x40`
<table>
    <tbody align=center>
        <tr>
            <td>Print every filter</td>
            <td>Regex grep</td>
            <td>Match whitespace</td>
            <td>Match "ip"</td>
            <td>Match escaped "."</td>
            <td>Width overflow</td>
            <td>Every tab is 40 spaces</td>
        </tr>
        <tr>
            <td>tshark -G |</td>
            <td>egrep</td>
            <td>'\s</td>
            <td>ip</td>
            <td>\.' |</td>
            <td>less -S</td>
            <td>-x40</td>
        </tr>
    </tbody>
</table>  

`tshark -r foo.pcap -E header=y -T fields -e ip.src -e ip.dst -e ip.proto -c 5`  
`tshark -r foo.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport tcp.flags==2 | sort | uniq -c | sort -rn | head`  

### xmllint  
  
Check an xml file for format errors<sup>[[1]](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark)</sup> `xmllint foo.xml --noout`  
  
[1]: Used in converting tshark pdml to xml for viewing pcaps in web browsers.
  
### xsltproc  
  
Apply an XSLT stylesheet to an XML to convert it to html `xsltproc foo.xsl foo.xml > foo.html`  
Get the XLST stylesheet from wireshark and apply it to an XML<sup>[[1]](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark)</sup> `xsltproc /usr/share/wireshark/pdml2html.xsl foo.xml > foo.html`
  
[1]: Used in converting tshark pdml to xml for viewing pcaps in web browsers.

  