## About [drive partitioning](https://en.wikipedia.org/wiki/Disk_partitioning#Unix-like_systems) in Linux.  
> A common minimal configuration for Linux systems is to use three partitions: one holding the system files mounted on "/" (the root directory), one holding user configuration files and data mounted on /home (home directory), and a swap partition.
  
> When a partition is deleted, its entry is removed from a table and the data is no longer accessible. The data remains on the disk until it is overwritten.
  
## From an [Ubuntu article](https://help.ubuntu.com/community/HowtoPartition/OperatingSystemsAndPartitions)  
> ...when shrinking a partition, you should leave some free space to reduce the likelyhood of fragmentation and make it easier to defragment. Fragmented files will cause your computer to run slower and increase the possibility of file corruption.
A rule of thumb is to keep at least 10% of the partition as free space. Personally, I like at least 25%.
  
## Concerning partitioning and [disk drives](https://en.wikipedia.org/wiki/Hard_disk_drive#Formatting)
It is important align the partitions of disks by the start and end of logical blocks. It would be very ineffecient and error-prone for a partition to appear during a middle of a logical block.
> Data is stored on a hard drive in a series of logical blocks. Each block is delimited by markers identifying its start and end . . . These blocks often contained 512 bytes of usable data, but other sizes have been used.
  
Partitioning should be done in KiB, MiB, and GiB because HDD logical blocks are 512 bytes/block. For example, 1024 KiB is (2^10) * 1024 -> 1048576 bytes -> 2048 blocks. Refer to [table](https://www.techtarget.com/rms/onlineimages/storage-hc_exbibyte_multiples_bytes.png).
  
## Resizing partitions on VMware
`parted /example/drivename` go into the full drive
`print free` find the number
`resizepart X 100GiB` X for partition number and the new end of partition
`quit` to get out parted
  
You'll resize the actual partition but the filesystem will retain it's original size.
Do `df -h` + `fdisk -l` and you can compare the different partition sizes. It will be different.
`resize2fs /example/drivename` to sync the size of file system to the new partition size.

## Find all unique IPs in a zeek conn.log

`cat conn.log | zeek-cut id.orig_h id.resp_h | tr '\t' '\n' | sort | uniq | wc -l`
Why use `tr '\t' '\n'` (replace all \t with \n)?

When doing `cat conn.log | zeek-cut id.orig_h id.resp_h` you get this output:  
```
10.2.8.101      23.198.7.167
10.2.8.101      104.129.55.103
10.2.8.101      104.129.55.103
10.2.8.101      40.126.28.21
10.2.8.101      10.2.8.1
```
By replacing all tabs with newlines the new output will look like:
```
10.2.8.101
23.198.7.167
10.2.8.101
104.129.55.103
10.2.8.101
104.129.55.103
```
This makes it much easier to do `sort | uniq | wc -l`
  
## [Generate zeek logs in JSON format](https://docs.zeek.org/en/master/log-formats.html#zeek-json-format-logs)  
`zeek -C -r foo.pcap LogAscii::use_json=T`  
Make a separate dir for these json logs. This is useful for pretty printing zeek logs with `jq` or with firefox pretty print.  
`zeek-cut` is no longer usable. Use `jq`, for ex. `jq -c '[."id.orig_h", ."query", ."answers"]' dns.log` (see [zeek doc](https://docs.zeek.org/en/master/log-formats.html#zeek-json-format-and-jq) & [jq manual](https://stedolan.github.io/jq/manual/))

## Proper way to report malicious URLs
BAD | GOOD
--- | ---
[dontclickthiswebsite.com](https://www.youtube.com/watch?v=c8tGgVX9__Q) | dontclickthiswebsite[.]com  

This is to prevent browsers and text editors from automatically making links to URLs or to stop people from acidentally clicking the link

## Give tshark a GUI by putting pcaps into a web browser  

Step 1: Carve out a small portion of the pcap, use `-Y` to write out a display filter, `-V` to verbosely output the packet, `-T` to convert to Packet Display Markup Language (pdml)  
`tshark -r foo.pcap -Y "tcp.stream eq 0" -V -T pdml > test.xml`  
  
Step 2: convert the xml file into html with xsltproc this is a tool that applies xml styling.  
  
Wireshark already has this stylesheet preinstalled to convert pdml + xml files into html, so you're looking for the file `pdml2html.xsl`  
In kali it's `/usr/share/doc/wireshark/pdml2html.xsl.gz`. It's a gz file so you want to get into that directory and use `gunzip pdml2html.xsl.gz` to decompress it.  
  
Go back to your working dir, the full command is then:  
`xsltproc /usr/share/doc/wireshark/pdml2html.xsl test.xml > test.html`
  
Step 3: open the html into firefox
`firefox test.html`  
Now your shit has a drop down menu for packets, kinda like wireshark

### Confusion around TCP sizes
  
tcp_hdr.len - Length of the TCP header  
tcp.len - Length of TCP payload  
ip_hdr.len - Lenght of the IP header  
ip.len - Size of the IP frame (including headers, loks like)  
frame.len - Length of the on-the-wire frame (ethernet, most probably)  
frame.cap_len - Length of the capture  