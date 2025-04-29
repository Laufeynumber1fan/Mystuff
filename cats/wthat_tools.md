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
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tr>tr</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark>tshark</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#xmllint>xmllint</a></td>
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#xsltproc>xsltproc</a></td>  
            <td><a href=https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#xxd>xxd</a></td>
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
`d` Forward one half-window  
`u` Backward one half-window  
  
TROUBLESHOOTING  
  
Screen full of `~` and (END):  
If `less` is not showing anything and the whole screen is just `~` then that means the piped command may have outputted to `stderr` and not `stdout`.  
For example, the command `tshark -z help` displays the help command for `-z` but the help info is considered an error message. When you pipe this command to `less` nothing gets displayed. 
Do `2>&1` to change the console `std` to `out` and not `err`.  
`tshark -z help 2>&1 | less`


### man
  
### tcpdump  
Cmdline pcap analyser, similar to tshark but lightweight. Has simpler filters.  
**Uses [capture filters](https://www.tcpdump.org/manpages/pcap-filter.7.html) for reading and capturing pcaps**  

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
  
## tr  
Translate, replace, delete characters  

Replace tabs into new lines `cat conn.log | zeek-cut id.orig_h id.resp_h | tr '\t' '\n' | sort | uniq | wc -l`  
Lowercase to uppercase `echo "hello world" | tr 'a-z' 'A-Z'`  
  
### tshark
Cmdline wireshark, wireshark filters are processed as cmdline arguments.  
**Only uses [capture filters](https://www.tcpdump.org/manpages/pcap-filter.7.html) for capturing pcaps `-f`. Only uses display filters<sup>refs:[1, ](https://www.wireshark.org/docs/man-pages/wireshark-filter.html)</sup><sup>[2, ](https://www.wireshark.org/docs/dfref/)</sup><sup>[3](https://tshark.dev/setup/)</sup> for reading pcaps `-Y`.**
  
`-f` Capture packets with pcap-filters/tcpdump expressions.  
`-Y` Apply [display filters](https://www.wireshark.org/docs/dfref/)<sup>[1]</sup>.  
`-T` Specify different output formats like `json`, `text`, `fields`<sup>[1]</sup>, etc.  
`-D` Lists all available interfaces to listen for traffic.  
`-V` Display all packet information verbosely. Use injunction with `-Y`<sup>[2]  
`-n` Disable name resolution  
`-x` Display hex & ASCII dump  
`-E` Display options for headers when using `-T`<sup>[3]</sup>

Advanced help:  
`-G` Prints every wireshark filter. Use injunction with `egrep "\sPATTERN\." | less -Sx40`.  
`-G help` more info.  
`-G protocols`Find abbreviations of protocols.  
  
Statistics:  
`-z` Protocol Hierarchy
`-z help | less` Display help

[1a]: `-Y`, `-T fields`, `-e` are the bread and butter, `-Y` finds packets based on the display filter. `-T fields` and `-e` modifies the output to specific fields. See [1b]  

<ins>Examples</ins>:  
[1b]: Display only dns queries `tshark -r foo.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name`  
[2a]: To display packet 100 verbosely `tshark -r foo.pcap -Y frame.number==100 -V`  
[2b]: To display a specific tcp stream versbosely `tshark -r foo.pcap -Y "tcp.stream eq 0" -V`  
[3]: Add header fields for custom columns `tshark -r foo.pcap -E header=y -T fields -e ip.src -e ip.dst -e ip.proto -c 5 | less -sX40`  

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

`tshark -r foo.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport tcp.flags==2 | sort | uniq -c | sort -rn | head`  
  
### xmllint  
  
Check an xml file for format errors<sup>[[1]](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark)</sup> `xmllint foo.xml --noout`  
  
[1]: Used in converting tshark pdml to xml for viewing pcaps in web browsers.
  
### xsltproc  
  
Apply an XSLT stylesheet to an XML to convert it to html `xsltproc foo.xsl foo.xml > foo.html`  
Get the XLST stylesheet from wireshark and apply it to an XML<sup>[[1]](https://github.com/Laufeynumber1fan/Mystuff/blob/main/cats/wthat_tools.md#tshark)</sup> `xsltproc /usr/share/wireshark/pdml2html.xsl foo.xml > foo.html`
  
[1]: Used in converting tshark pdml to xml for viewing pcaps in web browsers.
  
### xxd

Get hex of output

`-p` remove offset

Get hex of "hello world" `echo -n "hello world" | xxd`
Without format, get hex of "hello world" `echo -n "hello world" | xxd -p`