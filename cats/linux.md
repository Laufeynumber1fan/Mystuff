#### About [drive partitioning](https://en.wikipedia.org/wiki/Disk_partitioning#Unix-like_systems) in Linux.  
> A common minimal configuration for Linux systems is to use three partitions: one holding the system files mounted on "/" (the root directory), one holding user configuration files and data mounted on /home (home directory), and a swap partition.
  
> When a partition is deleted, its entry is removed from a table and the data is no longer accessible. The data remains on the disk until it is overwritten.
  
#### From an [Ubuntu article](https://help.ubuntu.com/community/HowtoPartition/OperatingSystemsAndPartitions)  
> ...when shrinking a partition, you should leave some free space to reduce the likelyhood of fragmentation and make it easier to defragment. Fragmented files will cause your computer to run slower and increase the possibility of file corruption.
A rule of thumb is to keep at least 10% of the partition as free space. Personally, I like at least 25%.
  
#### Concerning partitioning and [disk drives](https://en.wikipedia.org/wiki/Hard_disk_drive#Formatting)
It is important align the partitions of disks by the start and end of logical blocks. It would be very ineffecient and error-prone for a partition to appear during a middle of a logical block.
> Data is stored on a hard drive in a series of logical blocks. Each block is delimited by markers identifying its start and end . . . These blocks often contained 512 bytes of usable data, but other sizes have been used.
  
Partitioning should be done in KiB, MiB, and GiB because HDD logical blocks are 512 bytes/block. For example, 1024 KiB is (2^10) * 1024 -> 1048576 bytes -> 2048 blocks. Refer to [table](https://www.techtarget.com/rms/onlineimages/storage-hc_exbibyte_multiples_bytes.png).
  
#### Resizing partitions on VMware
`parted /example/drivename` go into the full drive
`print free` find the number
`resizepart X 100GiB` X for partition number and the new end of partition
`quit` to get out parted
  
You'll resize the actual partition but the filesystem will retain it's original size.
Do `df -h` + `fdisk -l` and you can compare the different partition sizes. It will be different.
`resize2fs /example/drivename` to sync the size of file system to the new partition size.

#### Find all unique IPs in a zeek conn.log

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

#### [Generate zeek logs in JSON format](https://docs.zeek.org/en/master/log-formats.html#zeek-json-format-logs)  
`zeek -C -r foo.pcap LogAscii::use_json=T`  
Make a separate dir for these json logs. This is useful for pretty printing zeek logs with `jq` or with firefox pretty print.  
`zeek-cut` is no longer usable. Use `jq`, for ex. `jq -c '[."id.orig_h", ."query", ."answers"]' dns.log` (see [zeek doc](https://docs.zeek.org/en/master/log-formats.html#zeek-json-format-and-jq) & [jq manual](https://stedolan.github.io/jq/manual/))
