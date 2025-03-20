About [drive partitioning](https://en.wikipedia.org/wiki/Disk_partitioning#Unix-like_systems) in Linux.  
> A common minimal configuration for Linux systems is to use three partitions: one holding the system files mounted on "/" (the root directory), one holding user configuration files and data mounted on /home (home directory), and a swap partition.
  
> When a partition is deleted, its entry is removed from a table and the data is no longer accessible. The data remains on the disk until it is overwritten.
  
From an [Ubuntu article](https://help.ubuntu.com/community/HowtoPartition/OperatingSystemsAndPartitions)  
> ...when shrinking a partition, you should leave some free space to reduce the likelyhood of fragmentation and make it easier to defragment. Fragmented files will cause your computer to run slower and increase the possibility of file corruption.
A rule of thumb is to keep at least 10% of the partition as free space. Personally, I like at least 25%.
  
Concerning partitioning and [disk drives](https://en.wikipedia.org/wiki/Hard_disk_drive#Formatting)
It is important align the partitions of disks by the start and end of logical blocks. It would be very ineffecient and error-prone for a partition to appear during a middle of a logical block.
> Data is stored on a hard drive in a series of logical blocks. Each block is delimited by markers identifying its start and end . . . These blocks often contained 512 bytes of usable data, but other sizes have been used.
  
Partitioning should be done in KiB, MiB, and GiB because HDD logical blocks are 512 bytes/block. For example, 1024 KiB is (2^10) * 1024 -> 1048576 bytes -> 2048 blocks. Refer to [table](https://www.techtarget.com/rms/onlineimages/storage-hc_exbibyte_multiples_bytes.png).
  
